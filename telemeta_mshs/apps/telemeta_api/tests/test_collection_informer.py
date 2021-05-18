# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Collection_informer tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.collection_informer import CollectionInformerFactory
from ..models.collection_informer import CollectionInformer
from ..models.authority import Authority
from ..models.collection import Collection

from .keycloak import get_token

# Expected structure for Collection_informer objects
COLLECTIONINFORMER_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('informer', dict),
]

# Expected keys for MODEL objects
COLLECTIONINFORMER_FIELDS = sorted(
    [item[0] for item in COLLECTIONINFORMER_STRUCTURE])


@pytest.mark.django_db
class TestCollectionInformerList(APITestCase):
    """
    This class manage all CollectionInformer tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])


        # Create a set of sample data
        CollectionInformerFactory.create_batch(1)

    def test_can_get_collection_informer_list(self):
        """
        Ensure CollectionInformer objects exists
        """

        url = reverse('collectioninformer-list', kwargs={
            'collection_pk': 1})

        # ORM side
        collection_informers = CollectionInformer.objects.all()
        self.assertEqual(len(collection_informers), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(COLLECTIONINFORMER_STRUCTURE)
    def test_has_valid_collection_informer_values(self,
                                                  attribute, attribute_type):
        """
        Ensure CollectionInformer objects have valid values
        """

        url = reverse('collectioninformer-list', kwargs={
            'collection_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for collection_informer in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(collection_informer.keys()), COLLECTIONINFORMER_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(collection_informer[attribute], str)
            else:
                self.assertIsInstance(
                    collection_informer[attribute], attribute_type)
            self.assertIsNot(collection_informer[attribute], '')

    def test_get_a_collection_informer(self):
        """
        Ensure we can get an CollectionInformer objects
        using an existing id
        """

        item = CollectionInformer.objects.first()
        url = reverse('collectioninformer-detail', kwargs={
                      'collection_pk': item.collection.id,
                      'pk': item.informer.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_collection_informer(self):
        """
        Ensure we can create a CollectionInformer object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=CollectionInformerFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.-
        data['informer'] = Authority.objects.first().id
        data['collection'] = Collection.objects.first().id

        url = reverse('collectioninformer-list', kwargs={
            'collection_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            COLLECTIONINFORMER_FIELDS)

        url = reverse(
            'collectioninformer-detail',
            kwargs={'collection_pk': response.data['collection']['id'],
                    'pk': response.data['informer']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_a_collection_informer(self):
        """
        Ensure we can delete a CollectionInformer object
        """

        item = CollectionInformer.objects.first()

        # Delete this object
        url = reverse(
            'collectioninformer-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.informer.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure CollectionInformer removed
        url_get = reverse(
            'collectioninformer-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.informer.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
