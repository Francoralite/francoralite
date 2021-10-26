# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Language tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.language import LanguageFactory
from ..models.language import Language

from .keycloak import get_token

# Expected structure for Language objects
LANGUAGE_STRUCTURE = [
    ('id', int),
    ('identifier', str),
    ('part2B', str),
    ('part2T', str),
    ('part1', str),
    ('scope', str),
    ('type', str),
    ('name', str),
    ('comment', str),
]

# Expected keys for MODEL objects
LANGUAGE_FIELDS = sorted([item[0] for item in LANGUAGE_STRUCTURE])


@pytest.mark.django_db
class TestLanguageList(APITestCase):
    """
    This class manage all Language tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")
        
        # Create a set of sample data
        LanguageFactory.create_batch(6)

    def test_can_get_language_list(self):
        """
        Ensure Language objects exists
        """
        url = reverse('language-list')

        # ORM side
        languages = Language.objects.all()
        self.assertEqual(len(languages), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(LANGUAGE_STRUCTURE)
    def test_has_valid_language_values(self, attribute, attribute_type):
        """
        Ensure Language objects have valid values
        """

        url = reverse('language-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for language in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(language.keys()), LANGUAGE_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
               self.assertIsInstance(language[attribute], str)
            else:
                self.assertIsInstance(language[attribute], attribute_type)
            self.assertIsNot(language[attribute], '')

    def test_get_a_language(self):
        """
        Ensure we can get an Language objects
        using an existing id
        """

        item = Language.objects.first()
        url = reverse('language-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_language(self):
        """
        Ensure we can create an Language object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=LanguageFactory)
        url = reverse('language-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            LANGUAGE_FIELDS)

        url = reverse(
            'language-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_a_language(self):
        """
        Ensure we can update an Language object
        """

        item = Language.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'language-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'language-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            LANGUAGE_FIELDS)
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_a_language(self):
        """
        Ensure we can patch an Language object
        """

        item = Language.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'language-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            LANGUAGE_FIELDS)
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_a_language(self):
        """
        Ensure we can delete an Language object
        """

        item = Language.objects.first()

        # Delete this object
        url = reverse(
            'language-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Language removed
        url_get = reverse(
            'language-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
