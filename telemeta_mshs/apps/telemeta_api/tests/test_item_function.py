# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ItemFunction tests
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

from .factories.item_function import ItemFunctionFactory
from ..models.item_function import ItemFunction

# Expected structure for Item_function objects
ITEMFUNCTION_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
ITEMFUNCTION_FIELDS = sorted(
    [item[0] for item in ITEMFUNCTION_STRUCTURE])


@pytest.mark.django_db
class TestItemFunctionList(APITestCase):
    """
    This class manage all ItemFunction tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        ItemFunctionFactory.create_batch(6)

    def test_can_get_item_function_list(self):
        """
        Ensure ItemFunction objects exists
        """
        url = reverse('itemfunction-list')

        # ORM side
        item_functions = ItemFunction.objects.all()
        self.assertEqual(len(item_functions), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(ITEMFUNCTION_STRUCTURE)
    def test_has_valid_item_function_values(
            self, attribute, attribute_type):
        """
        Ensure ItemFunction objects have valid values
        """

        url = reverse('itemfunction-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_function in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    item_function.keys()), ITEMFUNCTION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        item_function[attribute], basestring)
                else:
                    self.assertIsInstance(
                        item_function[attribute], str)
            else:
                self.assertIsInstance(
                    item_function[attribute], attribute_type)
            self.assertIsNot(item_function[attribute], '')

    def test_get_an_item_function(self):
        """
        Ensure we can get an ItemFunction objects
        using an existing id
        """

        item = ItemFunction.objects.first()
        url = reverse('itemfunction-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_function(self):
        """
        Ensure we can create an ItemFunction object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemFunctionFactory)
        url = reverse('itemfunction-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMFUNCTION_FIELDS)

        url = reverse(
            'itemfunction-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_item_function(self):
        """
        Ensure we can update an ItemFunction object
        """

        item = ItemFunction.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'itemfunction-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'itemfunction-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMFUNCTION_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_item_function(self):
        """
        Ensure we can patch an ItemFunction object
        """

        item = ItemFunction.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'itemfunction-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMFUNCTION_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_item_function(self):
        """
        Ensure we can delete an ItemFunction object
        """

        item = ItemFunction.objects.first()

        # Delete this object
        url = reverse(
            'itemfunction-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemFunction removed
        url_get = reverse(
            'itemfunction-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
