# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item Domain_Music tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_domain_music import ItemDomainMusicFactory
from .fake_data.fake_sound import CleanMediaMixin
from ..models.item_domain_music import ItemDomainMusic
# Models related
from ..models.domain_music import DomainMusic
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_domain_music objects
ITEMDOMAINMUSIC_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('domain_music', dict),
]

# Expected keys for MODEL objects
ITEMDOMAINMUSIC_FIELDS = sorted(
    [item[0] for item in ITEMDOMAINMUSIC_STRUCTURE])


@pytest.mark.django_db
class TestItemDomainMusicList(CleanMediaMixin, APITestCase):
    """
    This class manage all ItemDomainMusic tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        
        # Create a set of sample data
        ItemDomainMusicFactory.create_batch(6)

    def test_can_get_item_domain_music_list(self):
        """
        Ensure ItemDomainMusic objects exists
        """

        url = reverse('itemdomainmusic-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_domain_musics = ItemDomainMusic.objects.all()
        self.assertEqual(len(item_domain_musics), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMDOMAINMUSIC_STRUCTURE)
    def test_has_valid_item_domain_music_values(self,
                                                attribute, attribute_type):
        """
        Ensure ItemDomainMusic objects have valid values
        """

        url = reverse('itemdomainmusic-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_domain_music in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_domain_music.keys()), ITEMDOMAINMUSIC_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_domain_music[attribute], str)
            else:
                self.assertIsInstance(
                    item_domain_music[attribute], attribute_type)
            self.assertIsNot(item_domain_music[attribute], '')

    def test_get_an_item_domain_music(self):
        """
        Ensure we can get an ItemDomainMusic objects
        using an existing id
        """

        item = ItemDomainMusic.objects.first()

        url = reverse('itemdomainmusic-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.domain_music.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_domain_music(self):
        """
        Ensure we can create an ItemDomainMusic object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemDomainMusicFactory)

        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.
        data['item'] = 1
        data['domain_music'] = 2

        url = reverse('itemdomainmusic-list', kwargs={
            'item_pk': data['item']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMDOMAINMUSIC_FIELDS)

        url = reverse(
            'itemdomainmusic-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_domain_music(self):
        """
        Ensure we can delete an ItemDomainMusic object
        """

        item = ItemDomainMusic.objects.first()

        # Delete this object
        url = reverse(
            'itemdomainmusic-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.domain_music.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemDomainMusic removed
        url_get = reverse(
            'itemdomainmusic-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.domain_music.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
