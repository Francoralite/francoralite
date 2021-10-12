# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item Informer tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_informer import ItemInformerFactory
from ..models.item_informer import ItemInformer
from ..models.authority import Authority
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_informer objects

ITEMINFORMER_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('informer', dict),
]

# Expected keys for MODEL objects
ITEMINFORMER_FIELDS = sorted(
    [item[0] for item in ITEMINFORMER_STRUCTURE])


@pytest.mark.django_db
class TestItemInformerList(APITestCase):
    """
    This class manage all ItemInformer tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        ItemInformerFactory.create_batch(6)

    def test_can_get_item_informer_list(self):
        """
        Ensure ItemInformer objects exists
        """

        url = reverse('iteminformer-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_informers = ItemInformer.objects.all()
        self.assertEqual(len(item_informers), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMINFORMER_STRUCTURE)
    def test_has_valid_item_informer_values(self, attribute, attribute_type):
        """
        Ensure ItemInformer objects have valid values
        """

        url = reverse('iteminformer-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_informer in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_informer.keys()), ITEMINFORMER_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_informer[attribute], str)
            else:
                self.assertIsInstance(item_informer[attribute], attribute_type)
            self.assertIsNot(item_informer[attribute], '')

    def test_get_an_item_informer(self):
        """
        Ensure we can get an ItemInformer objects
        using an existing id
        """

        item = ItemInformer.objects.first()
        url = reverse('iteminformer-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.informer.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_informer(self):
        """
        Ensure we can create an ItemInformer object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemInformerFactory)

        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.
        data['item'] = 1 
        data['informer'] = 2 

        url = reverse('iteminformer-list', kwargs={
            'item_pk': data['item']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMINFORMER_FIELDS)

        url = reverse(
            'iteminformer-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_informer(self):
        """
        Ensure we can delete an ItemInformer object
        """

        item = ItemInformer.objects.first()

        # Delete this object
        url = reverse(
            'iteminformer-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.informer.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemInformer removed
        url_get = reverse(
            'iteminformer-detail', kwargs={
                 'item_pk': item.item.id,
                 'pk': item.informer.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
