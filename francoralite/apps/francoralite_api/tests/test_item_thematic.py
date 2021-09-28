# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item Thematic tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_thematic import ItemThematicFactory
from ..models.item_thematic import ItemThematic
# Models related
from ..models.thematic import Thematic
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_thematic objects
ITEMTHEMATIC_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('thematic', dict),
]

# Expected keys for MODEL objects
ITEMTHEMATIC_FIELDS = sorted(
    [item[0] for item in ITEMTHEMATIC_STRUCTURE])


@pytest.mark.django_db
class TestItemThematicList(APITestCase):
    """
    This class manage all ItemThematic tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        ItemThematicFactory.create_batch(6)

    def test_can_get_item_thematic_list(self):
        """
        Ensure ItemThematic objects exists
        """
        # kwargs for the related tables
        url = reverse('itemthematic-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_thematics = ItemThematic.objects.all()
        self.assertEqual(len(item_thematics), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMTHEMATIC_STRUCTURE)
    def test_has_valid_item_thematic_values(self, attribute, attribute_type):
        """
        Ensure ItemThematic objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemthematic-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_thematic in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_thematic.keys()), ITEMTHEMATIC_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_thematic[attribute], str)
            else:
                self.assertIsInstance(item_thematic[attribute], attribute_type)
            self.assertIsNot(item_thematic[attribute], '')

    def test_get_an_item_thematic(self):
        """
        Ensure we can get an ItemThematic objects
        using an existing id
        """

        item = ItemThematic.objects.first()
        # kwargs for the related tables
        url = reverse('itemthematic-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.thematic.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_thematic(self):
        """
        Ensure we can create an ItemThematic object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemThematicFactory)

        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.
        data['item'] = 1
        data['thematic'] = 2

        url = reverse('itemthematic-list', kwargs={
            'item_pk': data['item']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMTHEMATIC_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemthematic-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_thematic(self):
        """
        Ensure we can delete an ItemThematic object
        """

        item = ItemThematic.objects.first()

        # Delete this object
        # kwargs for the related tables
        url = reverse(
            'itemthematic-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.thematic.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemThematic removed
        # kwargs for the related tables
        url_get = reverse(
            'itemthematic-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.thematic.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
