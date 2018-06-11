# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

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


from .factories.MediaCollection import MediacollectionFactory
from telemeta.models.collection import MediaCollection as Mediacollection


# Expected structure for Mediacollection objects
# FIXIT ----
MEDIACOLLECTION_STRUCTURE = [
    ('id', int),
    ('title', str),
    ('alt_title', str),
    ('creator', str),
    ('description', str),
    ('recording_context', str),
    ('recorded_from_year', int),
    ('recorded_to_year', int),
    ('year_published', int),
    ('public_access', str),
    ('collector', str),
    ('publisher', str),
    ('publisher_collection', str),
    ('publisher_serial', str),
    ('booklet_author', str),
    ('reference', str),
    ('external_references', str),
    ('auto_period_access', bool),
    ('legal_rights', str),
    ('code', str),
    ('old_code', str),
    ('acquisition_mode', str),
    ('cnrs_contributor', str),
    ('copy_type', str),
    ('metadata_author', str),
    ('booklet_description', str),
    ('publishing_status', str),
    ('status', str),
    ('alt_copies', str),
    ('comment', str),
    ('metadata_writer', str),
    ('archiver_notes', str),
    ('items_done', str),
    ('collector_is_creator', bool),
    ('is_published', bool),
    ('conservation_site', str),
    ('media_type', str),
    ('approx_duration', str),
    ('physical_items_num', int),
    ('original_format', str),
    ('physical_format', str),
    ('ad_conversion', str),
    ('alt_ids', str),
    ('travail', str)
]

# Expected keys for MODEL objects
MEDIACOLLECTION_FIELDS = sorted(
    [item[0] for item in MEDIACOLLECTION_STRUCTURE])


@pytest.mark.django_db
class TestMediacollectionList(APITestCase):
    """
    This class manage all Mediacollection tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        MediacollectionFactory.create_batch(6)

    def test_can_get_MediaCollection_list(self):
        """
        Ensure Mediacollection objects exists
        """
        url = reverse('MediaCollection-list')

        # ORM side
        MediaCollections = Mediacollection.objects.all()
        self.assertEqual(len(MediaCollections), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(MEDIACOLLECTION_STRUCTURE)
    def test_has_valid_MediaCollection_values(self, attribute, attribute_type):
        """
        Ensure Mediacollection objects have valid values
        """

        url = reverse('MediaCollection-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for MediaCollection in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(MediaCollection.keys()), MEDIACOLLECTION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        MediaCollection[attribute], basestring)
                else:
                    self.assertIsInstance(MediaCollection[attribute], str)
            else:
                self.assertIsInstance(
                    MediaCollection[attribute], attribute_type)
            self.assertIsNot(MediaCollection[attribute], '')

    def test_get_an_MediaCollection(self):
        """
        Ensure we can get an Mediacollection objects
        using an existing id
        """

        item = Mediacollection.objects.first()
        url = reverse('MediaCollection-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_MediaCollection(self):
        """
        Ensure we can create an Mediacollection object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=MediacollectionFactory)

        # related objects
        data['recording_context'] = str(data['recording_context'])
        data['publisher'] = str(data['publisher'])
        data['publisher_collection'] = str(data['publisher_collection'])
        data['legal_rights'] = str(data['legal_rights'])
        data['acquisition_mode'] = str(data['acquisition_mode'])
        data['copy_type'] = str(data['copy_type'])
        data['metadata_author'] = str(data['metadata_author'])
        data['publishing_status'] = str(data['publishing_status'])
        data['status'] = str(data['status'])
        data['metadata_writer'] = str(data['metadata_writer'])
        data['media_type'] = str(data['media_type'])
        data['original_format'] = str(data['original_format'])
        data['physical_format'] = str(data['physical_format'])
        data['ad_conversion'] = str(data['ad_conversion'])

        url = reverse('MediaCollection-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MEDIACOLLECTION_FIELDS)

        url = reverse(
            'MediaCollection-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

        item = Mediacollection.objects.first()
        self.assertEqual(item.id, 1)

    def test_update_an_MediaCollection(self):
        """
        Ensure we can update an Mediacollection object
        """

        item = Mediacollection.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'MediaCollection-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['title'] = 'foobar_test_put'
        url = reverse(
            'MediaCollection-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MEDIACOLLECTION_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_put')

    def test_patch_an_MediaCollection(self):
        """
        Ensure we can patch an Mediacollection object
        """

        item = Mediacollection.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_patch')

        data = {'title': 'foobar_test_patch'}
        url = reverse(
            'MediaCollection-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MEDIACOLLECTION_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_patch')

    def test_delete_an_MediaCollection(self):
        """
        Ensure we can delete an Mediacollection object
        """

        item = Mediacollection.objects.first()

        # Delete this object
        url = reverse(
            'MediaCollection-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Mediacollection removed
        url_get = reverse(
            'MediaCollection-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
