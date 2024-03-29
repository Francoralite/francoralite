# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item tests
"""

import factory
import pytest

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item import ItemFactory, ItemCompleteFactory
from .factories.recording_context import RecordingContextFactory
from .factories.performancecollectionmusician import PerformanceCollectionMusicianFactory
from .fake_data.fake_sound import CleanMediaMixin
from ..models.item import Item
from ..models.collection import Collection
from ..models.mediatype import MediaType
from ..models.coupe import Coupe
from ..models.recording_context import RecordingContext
from ..models.performance_collection_musician import PerformanceCollectionMusician
from .fake_data.fake_sound import create_tmp_sound

from .keycloak import get_token

# Expected structure for Item objects

ITEM_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('title', str),
    ('alt_title', str),
    ('trans_title', str),
    ('description', str),
    ('code', str),
    ('code_partner', str),
    ('auto_period_access', bool),
    ('remarks', str),
    ('date_edit', str),
    ('media_type', dict),
    ('approx_duration', str),
    ('file', str),
    ('url_file', str),
    ('timbre', str),
    ('timbre_ref', str),
    ('melody', str),
    ('domain', str),
    ('deposit_digest', str),
    ('deposit_names', str),
    ('deposit_places', str),
    ('deposit_periods', str),
    ('text_bool', bool),
    ('text', str),
    ('incipit', str),
    ('refrain', str),
    ('jingle', str),
    ('coupe', dict),
]

# Expected keys for MODEL objects
ITEM_FIELDS = sorted([item[0] for item in ITEM_STRUCTURE])


@pytest.mark.django_db
class TestItemList(CleanMediaMixin, APITestCase):
    """
    This class manage all Item tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)

        ItemFactory.reset_sequence()

        # Create a set of sample data
        RecordingContextFactory.create_batch(6)
        ItemCompleteFactory.create_batch(6)
        PerformanceCollectionMusicianFactory.create_batch(3)

    def test_can_get_item_list(self):
        """
        Ensure Item objects exists
        """
        url = reverse('item-list')

        # ORM side
        items = Item.objects.all()
        self.assertEqual(len(items), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(ITEM_STRUCTURE)
    def test_has_valid_item_values(self, attribute, attribute_type):
        """
        Ensure Item objects have valid values
        """

        url = reverse('item-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item.keys()), ITEM_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                try:
                    self.assertIsInstance(item[attribute], str)
                except AssertionError:
                    # Because of serializer.DurationField
                    self.assertIsInstance(item[attribute], type(None))
            else:
                self.assertIsInstance(item[attribute], attribute_type)
            if attribute not in ['url_file']:
                self.assertIsNot(item[attribute], '')

    def test_get_an_item(self):
        """
        Ensure we can get an Item objects
        using an existing id
        """

        item = Item.objects.first()
        url = reverse('item-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def _create_tmp_file(self):
        file_name = '/tmp/test_upload.txt'
        f = open(file_name, 'w')
        f.write('test123\n')
        f.close()
        f = open(file_name, 'r')
        return f

    def test_create_an_item(self):
        """
        Ensure we can create an Item object
        """

        # Create a fake file.
        fake_sound = create_tmp_sound("c'est déjà l'été")
        fake_url = 'https://api.nakala.fr/data/10.34847/nkl.a03a235m/f6e600e2c798959f9c4a6dafb9139f71b26ab5e9'

        # Tests data for fake file
        files_data = [
            ('', '', status.HTTP_400_BAD_REQUEST),
            (fake_sound, '', status.HTTP_201_CREATED),
            ('', fake_url, status.HTTP_201_CREATED),
            (fake_sound, fake_url, status.HTTP_400_BAD_REQUEST),
        ]

        i = 0
        for file_data in files_data :

            data = factory.build(
                dict,
                FACTORY_CLASS=ItemFactory)
            i = i + 1
            data['code'] = data['code'][0:-3] + str(500+i)

            collection = Collection.objects.first()
            # Write the Collection object in the item data object.
            data['collection'] = collection.id

            mediatype = MediaType.objects.first()
            # Write the MediaType object in the item data object.
            data['media_type'] = mediatype.id

            coupe = Coupe.objects.first()
            # Write the Coupe object in the item data object.
            data['coupe'] = coupe.id

            # Retrieve data for file
            (audio_file, data['url_file'], status_response) = file_data
            data['file'] = audio_file

            url = reverse('item-list')
            response = self.client.post(url, data, format='multipart')
            #ic(response.json())
            # Check only expected attributes returned
            self.assertEqual(response.status_code, status_response)
            if status_response == status.HTTP_201_CREATED :
                self.assertIsInstance(response.data, dict)
                self.assertEqual(
                    sorted(response.data.keys()),
                    ITEM_FIELDS)

                url = reverse(
                    'item-detail',
                    kwargs={'pk': response.data['id']}
                )
                response_get = self.client.get(url)

                self.assertEqual(response_get.status_code, status.HTTP_200_OK)
                self.assertIsInstance(response_get.data, dict)
                data_response = response_get.data
                if data_response['file'] != None :
                    assert "cest_deja_lete" in  data_response['file']

    def test_complete(self):
        item = Item.objects.first()
        url = reverse('item-complete', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(len(response.data["performances"]), 1)
        self.assertEqual(len(response.data["collectors"]), 2)
        self.assertEqual(len(response.data["informers"]), 3)
        self.assertEqual(len(response.data["authors"]), 1)
        self.assertEqual(len(response.data["compositors"]), 1)
        self.assertEqual(len(response.data["dances"]), 2)
        self.assertEqual(len(response.data["domain_musics"]), 2)
        self.assertEqual(len(response.data["domain_songs"]), 2)
        self.assertEqual(len(response.data["domain_tales"]), 2)
        self.assertEqual(len(response.data["domain_vocals"]), 2)
        self.assertEqual(len(response.data["musical_groups"]), 2)
        self.assertEqual(len(response.data["musical_organizations"]), 2)
        self.assertEqual(len(response.data["thematics"]), 2)
        self.assertEqual(len(response.data["usefulnesses"]), 2)
        self.assertEqual(len(response.data["coiraults"]), 2)
        self.assertEqual(len(response.data["lafortes"]), 2)


    def test_performances(self):
        item = Item.objects.first()
        url = reverse('item-performances', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(len(response.data["performances"]), 1)

    def test_siblings(self):
        item = Item.objects.first()
        url = '/api/item/' + str(item.id) + '/siblings'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data.keys(), set((
            'count', 'current_index',
            'first_id', 'previous_id', 'next_id', 'last_id',
        )))

    def test_update_an_item(self):
        """
        Ensure we can update an Item object
        """

        item = Item.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'item-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['title'] = 'foobar_test_put'
        data['collection'] = data['collection']['id']
        data['media_type'] = data['media_type']['id']
        data['coupe'] = data['coupe']['id']
        # Create a fake file.
        data['file'] = create_tmp_sound(data['code'])
        data['url_file'] = ''

        data['approx_duration'] = '00:20'

        url = reverse(
            'item-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='multipart')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEM_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_put')

    def test_patch_an_item(self):
        """
        Ensure we can patch an Item object
        """

        item = Item.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_patch')

        data = {
            'title': 'foobar_test_patch',
            'domain': 'TC'
            }
        url = reverse(
            'item-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='multipart')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEM_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_patch')

    def test_uniq_code_item(self):
        """
        Ensure we don't validate a non-uniq item code
        """

        item = Item.objects.first()
        code_1 = item.code
        item = Item.objects.last()

        data = {'code': code_1}
        url = reverse(
            'item-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='multipart')

        # Ensure code 409 returned
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_download_a_file(self, depends=['test_create_an_item'] ):
        """
        Ensure we can download a file of an item
        """
        item = Item.objects.first()

        url = reverse(
            'item-sound_download',
            kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_an_item(self):
        """
        Ensure we can delete an Item object
        """

        item = Item.objects.first()

        # Delete this object
        url = reverse(
            'item-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Item removed
        url_get = reverse(
            'item-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_get_by_code(self):
        """
        Ensure we can obtain an item with its code (via the API call)
        refer issue #203
        """

        item = Item.objects.first()
        code = item.code
        description = item.description

        response = self.client.get("http://nginx.francoralite.localhost:8080/api/item?code=" + code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

        self.assertEqual(response.data[0]['description'], description)
