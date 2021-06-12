# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
HornbostelSachs tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.hornbostelsachs import HornbostelSachsFactory
from ..models.hornbostelsachs import HornbostelSachs

from .keycloak import get_token

# Expected structure for Hornbostelsachs objects
HORNBOSTELSACHS_STRUCTURE = [
    ('id', int),
    ('number', str),
    ('name', str),
]

# Expected keys for MODEL objects
HORNBOSTELSACHS_FIELDS = sorted([item[0] for item in HORNBOSTELSACHS_STRUCTURE])


@pytest.mark.django_db
class TestHornbostelSachsList(APITestCase):
    """
    This class manage all HornbostelSachs tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        HornbostelSachsFactory.create_batch(6)

    def test_can_get_hornbostelsachs_list(self):
        """
        Ensure HornbostelSachs objects exists
        """
        url = reverse('hornbostelsachs-list')

        # ORM side
        hornbostelsachss = HornbostelSachs.objects.all()
        self.assertEqual(len(hornbostelsachss), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(HORNBOSTELSACHS_STRUCTURE)
    def test_has_valid_hornbostelsachs_values(self, attribute, attribute_type):
        """
        Ensure HornbostelSachs objects have valid values
        """

        url = reverse('hornbostelsachs-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for hornbostelsachs in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(hornbostelsachs.keys()), HORNBOSTELSACHS_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(hornbostelsachs[attribute], str)
            else:
                self.assertIsInstance(hornbostelsachs[attribute], attribute_type)
            self.assertIsNot(hornbostelsachs[attribute], '')

    def test_get_an_hornbostelsachs(self):
        """
        Ensure we can get an HornbostelSachs objects
        using an existing id
        """

        item = HornbostelSachs.objects.first()
        url = reverse('hornbostelsachs-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_hornbostelsachs(self):
        """
        Ensure we can create an HornbostelSachs object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=HornbostelSachsFactory)
        url = reverse('hornbostelsachs-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            HORNBOSTELSACHS_FIELDS)

        url = reverse(
            'hornbostelsachs-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_hornbostelsachs(self):
        """
        Ensure we can update an HornbostelSachs object
        """

        item = HornbostelSachs.objects.first()
        # FIXIT --------------------
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'hornbostelsachs-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        # FIXIT --------------------
        data['name'] = 'foobar_test_put'
        url = reverse(
            'hornbostelsachs-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            HORNBOSTELSACHS_FIELDS)
        # FIXIT --------------------
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_hornbostelsachs(self):
        """
        Ensure we can patch an HornbostelSachs object
        """

        item = HornbostelSachs.objects.first()
        # FIXIT --------------------
        self.assertNotEqual(item.name, 'foobar_test_patch')

        # FIXIT --------------------
        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'hornbostelsachs-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            HORNBOSTELSACHS_FIELDS)
        # FIXIT --------------------
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_hornbostelsachs(self):
        """
        Ensure we can delete an HornbostelSachs object
        """

        item = HornbostelSachs.objects.first()

        # Delete this object
        url = reverse(
            'hornbostelsachs-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure HornbostelSachs removed
        url_get = reverse(
            'hornbostelsachs-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
