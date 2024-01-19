# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Usefulness tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.usefulness import UsefulnessFactory
from ..models.usefulness import Usefulness

from .keycloak import get_token

# Expected structure for Usefulness objects
USEFULNESS_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
USEFULNESS_FIELDS = sorted(
    [item[0] for item in USEFULNESS_STRUCTURE])


@pytest.mark.django_db
class TestUsefulnessList(APITestCase):
    """
    This class manage all Usefulness tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")
        
        # Create a set of sample data
        UsefulnessFactory.create_batch(6)

    def test_can_get_usefulness_list(self):
        """
        Ensure Usefulness objects exists
        """
        url = reverse('usefulness-list')

        # ORM side
        usefulnesss = Usefulness.objects.all()
        self.assertEqual(len(usefulnesss), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(USEFULNESS_STRUCTURE)
    def test_has_valid_usefulness_values(
            self, attribute, attribute_type):
        """
        Ensure Usefulness objects have valid values
        """

        url = reverse('usefulness-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for usefulness in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    usefulness.keys()), USEFULNESS_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(usefulness[attribute], str)
            else:
                self.assertIsInstance(usefulness[attribute], attribute_type)
            self.assertIsNot(usefulness[attribute], '')

    def test_get_an_usefulness(self):
        """
        Ensure we can get an Usefulness objects
        using an existing id
        """

        item = Usefulness.objects.first()
        url = reverse('usefulness-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_usefulness(self):
        """
        Ensure we can create an Usefulness object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=UsefulnessFactory)
        url = reverse('usefulness-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            USEFULNESS_FIELDS)

        url = reverse(
            'usefulness-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_usefulness(self):
        """
        Ensure we can update an Usefulness object
        """

        item = Usefulness.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'usefulness-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'usefulness-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            USEFULNESS_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_usefulness(self):
        """
        Ensure we can patch an Usefulness object
        """

        item = Usefulness.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'usefulness-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            USEFULNESS_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_usefulness(self):
        """
        Ensure we can delete an Usefulness object
        """

        item = Usefulness.objects.first()

        # Delete this object
        url = reverse(
            'usefulness-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Usefulness removed
        url_get = reverse(
            'usefulness-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
