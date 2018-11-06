"""
Coupe tests
"""

import factory
import pytest
import sys

# from django.forms.models import model_to_dict
from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.collectioncollectors import CollectionCollectorsFactory
from ..models.collectioncollectors import CollectionCollectors
from ..models.authority import Authority
from ..models.collection import Collection

# Expected structure for Coupe objects
COLLECTORS_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('collector', dict),
]

# Expected keys for Coupe objects
COLLECTORS_FIELDS = sorted([item[0] for item in COLLECTORS_STRUCTURE])


@pytest.mark.django_db
class TestCollectionCokkecrosList(APITestCase):
    """
    This class manage all CollectionCollectors tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

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
        self.assertEqual(len(response.data), 6)

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
                if sys.version_info.major == 2:
                    self.assertIsInstance(collectors[attribute], basestring)
                else:
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

        data['collector'] = Authority.objects.first()
        data['collection'] = Collection.objects.first()
        data['collector'] = data['collector'].__dict__['_original_state']
        data['collection'] = data['collection'].__dict__['_original_state']
        data['collection']['code'] = 'code1500'
        url = reverse('collectioncollectors-list', kwargs={
            'collection_pk': 1})
        response = self.client.post(url, data, format='json')
        print(response)

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), COLLECTORS_FIELDS)

        url = reverse(
            'collectioncollectors-detail',
            kwargs={'collection_pk': response.data['collection']['id'],
                    'pk': response.data['collector']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    # def test_update_an_collectioncollectors(self):
    #     """
    #     Ensure we can update an CollectionCollectors object
    #     """
    #
    #     item = CollectionCollectors.objects.first()
    #     self.assertNotEqual(item.value, 'foobar_test_put')
    #
    #     # Get existing object from API
    #     url_get = reverse('coupe-detail', kwargs={'pk': item.id})
    #     data = self.client.get(url_get).data
    #
    #     data['value'] = 'foobar_test_put'
    #     url = reverse('coupe-detail', kwargs={'pk': item.id})
    #     response = self.client.put(url, data, format='json')
    #
    #     # Ensure new value returned
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIsInstance(response.data, dict)
    #     self.assertEqual(sorted(response.data.keys()), COLLECTORS_FIELDS)
    #     self.assertEqual(response.data['value'], 'foobar_test_put')

    # def test_patch_an_coupe(self):
    #     """
    #     Ensure we can patch an Coupe object
    #     """
    #
    #     item = Coupe.objects.first()
    #     self.assertNotEqual(item.value, 'foobar_test_patch')
    #
    #     data = {'value': 'foobar_test_patch'}
    #     url = reverse('coupe-detail', kwargs={'pk': item.id})
    #     response = self.client.patch(url, data, format='json')
    #
    #     # Ensure new value returned
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIsInstance(response.data, dict)
    #     self.assertEqual(sorted(response.data.keys()), INSTITUTION_FIELDS)
    #     self.assertEqual(response.data['value'], 'foobar_test_patch')
    #
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
