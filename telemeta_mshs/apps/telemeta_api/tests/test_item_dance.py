# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Institution tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_dance import ItemDanceFactory
from ..models.item_dance import ItemDance
# Models related
from ..models.dance import Dance
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_dance objects
ITEMDANCE_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('dance', dict),
]

# Expected keys for MODEL objects
ITEMDANCE_FIELDS = sorted(
    [item[0] for item in ITEMDANCE_STRUCTURE])


@pytest.mark.django_db
class TestItemDanceList(APITestCase):
    """
    This class manage all ItemDance tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        ItemDanceFactory.create_batch(1)

    def test_can_get_item_dance_list(self):
        """
        Ensure ItemDance objects exists
        """
        # kwargs for the related tables
        url = reverse('itemdance-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_dances = ItemDance.objects.all()
        self.assertEqual(len(item_dances), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMDANCE_STRUCTURE)
    def test_has_valid_item_dance_values(self, attribute, attribute_type):
        """
        Ensure ItemDance objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemdance-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_dance in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_dance.keys()), ITEMDANCE_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(item_dance[attribute], basestring)
                else:
                    self.assertIsInstance(item_dance[attribute], str)
            else:
                self.assertIsInstance(item_dance[attribute], attribute_type)
            self.assertIsNot(item_dance[attribute], '')

    def test_get_an_item_dance(self):
        """
        Ensure we can get an ItemDance objects
        using an existing id
        """

        item = ItemDance.objects.first()
        #  kwargs for the related tables
        url = reverse('itemdance-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.dance.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_dance(self):
        """
        Ensure we can create an ItemDance object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemDanceFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = Item.objects.first().id
        data['dance'] = Dance.objects.first().id

        url = reverse('itemdance-list', kwargs={
            'item_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMDANCE_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemdance-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['dance']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_dance(self):
        """
        Ensure we can delete an ItemDance object
        """

        item = ItemDance.objects.first()

        # Delete this object
        # kwargs for the related tables
        url = reverse(
            'itemdance-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.dance.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemDance removed
        # kwargs for the related tables
        url_get = reverse(
            'itemdance-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.dance.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
