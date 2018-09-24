# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ExtMediaItem tests
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

from .factories.ext_media_item import ExtMediaItemFactory
from .factories.media_item import MediaItemFactory
from ..models.ext_media_item import ExtMediaItem
from telemeta.models.item import MediaItem

# Expected structure for Ext_media_item objects
# FIXIT ----
EXTMEDIAITEM_STRUCTURE = [
    ('id', int),
    ('media_item', dict),
    ('mshs_alt_title', str),
    ('description', str),
    ('mshs_timbre', str),
    ('mshs_timbre_ref', str),
    ('mshs_timbre_code', str),
    ('mshs_melody', str),
    ('mshs_domain', str),
    ('mshs_domain_song', str),
    ('mshs_domain_vocal', str),
    ('mshs_domain_music', str),
    ('mshs_domain_tale', str),
    ('mshs_details', str),
    ('mshs_function', str),
    ('mshs_dance', str),
    ('mshs_dance_details', str),
    ('mshs_deposit_digest', str),
    ('mshs_deposit_thematic', str),
    ('mshs_deposit_names', str),
    ('mshs_deposit_places', str),
    ('mshs_deposit_periods', str),
    ('mshs_text_bool', bool),
    ('mshs_text', str),
    ('mshs_incipit', str),
    ('mshs_refrain', str),
    ('mshs_jingle', str),
    ('mshs_ch_coupe', str),
    ('mshs_title_ref_coirault', str),
    ('mshs_code_coirault', str),
    ('mshs_title_ref_laforte', str),
    ('mshs_code_laforte', str),
    ('mshs_title_ref_Dela', str),
    ('mshs_code_Dela', str),
    ('mshs_title_ref_Aare', str),
    ('mshs_code_Aare', str),
    ('mshs_musical_organization', str),
    ('mshs_group', str),
    ('code', str),
]

# Expected keys for MODEL objects
EXTMEDIAITEM_FIELDS = sorted([item[0] for item in EXTMEDIAITEM_STRUCTURE])


@pytest.mark.django_db
class TestExtMediaItemList(APITestCase):
    """
    This class manage all ExtMediaItem tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        call_command('telemeta-setup-enumerations')
        # Create a set of sample data
        MediaItemFactory.create_batch(6)

    def test_can_get_ext_media_item_list(self):
        """
        Ensure ExtMediaItem objects exists
        """
        url = reverse('MediaItem-list')
        # ORM side
        ext_media_items = ExtMediaItem.objects.all()
        self.assertEqual(len(ext_media_items), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(EXTMEDIAITEM_STRUCTURE)
    def test_has_valid_ext_media_item_values(self, attribute, attribute_type):
        """
        Ensure ExtMediaItem objects have valid values
        """

        url = reverse('extmediaitem-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for ext_media_item in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(ext_media_item.keys()), EXTMEDIAITEM_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        ext_media_item[attribute], basestring)
                else:
                    self.assertIsInstance(ext_media_item[attribute], str)
            else:
                self.assertIsInstance(
                    ext_media_item[attribute], attribute_type)
            self.assertIsNot(ext_media_item[attribute], '')

    def test_get_an_ext_media_item(self):
        """
        Ensure we can get an ExtMediaItem objects
        using an existing id
        """

        item = ExtMediaItem.objects.first()
        url = reverse('extmediaitem-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    # def test_create_an_ext_media_item(self):
    #     """
    #     Ensure we can create an ExtMediaItem object
    #     """
    #
    #     data = factory.build(
    #         dict,
    #         FACTORY_CLASS=ExtMediaItemFactory)
    #     data['media_item'] = str(data['media_item'].__dict__)
    #     data['mshs_ch_coupe'] = str(data['mshs_ch_coupe'])
    #     url = reverse('extmediaitem-list')
    #     response = self.client.post(url, data, format='json')
    #
    #     # Check only expected attributes returned
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertIsInstance(response.data, dict)
    #     self.assertEqual(
    #         sorted(response.data.keys()),
    #         EXTMEDIAITEM_FIELDS)
    #
    #     url = reverse(
    #         'extmediaitem-detail',
    #         kwargs={'pk': response.data['id']}
    #     )
    #     response_get = self.client.get(url)
    #
    #     self.assertEqual(response_get.status_code, status.HTTP_200_OK)
    #     self.assertIsInstance(response_get.data, dict)

    def test_update_an_ext_media_item(self):
        """
        Ensure we can update an ExtMediaItem object
        """

        item = ExtMediaItem.objects.first()
        self.assertNotEqual(item.description, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'extmediaitem-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['description'] = 'foobar_test_put'
        url = reverse(
            'extmediaitem-detail',
            kwargs={'pk': item.id})

        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            EXTMEDIAITEM_FIELDS)
        self.assertEqual(response.data['description'], 'foobar_test_put')

    def test_patch_an_ext_media_item(self):
        """
        Ensure we can patch an ExtMediaItem object
        """

        item = ExtMediaItem.objects.first()
        self.assertNotEqual(item.description, 'foobar_test_patch')

        data = {'description': 'foobar_test_patch'}
        url = reverse(
            'extmediaitem-detail',
            kwargs={'pk': item.id})

        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            EXTMEDIAITEM_FIELDS)
        self.assertEqual(response.data['description'], 'foobar_test_patch')

    def test_delete_an_ext_media_item(self):
        """
        Ensure we can delete an ExtMediaItem object
        """

        item = ExtMediaItem.objects.first()

        # Delete this object
        url = reverse(
            'extmediaitem-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ExtMediaItem removed
        url_get = reverse(
            'extmediaitem-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
