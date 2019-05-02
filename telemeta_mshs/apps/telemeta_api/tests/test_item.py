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
import sys
import os
import settings
from types import NoneType

from telemeta.cache import TelemetaCache

from django.forms.models import model_to_dict
from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item import ItemFactory
from ..models.item import Item
from ..models.collection import Collection
from ..models.mediatype import MediaType
from ..models.coupe import Coupe
from .fake_data.fake_sound import create_tmp_sound

# Expected structure for Item objects
# FIXIT ----
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
class TestItemList(APITestCase):
    """
    This class manage all Item tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        ItemFactory.create_batch(6)

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
                if sys.version_info.major == 2:
                    try:
                        self.assertIsInstance(item[attribute], basestring)
                    except AssertionError:
                        # Because of serializer.DurationField
                        self.assertIsInstance(item[attribute], NoneType)
                else:
                    try:
                        self.assertIsInstance(item[attribute], str)
                    except AssertionError:
                        # Because of serializer.DurationField
                        self.assertIsInstance(item[attribute], NoneType)
            else:
                self.assertIsInstance(item[attribute], attribute_type)
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

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemFactory)

        collection = Collection.objects.first()
        # Write the Collection object in the item data object.
        data['collection'] = collection.id

        mediatype = MediaType.objects.first()
        # Write the MediaType object in the item data object.
        data['media_type'] = mediatype.id

        coupe = Coupe.objects.first()
        # Write the Coupe object in the item data object.
        data['coupe'] = coupe.id

        # Create a fake file.
        data['file'] = create_tmp_sound()

        url = reverse('item-list')
        response = self.client.post(url, data, format='multipart')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
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
        item = response.data

        # Item Analysis ----------------------------------
        # Test if related ItemAnalyzis are presents
        url = reverse('itemanalysis-list', kwargs={
            'item_pk': item['id']})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        # Number of analysis per item
        self.assertEqual(len(response.data), 12)
        for data_analysis in response.data:
            # number of feature per analysis
            self.assertEqual(len(data_analysis), 7)

        # Transcoding ------------------------------------
        # Test if related ItemTrancodingFlags are presents
        url = reverse('itemtranscodingflag-list', kwargs={
            'item_pk':  item['id']})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        for transcoding_flag in response.data:
            # number of feature per transcoding_flag
            self.assertEqual(len(transcoding_flag), 5)

        # Grapher ----------------------------------------
        default_grapher_id = getattr(
             settings, 'TIMESIDE_DEFAULT_GRAPHER_ID', ('waveform_centroid'))
        MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
        CACHE_DIR = os.path.join(MEDIA_ROOT, 'cache')
        cache_data = TelemetaCache(
            getattr(settings, 'TELEMETA_DATA_CACHE_DIR', CACHE_DIR))
        list_file = os.listdir(cache_data.dir)
        self.assertEqual(
            item['code'] + '.' + default_grapher_id +
            '.346_130.png' in list_file, True)

    def test_update_an_item(self):
        """
        Ensure we can update an Item object
        """

        # item = Item.objects.last()
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
        data['file'] = create_tmp_sound()

        response = self.client.get(
            '/api/timeside/' + data['code'] + '/analyze/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
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

        data = {'title': 'foobar_test_patch'}
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

    def test_timeside_analyze(self):
        """
        Ensure we can retrieve analysis data of an item's sound
        """

        # Retrieve a valid item's code
        item = Item.objects.first()

        # Retrieve some analysis data
        # FIXIT ------------------------
        duration = str(item.approx_duration)

        # The code is right --> there is some data
        response = self.client.get('/api/timeside/' +
                                   str(item.id) + '/analyze/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['duration'], duration)

        # The code is wrong/not-present --> there is no data
        response = self.client.get('/api/timeside/0/analyze/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_timeside_visualize(self):
        """
        Test if the spectrogram's image exists
        """

        # Retrieve a valid item's code
        item = Item.objects.first()
        id = str(item.id)
        code = str(item.code)

        # Call to the visualize endpoint
        response = self.client.get('/api/timeside/' + id + '/visualize/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data

        # Grapher ----------------------------------------
        default_grapher_id = data['grapher']

        MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
        CACHE_DIR = os.path.join(MEDIA_ROOT, 'cache')
        cache_data = TelemetaCache(
            getattr(settings, 'TELEMETA_DATA_CACHE_DIR', CACHE_DIR))
        list_file = os.listdir(cache_data.dir)

        # Test if the file exists
        self.assertEqual(
            code + '.' + default_grapher_id +
            '.' + str(data['width']) + '_' +
            str(data['height']) + '.png' in list_file, True)
