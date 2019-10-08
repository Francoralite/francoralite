# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ItemMarker tests
"""

import factory
import pytest
import sys
from types import NoneType

from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_marker import ItemMarkerFactory
from ..models.item_marker import ItemMarker

# Models related
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_marker objects
ITEM_MARKER_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('time', float),
    ('title', str),
    ('date', str),
    ('description', str),
    ('author', dict),
]

# Expected keys for MODEL objects
ITEMMARKER_FIELDS = sorted([item[0] for item in ITEM_MARKER_STRUCTURE])


@pytest.mark.django_db
class TestItemMarkerList(APITestCase):
    """
    This class manage all ItemMarker tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])
        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        ItemMarkerFactory.create_batch(6)

    def test_can_get_item_marker_list(self):
        """
        Ensure ItemMarker objects exists
        using an existing item's id
        """
        # ORM side
        item_markers = ItemMarker.objects.all()
        self.assertEqual(len(item_markers), 6)

        # API side
        item = Item.objects.first()
        # Retrieve the markers related to an item
        url = reverse('itemmarker-list',
                      kwargs={'item_pk': item.id})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(ITEM_MARKER_STRUCTURE)
    def test_has_valid_item_marker_values(self, attribute, attribute_type):
        """
        Ensure ItemMarker objects have valid values
        """

        url = reverse('itemmarker-list', kwargs={'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_marker in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_marker.keys()), ITEMMARKER_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(item_marker[attribute], basestring)
                else:
                    self.assertIsInstance(item_marker[attribute], str)
            else:
                if attribute == 'author':
                    # Because of author field
                    try:
                        self.assertIsInstance(item_marker[attribute], NoneType)
                    except AssertionError:
                        self.assertIsInstance(
                            item_marker[attribute], attribute_type)
                else:
                    self.assertIsInstance(
                        item_marker[attribute], attribute_type)
            self.assertIsNot(item_marker[attribute], '')

    def test_get_an_item_marker(self):
        """
        Ensure we can get an ItemMarker objects
        using an existing id
        """

        item = ItemMarker.objects.first()
        url = reverse('itemmarker-detail',
                      kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_marker(self):
        """
        Ensure we can create an ItemMarker object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemMarkerFactory)
        data['item'] = Item.objects.first().id
        # data['user'] = User.objects.first().id

        url = reverse('itemmarker-list', kwargs={
            'item_pk': Item.objects.first().id})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMMARKER_FIELDS)

        url = reverse(
            'itemmarker-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_item_marker(self):
        """
        Ensure we can update an ItemMarker object
        """

        item = ItemMarker.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'itemmarker-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        data = self.client.get(url_get).data

        data['title'] = 'foobar_test_put'
        data['item'] = data['item']['id']
        url = reverse(
            'itemmarker-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMMARKER_FIELDS)

        self.assertEqual(response.data['title'], 'foobar_test_put')

    def test_patch_an_item_marker(self):
        """
        Ensure we can patch an ItemMarker object
        """

        item = ItemMarker.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_patch')

        data = {'title': 'foobar_test_patch'}
        url = reverse(
            'itemmarker-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMMARKER_FIELDS)

        self.assertEqual(response.data['title'], 'foobar_test_patch')

    def test_delete_an_item_marker(self):
        """
        Ensure we can delete an ItemMarker object
        """

        item = ItemMarker.objects.first()

        # Delete this object
        url = reverse(
            'itemmarker-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemMarker removed
        url_get = reverse(
            'itemmarker-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
