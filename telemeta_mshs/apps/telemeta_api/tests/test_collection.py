# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

"""
Collection tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase


from .factories.collection import CollectionFactory
from ..models.collection import Collection
from ..models.mission import Mission
from ..models.mediatype import MediaType
from ..models.legal_rights import LegalRights

from .keycloak import get_token

# Expected structure for collection objects
COLLECTION_STRUCTURE = [
    ('id', int),
    ('mission', dict),
    ('title', str),
    ('alt_title', str),
    ('description', str),
    ('recording_context', str),
    ('recorded_from_year', str),
    ('recorded_to_year', str),
    ('year_published', int),
    ('legal_rights', dict),
    ('location_details', str),
    ('cultural_area', str),
    ('language', str),
    ('publisher_collection', str),
    ('booklet_author', str),
    ('metadata_author', str),
    ('code', str),
    ('code_partner', str),
    ('booklet_description', str),
    ('comment', str),
    ('media_type', dict),
    ('physical_items_num', int),
    ('auto_period_access', bool)
]

# Expected keys for MODEL objects
COLLECTION_FIELDS = sorted(
    [item[0] for item in COLLECTION_STRUCTURE])


@pytest.mark.django_db
class TestCollectionList(APITestCase):
    """
    This class manage all Mediacollection tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])


        CollectionFactory.create_batch(6)

    def test_can_get_collection_list(self):
        """
        Ensure collection objects exists
        """
        url = reverse('collection-list')

        # ORM side
        collections = Collection.objects.all()
        self.assertEqual(len(collections), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(COLLECTION_STRUCTURE)
    def test_has_valid_collection_values(self, attribute, attribute_type):
        """
        Ensure collection objects have valid values
        """

        url = reverse('collection-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for collection in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(collection.keys()), COLLECTION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        collection[attribute], basestring)
                else:
                    self.assertIsInstance(collection[attribute], str)
            else:
                self.assertIsInstance(
                    collection[attribute], attribute_type)
            self.assertIsNot(collection[attribute], '')

    def test_get_an_collection(self):
        """
        Ensure we can get a collection objects
        using an existing id
        """

        item = Collection.objects.first()
        url = reverse('collection-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_collection(self):
        """
        Ensure we can create an collection object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=CollectionFactory)

        mission = Mission.objects.first()
        # Write the Mission object in the collection data object.
        data['mission'] = mission.id

        mediatype = MediaType.objects.first()
        # Write the MediaType object in the collection data object.
        data['media_type'] = mediatype.id

        legalrights = LegalRights.objects.first()
        # Write the MediaType object in the collection data object.
        data['legal_rights'] = legalrights.id

        # related objects
        data['recorded_from_year'] = str(data['recorded_from_year'])
        data['recorded_to_year'] = str(data['recorded_to_year'])
        data['recording_context'] = str(data['recording_context'])
        # data['legal_rights'] = str(data['legal_rights'])
        # data['metadata_author'] = str(data['metadata_author'])
        # data['publishing_status'] = str(data['publishing_status'])
        # data['status'] = str(data['status'])
        # data['metadata_writer'] = str(data['metadata_writer'])
        # data['media_type'] = str(data['media_type'])

        url = reverse('collection-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            COLLECTION_FIELDS)

        url = reverse(
            'collection-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_a_collection(self):
        """
        Ensure we can update a collection object
        """

        item = Collection.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'collection-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['title'] = 'foobar_test_put'
        url = reverse(
            'collection-detail',
            kwargs={'pk': item.id})
        data['mission'] = data['mission']['id']
        data['media_type'] = data['media_type']['id']
        data['legal_rights'] = data['legal_rights']['id']
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            COLLECTION_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_put')

    def test_patch_a_collection(self):
        """
        Ensure we can patch a collection object
        """

        item = Collection.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_patch')

        data = {'title': 'foobar_test_patch'}
        url = reverse(
            'collection-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            COLLECTION_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_patch')

    def test_delete_a_collection(self):
        """
        Ensure we can delete a collection object
        """

        item = Collection.objects.first()

        # Delete this object
        url = reverse(
            'collection-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Mediacollection removed
        url_get = reverse(
            'collection-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
