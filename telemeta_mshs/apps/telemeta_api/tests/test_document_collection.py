# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
DocumentCollection tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.document_collection import DocumentCollectionFactory
from ..models.document_collection import DocumentCollection
from ..models.document import Document
from ..models.collection import Collection

from .keycloak import get_token

# Expected structure for Document_collection objects
DOCUMENTCOLLECTION_STRUCTURE = [
    ('id', int),
    ('id_nakala', str),
    ('title', str),
    ('description', str),
    ('credits', str),
    ('date', str),
    ('collection', dict),
]

# Expected keys for MODEL objects
DOCUMENTCOLLECTION_FIELDS = sorted(
    [item[0] for item in DOCUMENTCOLLECTION_STRUCTURE])


@pytest.mark.django_db
class TestDocumentCollectionList(APITestCase):
    """
    This class manage all DocumentCollection tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        self.url = "/api/collection/1/document"
        self.url_detail =  self.url + "/1"

        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        DocumentCollectionFactory.create_batch(1)

    def test_can_get_document_collection_list(self):
        """
        Ensure DocumentCollection objects exists
        """

        # ORM side
        document_collections = DocumentCollection.objects.all()
        self.assertEqual(len(document_collections), 1)

        # API side
        response = self.client.get(self.url)


        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(DOCUMENTCOLLECTION_STRUCTURE)
    def test_has_valid_document_collection_values(self, attribute, attribute_type):
        """
        Ensure DocumentCollection objects have valid values
        """

        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for document_collection in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(document_collection.keys()), DOCUMENTCOLLECTION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(document_collection[attribute], str)
            else:
                self.assertIsInstance(document_collection[attribute], attribute_type)
            self.assertIsNot(document_collection[attribute], '')

    def test_get_an_document_collection(self):
        """
        Ensure we can get an DocumentCollection objects
        using an existing id
        """

        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_document_collection(self):
        """
        Ensure we can create an DocumentCollection object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=DocumentCollectionFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['document'] = Document.objects.first().id
        data['collection'] = Collection.objects.first().id

        response = self.client.post(self.url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOCUMENTCOLLECTION_FIELDS)
        self.assertEqual(response.data["id"], 2)

        response_get = self.client.get(self.url + "/2")

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_document_collection(self):
        """
        Ensure we can delete an DocumentCollection object
        """

        # Delete this object
        response = self.client.delete(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure DocumentCollection removed
        # FIXIT  kwargs for the related tables
        response_get = self.client.get(self.url_detail)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
