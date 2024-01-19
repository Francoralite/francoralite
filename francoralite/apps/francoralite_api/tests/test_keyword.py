# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Keyword tests
"""

import factory
import pytest

from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.keyword import KeywordFactory
from ..models.keyword import Keyword

from .keycloak import get_token

# Expected structure for Keyword objects
KEYWORD_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
KEYWORD_FIELDS = sorted(
    [item[0] for item in KEYWORD_STRUCTURE])


@pytest.mark.django_db
class TestKeywordList(APITestCase):
    """
    This class manage all Keyword tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")

        # Create a set of sample data
        KeywordFactory.create_batch(6)

    def test_can_get_keyword_list(self):
        """
        Ensure Keyword objects exists
        """
        url = reverse('keyword-list')

        # ORM side
        keywords = Keyword.objects.all()
        self.assertEqual(len(keywords), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(KEYWORD_STRUCTURE)
    def test_has_valid_keyword_values(
            self, attribute, attribute_type):
        """
        Ensure Keyword objects have valid values
        """

        url = reverse('keyword-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for keyword in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    keyword.keys()), KEYWORD_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(keyword[attribute], str)
            else:
                self.assertIsInstance(
                    keyword[attribute], attribute_type)
            self.assertIsNot(keyword[attribute], '')

    def test_get_an_keyword(self):
        """
        Ensure we can get an Keyword objects
        using an existing id
        """

        item = Keyword.objects.first()
        url = reverse('keyword-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_keyword(self):
        """
        Ensure we can create an Keyword object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=KeywordFactory)
        url = reverse('keyword-list')
        print("+-+-+-+")
        print(data)
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            KEYWORD_FIELDS)

        url = reverse(
            'keyword-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_keyword(self):
        """
        Ensure we can update an Keyword object
        """

        item = Keyword.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'keyword-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'keyword-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            KEYWORD_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_keyword(self):
        """
        Ensure we can patch an Keyword object
        """

        item = Keyword.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'keyword-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            KEYWORD_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_keyword(self):
        """
        Ensure we can delete an Keyword object
        """

        item = Keyword.objects.first()

        # Delete this object
        url = reverse(
            'keyword-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Keyword removed
        url_get = reverse(
            'keyword-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
