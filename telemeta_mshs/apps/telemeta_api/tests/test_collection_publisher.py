# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

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

from .factories.collection_publisher import CollectionPublisherFactory
from ..models.collection_publisher import CollectionPublisher
from ..models.authority import Authority
from ..models.collection import Collection

# Expected structure for Collection_publisher objects
COLLECTIONPUBLISHER_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('publisher', dict),
]

# Expected keys for MODEL objects
COLLECTIONPUBLISHER_FIELDS = sorted(
    [item[0] for item in COLLECTIONPUBLISHER_STRUCTURE])


@pytest.mark.django_db
class TestCollectionPublisherList(APITestCase):
    """
    This class manage all CollectionPublisher tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        CollectionPublisherFactory.create_batch(6)

    def test_can_get_collection_publisher_list(self):
        """
        Ensure CollectionPublisher objects exists
        """

        url = reverse('collectionpublisher-list', kwargs={
            'collection_pk': 1})

        # ORM side
        collection_publishers = CollectionPublisher.objects.all()
        self.assertEqual(len(collection_publishers), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(COLLECTIONPUBLISHER_STRUCTURE)
    def test_has_valid_collection_publisher_values(self,
                                                   attribute, attribute_type):
        """
        Ensure CollectionPublisher objects have valid values
        """

        url = reverse('collectionpublisher-list', kwargs={
            'collection_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for collection_publisher in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(collection_publisher.keys()),
                COLLECTIONPUBLISHER_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        collection_publisher[attribute], basestring)
                else:
                    self.assertIsInstance(collection_publisher[attribute], str)
            else:
                self.assertIsInstance(
                    collection_publisher[attribute], attribute_type)
            self.assertIsNot(collection_publisher[attribute], '')

    def test_get_an_collection_publisher(self):
        """
        Ensure we can get an CollectionPublisher objects
        using an existing id
        """

        item = CollectionPublisher.objects.first()
        url = reverse('collectionpublisher-detail', kwargs={
                      'collection_pk': item.collection.id,
                      'pk': item.publisher.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_collection_publisher(self):
        """
        Ensure we can create an CollectionPublisher object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=CollectionPublisherFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['publisher'] = Authority.objects.first()
        data['collection'] = Collection.objects.first()
        data['collection'] = data['collection'].__dict__['_original_state']
        data['publisher'] = data['publisher'].__dict__['_original_state']
        data['collection']['code'] = 'code1500'

        url = reverse('collectionpublisher-list', kwargs={
            'collection_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            COLLECTIONPUBLISHER_FIELDS)

        url = reverse(
            'collectionpublisher-detail',
            kwargs={'collection_pk': response.data['collection']['id'],
                    'pk': response.data['publisher']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_collection_publisher(self):
        """
        Ensure we can delete an CollectionPublisher object
        """

        item = CollectionPublisher.objects.first()

        # Delete this object
        url = reverse(
            'collectionpublisher-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.publisher.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure CollectionPublisher removed
        url_get = reverse(
            'collectionpublisher-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.publisher.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)