# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Document Item tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.document_item import DocumentItemFactory
from ..models.document_item import DocumentItem
from ..models.document import Document
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Document_item objects
DOCUMENTITEM_STRUCTURE = [
    ('id', int),
    ('id_nakala', str),
    ('title', str),
    ('description', str),
    ('credits', str),
    ('date', str),
    ('item', dict),
]

# Expected keys for MODEL objects
DOCUMENTITEM_FIELDS = sorted(
    [item[0] for item in DOCUMENTITEM_STRUCTURE])


@pytest.mark.django_db
class TestDocumentItemList(APITestCase):
    """
    This class manage all DocumentItem tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        self.url = "/api/item/1/document"
        self.url_detail =  self.url + "/1"

        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        DocumentItemFactory.create_batch(1)

    def test_can_get_document_item_list(self):
        """
        Ensure DocumentItem objects exists
        """

        # ORM side
        document_items = DocumentItem.objects.all()
        self.assertEqual(len(document_items), 1)

        # API side
        response = self.client.get(self.url)


        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(DOCUMENTITEM_STRUCTURE)
    def test_has_valid_document_item_values(self, attribute, attribute_type):
        """
        Ensure DocumentItem objects have valid values
        """

        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for document_item in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(document_item.keys()), DOCUMENTITEM_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(document_item[attribute], str)
            else:
                self.assertIsInstance(document_item[attribute], attribute_type)
            self.assertIsNot(document_item[attribute], '')

    def test_get_an_document_item(self):
        """
        Ensure we can get an DocumentItem objects
        using an existing id
        """

        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_document_item(self):
        """
        Ensure we can create an DocumentItem object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=DocumentItemFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['document'] = Document.objects.first().id
        data['item'] = Item.objects.first().id

        response = self.client.post(self.url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOCUMENTITEM_FIELDS)
        self.assertEqual(response.data["id"], 2)

        response_get = self.client.get(self.url + "/2")

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_document_item(self):
        """
        Ensure we can delete an DocumentItem object
        """

        # Delete this object
        response = self.client.delete(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure DocumentItem removed
        response_get = self.client.get(self.url_detail)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
