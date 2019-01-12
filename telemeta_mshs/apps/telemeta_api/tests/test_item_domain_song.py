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

from django.forms.models import model_to_dict
from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_domain_song import ItemDomainSongFactory
from ..models.item_domain_song import ItemDomainSong
# Models related
from ..models.domain_song import DomainSong
from ..models.item import Item

# Expected structure for Item_domain_song objects
ITEMDOMAINSONG_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('domain_song', dict),
]

# Expected keys for MODEL objects
ITEMDOMAINSONG_FIELDS = sorted(
    [item[0] for item in ITEMDOMAINSONG_STRUCTURE])


@pytest.mark.django_db
class TestItemDomainSongList(APITestCase):
    """
    This class manage all ItemDomainSong tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        ItemDomainSongFactory.create_batch(1)

    def test_can_get_item_domain_song_list(self):
        """
        Ensure ItemDomainSong objects exists
        """

        url = reverse('itemdomainsong-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_domain_songs = ItemDomainSong.objects.all()
        self.assertEqual(len(item_domain_songs), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMDOMAINSONG_STRUCTURE)
    def test_has_valid_item_domain_song_values(self,
                                               attribute, attribute_type):
        """
        Ensure ItemDomainSong objects have valid values
        """

        url = reverse('itemdomainsong-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_domain_song in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_domain_song.keys()), ITEMDOMAINSONG_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        item_domain_song[attribute], basestring)
                else:
                    self.assertIsInstance(
                        item_domain_song[attribute], str)
            else:
                self.assertIsInstance(
                    item_domain_song[attribute], attribute_type)
            self.assertIsNot(item_domain_song[attribute], '')

    def test_get_an_item_domain_song(self):
        """
        Ensure we can get an ItemDomainSong objects
        using an existing id
        """

        item = ItemDomainSong.objects.first()

        url = reverse('itemdomainsong-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.domain_song.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_domain_song(self):
        """
        Ensure we can create an ItemDomainSong object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemDomainSongFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = Item.objects.first().id
        data['domain_song'] = DomainSong.objects.first().id

        url = reverse('itemdomainsong-list', kwargs={
            'item_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMDOMAINSONG_FIELDS)

        url = reverse(
            'itemdomainsong-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['domain_song']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_domain_song(self):
        """
        Ensure we can delete an ItemDomainSong object
        """

        item = ItemDomainSong.objects.first()

        # Delete this object
        url = reverse(
            'itemdomainsong-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.domain_song.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemDomainSong removed
        url_get = reverse(
            'itemdomainsong-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.domain_song.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
