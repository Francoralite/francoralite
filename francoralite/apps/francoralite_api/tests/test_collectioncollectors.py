"""
CollectionCollectors tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.collectioncollectors import CollectionCollectorsFactory
from ..models.collectioncollectors import CollectionCollectors
from ..models.authority import Authority
from ..models.collection import Collection

from .keycloak import get_token

# Expected structure for Coupe objects
COLLECTORS_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('collector', dict),
]

# Expected keys for Coupe objects
COLLECTORS_FIELDS = sorted([item[0] for item in COLLECTORS_STRUCTURE])


@pytest.mark.django_db
class TestCollectionCollectorsList(APITestCase):
    """
    This class manage all CollectionCollectors tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])


        CollectionCollectorsFactory.create_batch(6)

    def test_can_get_collectioncollectors_list(self):
        """
        Ensure CollectionCollectors objects exists
        """
        url = reverse('collectioncollectors-list', kwargs={
            'collection_pk': 1})

        # ORM side
        collectionscollectors = CollectionCollectors.objects.all()
        self.assertEqual(len(collectionscollectors), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(COLLECTORS_STRUCTURE)
    def test_has_valid_collectioncollectors_values(self,
                                                   attribute, attribute_type):
        """
        Ensure CollectionCollectors objects have valid values
        """

        url = reverse('collectioncollectors-list', kwargs={
            'collection_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for collectors in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(collectors.keys()), COLLECTORS_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(collectors[attribute], str)
            else:
                self.assertIsInstance(collectors[attribute], attribute_type)
            self.assertIsNot(collectors[attribute], '')

    def test_get_a_collectioncollectors(self):
        """
        Ensure we can get a CollectionCollectors objects using an existing id
        """

        item = CollectionCollectors.objects.first()
        url = reverse('collectioncollectors-detail', kwargs={
            'collection_pk': item.collection.id,
            'pk': item.collector.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_collectioncollectors(self):
        """
        Ensure we can create a CollectionCollectors object
        """

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data = factory.build(dict, FACTORY_CLASS=CollectionCollectorsFactory)

        data['collector'] = Authority.objects.last().id
        data['collection'] = Collection.objects.first().id

        url = reverse('collectioncollectors-list', kwargs={
            'collection_pk': data['collection']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), COLLECTORS_FIELDS)

        url = reverse(
            'collectioncollectors-detail',
            kwargs={'collection_pk': response.data['collection']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_collectioncollectors(self):
        """
        Ensure we can delete an CollectionCollectors object
        """

        item = CollectionCollectors.objects.first()

        # Delete this object
        url = reverse('collectioncollectors-detail', kwargs={
            'collection_pk': item.collection.id,
            'pk': item.collector.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure CollectionCollectors removed
        url_get = reverse('collectioncollectors-detail', kwargs={
            'collection_pk': item.collection.id,
            'pk': item.collector.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
