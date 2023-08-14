# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Test Coirault
"""

# Context from Class or Interface francoralite/apps/francoralite_api/tests/test_coirault.py:TestCoirault

import factory
import pytest
import sys

from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase


from .keycloak import get_token

from .factories.item_coirault import ItemCoiraultFactory
from ..models.item_coirault import ItemCoirault


ITEMCOIRAULT_STRUCTURE = [
    ("id", int),
    ("item", dict),
    ("coirault", dict),
]

ITEMCOIRAULT_FIELDS = sorted([item[0] for item in ITEMCOIRAULT_STRUCTURE])


@pytest.mark.django_db
class TestItemCoiraultList(APITestCase):
    """
    This class manage all ItemCoirault tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)

        # Create a set of sample data
        ItemCoiraultFactory.create_batch(6)

    def test_can_get_item_coirault_list(self):
        """
        Ensure ItemCoirault objects exists
        """
        # kwargs for the related tables
        url = reverse("itemcoirault-list", kwargs={"item_pk": 1})

        # ORM side
        item_coiraults = ItemCoirault.objects.all()
        self.assertEqual(len(item_coiraults), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMCOIRAULT_STRUCTURE)
    def test_has_valid_item_coirault_values(self, attribute, attribute_type):
        """
        Ensure ItemCoirault objects have valid values
        """

        # kwargs for the related tables
        url = reverse("itemcoirault-list", kwargs={"item_pk": 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        for item_coirault in response.data:
            # check only expected attributes returned
            self.assertEqual(
                sorted(item_coirault.keys()), ITEMCOIRAULT_FIELDS
            )

            # ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_coirault[attribute], str)
            else:
                self.assertIsInstance(item_coirault[attribute], attribute_type)
            self.assertIsNot(item_coirault[attribute], '')

    def test_get_an_item_coirault(self):
        """
        Ensure we can get an ItemCoirault objects using an existing id
        """
        
        item = ItemCoirault.objects.first()

        url = reverse("itemcoirault-detail", kwargs={"item_pk": 1, "pk": item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_coirault(self):
        """
        Ensure we can create an ItemCoirault object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemCoiraultFactory
        )

        # Convert the related entity in dictionnary.
        # Then they will be easily converted in JSON format.
        data['item'] = 1
        data['coirault'] = 2

        url = reverse("itemcoirault-list", kwargs={"item_pk": 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), ITEMCOIRAULT_FIELDS)

        url = reverse(
            'itemcoirault-detail', kwargs={
                'item_pk': response.data['item']['id'],
                'pk': response.data['id']
            }
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_coirault(self):
        """
        Ensure we can delete an ItemCoirault object
        """

        item = ItemCoirault.objects.first()

        # Delete this object
        url = reverse("itemcoirault-detail", kwargs={"item_pk": 1, "pk": item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemCoirault removed
        url_get = reverse(
            'itemcoirault-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.coirault.id
            }
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)



        
