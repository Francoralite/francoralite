# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item-Authors tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_author import ItemAuthorFactory
from .fake_data.fake_sound import CleanMediaMixin
from ..models.item_author import ItemAuthor
from ..models.authority import Authority
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_author objects
ITEMAUTHOR_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('author', dict),
]

# Expected keys for MODEL objects
ITEMAUTHOR_FIELDS = sorted(
    [item[0] for item in ITEMAUTHOR_STRUCTURE])


@pytest.mark.django_db
class TestItemAuthorList(CleanMediaMixin, APITestCase):
    """
    This class manage all ItemAuthor tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        
        # Create a set of sample data
        ItemAuthorFactory.create_batch(6)

    def test_can_get_item_author_list(self):
        """
        Ensure ItemAuthor objects exists
        """
        # kwargs for the related tables
        url = reverse('itemauthor-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_authors = ItemAuthor.objects.all()
        self.assertEqual(len(item_authors), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMAUTHOR_STRUCTURE)
    def test_has_valid_item_author_values(self, attribute, attribute_type):
        """
        Ensure ItemAuthor objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemauthor-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_author in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_author.keys()), ITEMAUTHOR_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_author[attribute], str)
            else:
                self.assertIsInstance(item_author[attribute], attribute_type)
            self.assertIsNot(item_author[attribute], '')

    def test_get_an_item_author(self):
        """
        Ensure we can get an ItemAuthor objects
        using an existing id
        """

        item = ItemAuthor.objects.first()

        url = reverse('itemauthor-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.author.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_author(self):
        """
        Ensure we can create an ItemAuthor object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemAuthorFactory)

        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.
        data['item'] = 1
        data['author'] = 2

        url = reverse('itemauthor-list', kwargs={
            'item_pk': data['item']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMAUTHOR_FIELDS)

        url = reverse(
            'itemauthor-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_author(self):
        """
        Ensure we can delete an ItemAuthor object
        """

        item = ItemAuthor.objects.first()

        # Delete this object
        url = reverse(
            'itemauthor-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.author.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemAuthor removed
        url_get = reverse(
            'itemauthor-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.author.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
