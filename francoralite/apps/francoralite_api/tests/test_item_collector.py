# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item Collector tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_collector import ItemCollectorFactory
from .fake_data.fake_sound import CleanMediaMixin
from ..models.item_collector import ItemCollector
from ..models.authority import Authority
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_collector objects
ITEMCOLLECTOR_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('collector', dict),
]

# Expected keys for MODEL objects
ITEMCOLLECTOR_FIELDS = sorted(
    [item[0] for item in ITEMCOLLECTOR_STRUCTURE])


@pytest.mark.django_db
class TestItemCollectorList(CleanMediaMixin, APITestCase):
    """
    This class manage all ItemCollector tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        
        # Create a set of sample data
        ItemCollectorFactory.create_batch(6)

    def test_can_get_item_collector_list(self):
        """
        Ensure ItemCollector objects exists
        """
        # kwargs for the related tables
        url = reverse('itemcollector-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_collectors = ItemCollector.objects.all()
        self.assertEqual(len(item_collectors), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMCOLLECTOR_STRUCTURE)
    def test_has_valid_item_collector_values(self, attribute, attribute_type):
        """
        Ensure ItemCollector objects have valid values
        """

        # Kwargs for the related tables
        url = reverse('itemcollector-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_collector in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_collector.keys()), ITEMCOLLECTOR_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_collector[attribute], str)
            else:
                self.assertIsInstance(
                    item_collector[attribute], attribute_type)
            self.assertIsNot(item_collector[attribute], '')

    def test_get_an_item_collector(self):
        """
        Ensure we can get an ItemCollector objects
        using an existing id
        """

        item = ItemCollector.objects.first()

        url = reverse('itemcollector-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.collector.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_collector(self):
        """
        Ensure we can create an ItemCollector object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemCollectorFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = 1
        data['collector'] = 2

        url = reverse('itemcollector-list', kwargs={
            'item_pk': data['item']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMCOLLECTOR_FIELDS)

        url = reverse(
            'itemcollector-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_collector(self):
        """
        Ensure we can delete an ItemCollector object
        """

        item = ItemCollector.objects.first()

        # Delete this object
        # FIXIT  kwargs for the related tables
        url = reverse(
            'itemcollector-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.collector.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemCollector removed
        url_get = reverse(
            'itemcollector-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.collector.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
