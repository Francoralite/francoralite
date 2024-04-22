# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item Keyword tests
"""

import factory
import pytest

from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_keyword import ItemKeywordFactory
from .fake_data.fake_sound import CleanMediaMixin
from ..models.item_keyword import ItemKeyword

from .keycloak import get_token

# Expected structure for Item_keyword objects
ITEMKEYWORD_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('keyword', dict),
]

# Expected keys for MODEL objects
ITEMKEYWORD_FIELDS = sorted(
    [item[0] for item in ITEMKEYWORD_STRUCTURE])


@pytest.mark.django_db
class TestItemKeywordList(CleanMediaMixin, APITestCase):
    """
    This class manage all ItemKeyword tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)

        # Create a set of sample data
        ItemKeywordFactory.create_batch(6)

    def test_can_get_item_keyword_list(self):
        """
        Ensure ItemKeyword objects exists
        """
        # kwargs for the related tables
        url = reverse('itemkeyword-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_keywords = ItemKeyword.objects.all()
        self.assertEqual(len(item_keywords), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMKEYWORD_STRUCTURE)
    def test_has_valid_item_keyword_values(self, attribute, attribute_type):
        """
        Ensure ItemKeyword objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemkeyword-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_keyword in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_keyword.keys()), ITEMKEYWORD_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_keyword[attribute], str)
            else:
                self.assertIsInstance(item_keyword[attribute], attribute_type)
            self.assertIsNot(item_keyword[attribute], '')

    def test_get_an_item_keyword(self):
        """
        Ensure we can get an ItemKeyword objects
        using an existing id
        """

        item = ItemKeyword.objects.first()
        # kwargs for the related tables
        url = reverse('itemkeyword-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.keyword.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_keyword(self):
        """
        Ensure we can create an ItemKeyword object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemKeywordFactory)

        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.
        data['item'] = 1
        data['keyword'] = 2

        url = reverse('itemkeyword-list', kwargs={
            'item_pk': data['item']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMKEYWORD_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemkeyword-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_keyword(self):
        """
        Ensure we can delete an ItemKeyword object
        """

        item = ItemKeyword.objects.first()

        # Delete this object
        # kwargs for the related tables
        url = reverse(
            'itemkeyword-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.keyword.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemKeyword removed
        # kwargs for the related tables
        url_get = reverse(
            'itemkeyword-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.keyword.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
