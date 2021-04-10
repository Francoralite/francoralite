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

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_language import ItemLanguageFactory
from ..models.item_language import ItemLanguage
# Models related
from ..models.language import Language
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_language objects
ITEMLANGUAGE_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('language', dict),
]

# Expected keys for MODEL objects
ITEMLANGUAGE_FIELDS = sorted(
    [item[0] for item in ITEMLANGUAGE_STRUCTURE])


@pytest.mark.django_db
class TestItemLanguageList(APITestCase):
    """
    This class manage all ItemLanguage tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        ItemLanguageFactory.create_batch(1)

    def test_can_get_item_language_list(self):
        """
        Ensure ItemLanguage objects exists
        """
        # kwargs for the related tables
        url = reverse('itemlanguage-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_languages = ItemLanguage.objects.all()
        self.assertEqual(len(item_languages), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMLANGUAGE_STRUCTURE)
    def test_has_valid_item_language_values(self, attribute, attribute_type):
        """
        Ensure ItemLanguage objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemlanguage-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_language in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_language.keys()), ITEMLANGUAGE_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(item_language[attribute], basestring)
                else:
                    self.assertIsInstance(item_language[attribute], str)
            else:
                self.assertIsInstance(item_language[attribute], attribute_type)
            self.assertIsNot(item_language[attribute], '')

    def test_get_an_item_language(self):
        """
        Ensure we can get an ItemLanguage objects
        using an existing id
        """

        item = ItemLanguage.objects.first()
        #  kwargs for the related tables
        url = reverse('itemlanguage-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.language.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_language(self):
        """
        Ensure we can create an ItemLanguage object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemLanguageFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = Item.objects.first().id
        data['language'] = Language.objects.first().id

        url = reverse('itemlanguage-list', kwargs={
            'item_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMLANGUAGE_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemlanguage-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['language']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_language(self):
        """
        Ensure we can delete an ItemLanguage object
        """

        item = ItemLanguage.objects.first()

        # Delete this object
        # kwargs for the related tables
        url = reverse(
            'itemlanguage-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.language.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemLanguage removed
        # kwargs for the related tables
        url_get = reverse(
            'itemlanguage-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.language.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
