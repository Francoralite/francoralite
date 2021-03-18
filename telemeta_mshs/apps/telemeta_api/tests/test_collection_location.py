# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
CollectionLocation tests
"""

import factory
import pytest
import sys
import random

from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.collection_location import CollectionLocationFactory
from ..models.collection_location import CollectionLocation
from ..models.location import Location
from ..models.collection import Collection

from .keycloak import get_token

# Expected structure for Collection_location objects
COLLECTIONLOCATION_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('location', dict),
]

# Expected keys for MODEL objects
COLLECTIONLOCATION_FIELDS = sorted(
    [item[0] for item in COLLECTIONLOCATION_STRUCTURE])


@pytest.mark.django_db
class TestCollectionLocationList(APITestCase):
    """
    This class manage all CollectionLocation tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])


        # Create a set of sample data
        CollectionLocationFactory.create_batch(1)

    def test_can_get_collection_location_list(self):
        """
        Ensure CollectionLocation objects exists
        """

        url = reverse('collectionlocation-list', kwargs={
            'collection_pk': 1})

        # ORM side
        collection_locations = CollectionLocation.objects.all()
        self.assertEqual(len(collection_locations), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(COLLECTIONLOCATION_STRUCTURE)
    def test_has_valid_collection_location_values(self,
                                                  attribute, attribute_type):
        """
        Ensure CollectionLocation objects have valid values
        """

        url = reverse('collectionlocation-list', kwargs={
            'collection_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for collection_location in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(collection_location.keys()), COLLECTIONLOCATION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        collection_location[attribute], basestring)
                else:
                    self.assertIsInstance(collection_location[attribute], str)
            else:
                self.assertIsInstance(
                    collection_location[attribute], attribute_type)
            self.assertIsNot(collection_location[attribute], '')

    def test_get_a_collection_location(self):
        """
        Ensure we can get a CollectionLocation objects
        using an existing id
        """

        item = CollectionLocation.objects.first()
        url = reverse('collectionlocation-detail', kwargs={
                      'collection_pk': item.collection.id,
                      'pk': item.location.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_collection_location(self):
        """
        Ensure we can create a CollectionLocation object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=CollectionLocationFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['location'] = Location.objects.first().id
        data['collection'] = Collection.objects.first().id

        url = reverse('collectionlocation-list', kwargs={
            'collection_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            COLLECTIONLOCATION_FIELDS)

        url = reverse(
            'collectionlocation-detail',
            kwargs={'collection_pk': response.data['collection']['id'],
                    'pk': response.data['location']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_a_collection_location(self):
        """
        Ensure we can delete a CollectionLocation object
        """

        item = CollectionLocation.objects.first()

        # Delete this object
        url = reverse(
            'collectionlocation-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.location.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure CollectionLocation removed
        url_get = reverse(
            'collectionlocation-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.location.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
