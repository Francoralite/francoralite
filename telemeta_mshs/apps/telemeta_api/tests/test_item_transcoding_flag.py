# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ItemTranscodingFlag tests
"""

import factory
import pytest
import sys

from django.forms.models import model_to_dict
from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_transcoding_flag import ItemTranscodingFlagFactory
from ..models.item_transcoding_flag import ItemTranscodingFlag

# Models related
from ..models.item import Item

# Expected structure for Item_transcoding_flag objects
ITEMTRANSCODINGFLAG_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('mime_type', str),
    ('date', str),
    ('value', bool)
]

# Expected keys for MODEL objects
ITEMTRANSCODINGFLAG_FIELDS = sorted(
    [item[0] for item in ITEMTRANSCODINGFLAG_STRUCTURE])


@pytest.mark.django_db
class TestItemTranscodingFlagList(APITestCase):
    """
    This class manage all ItemTranscodingFlag tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        ItemTranscodingFlagFactory.create_batch(6)

    def test_can_get_item_transcoding_flag_list(self):
        """
        Ensure ItemTranscodingFlag objects exists
        """
        url = reverse('itemtranscodingflag-list',  kwargs={
            'item_pk': 1})

        # ORM side
        item_transcoding_flags = ItemTranscodingFlag.objects.all()
        self.assertEqual(len(item_transcoding_flags), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(ITEMTRANSCODINGFLAG_STRUCTURE)
    def test_has_valid_item_transcoding_flag_values(self,
                                                    attribute, attribute_type):
        """
        Ensure ItemTranscodingFlag objects have valid values
        """

        url = reverse('itemtranscodingflag-list', kwargs={'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_transcoding_flag in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_transcoding_flag.keys()),
                ITEMTRANSCODINGFLAG_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        item_transcoding_flag[attribute], basestring)
                else:
                    self.assertIsInstance(
                        item_transcoding_flag[attribute], str)
            else:
                self.assertIsInstance(
                    item_transcoding_flag[attribute], attribute_type)
            self.assertIsNot(item_transcoding_flag[attribute], '')

    def test_get_an_item_transcoding_flag(self):
        """
        Ensure we can get an ItemTranscodingFlag objects
        using an existing id
        """

        item = ItemTranscodingFlag.objects.first()
        url = reverse('itemtranscodingflag-detail',
                      kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_transcoding_flag(self):
        """
        Ensure we can create an ItemTranscodingFlag object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemTranscodingFlagFactory)
        data['item'] = Item.objects.first().id
        print("---------------------")
        print(data)
        print("---------------------")

        url = reverse('itemtranscodingflag-list', kwargs={
            'item_pk': Item.objects.first().id})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMTRANSCODINGFLAG_FIELDS)

        url = reverse(
            'itemtranscodingflag-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_item_transcoding_flag(self):
        """
        Ensure we can update an ItemTranscodingFlag object
        """

        item = ItemTranscodingFlag.objects.first()
        self.assertNotEqual(item.mime_type, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'itemtranscodingflag-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        data = self.client.get(url_get).data

        data['mime_type'] = 'foobar_test_put'
        data['item'] = data['item']['id']
        url = reverse(
            'itemtranscodingflag-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMTRANSCODINGFLAG_FIELDS)

        self.assertEqual(response.data['mime_type'], 'foobar_test_put')

    def test_patch_an_item_transcoding_flag(self):
        """
        Ensure we can patch an ItemTranscodingFlag object
        """

        item = ItemTranscodingFlag.objects.first()

        self.assertNotEqual(item.mime_type, 'foobar_test_patch')

        data = {'mime_type': 'foobar_test_patch'}
        url = reverse(
            'itemtranscodingflag-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMTRANSCODINGFLAG_FIELDS)

        self.assertEqual(response.data['mime_type'], 'foobar_test_patch')

    def test_delete_an_item_transcoding_flag(self):
        """
        Ensure we can delete an ItemTranscodingFlag object
        """

        item = ItemTranscodingFlag.objects.first()

        # Delete this object
        url = reverse(
            'itemtranscodingflag-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemTranscodingFlag removed
        url_get = reverse(
            'itemtranscodingflag-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
