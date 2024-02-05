# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
CollectionCulturalArea tests
"""

import factory
import pytest
import sys
import random

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.collection_cultural_area import CollectionCulturalAreaFactory
from ..models.collection_cultural_area import CollectionCulturalArea
from ..models.cultural_area import CulturalArea
from ..models.collection import Collection

from .keycloak import get_token

# Expected structure for Collection_cultural_area objects
COLLECTION_CULTURAL_AREA_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('cultural_area', dict),
]

# Expected keys for MODEL objects
COLLECTION_CULTURAL_AREA_FIELDS = sorted(
    [item[0] for item in COLLECTION_CULTURAL_AREA_STRUCTURE])


@pytest.mark.django_db
class TestCollectionCulturalAreaList(APITestCase):
    """
    This class manage all CollectionCulturalArea tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)

        # Create a set of sample data
        CollectionCulturalAreaFactory.create_batch(6)

    def test_can_get_collection_cultural_area_list(self):
        """
        Ensure CollectionCulturalArea objects exists
        """

        url = reverse('collectionculturalarea-list', kwargs={
            'collection_pk': 1})

        # ORM side
        collection_cultural_areas = CollectionCulturalArea.objects.all()
        self.assertEqual(len(collection_cultural_areas), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(COLLECTION_CULTURAL_AREA_STRUCTURE)
    def test_has_valid_collection_cultural_area_values(self,
                                                  attribute, attribute_type):
        """
        Ensure CollectionCulturalArea objects have valid values
        """

        url = reverse('collectionculturalarea-list', kwargs={
            'collection_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for collection_cultural_area in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(collection_cultural_area.keys()), COLLECTION_CULTURAL_AREA_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(collection_cultural_area[attribute], str)
            else:
                self.assertIsInstance(
                    collection_cultural_area[attribute], attribute_type)
            self.assertIsNot(collection_cultural_area[attribute], '')

    def test_get_a_collection_cultural_area(self):
        """
        Ensure we can get a CollectionCulturalArea objects
        using an existing id
        """

        item = CollectionCulturalArea.objects.first()
        url = reverse('collectionculturalarea-detail', kwargs={
                      'collection_pk': item.collection.id,
                      'pk': item.cultural_area.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_collection_cultural_area(self):
        """
        Ensure we can create a CollectionCulturalArea object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=CollectionCulturalAreaFactory)

        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.
        data['cultural_area'] = 2
        data['collection'] = 1

        url = reverse('collectionculturalarea-list', kwargs={
            'collection_pk': data['collection']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            COLLECTION_CULTURAL_AREA_FIELDS)

        url = reverse(
            'collectionculturalarea-detail',
            kwargs={'collection_pk': response.data['collection']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_a_collection_cultural_area(self):
        """
        Ensure we can delete a CollectionCulturalArea object
        """

        item = CollectionCulturalArea.objects.first()

        # Delete this object
        url = reverse(
            'collectionculturalarea-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.cultural_area.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure CollectionCulturalArea removed
        url_get = reverse(
            'collectionculturalarea-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.cultural_area.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
