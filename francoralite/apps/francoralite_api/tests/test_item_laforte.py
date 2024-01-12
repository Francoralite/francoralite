# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ItemLaforte tests
"""

import factory
import pytest

from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_laforte import ItemLaforteFactory
from .fake_data.fake_sound import CleanMediaMixin
from ..models.item_laforte import ItemLaforte

from .keycloak import get_token

# Expected structure for ItemLaforte objects
ITEM_LAFORTE_STRUCTURE = [
    ("id", int),
    ("item", factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.item.ItemFactory")),
    ("laforte", factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.ref_laforte.RefLaforteFactory")),
]

# Expected structure for ItemLaforte model objects
ITEM_LAFORTE_FIELDS = sorted([item[0] for item in ITEM_LAFORTE_STRUCTURE])


@pytest.mark.django_db
class TestItemLaforte(APITestCase, CleanMediaMixin):
    """
    ItemLaforte tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)

        # Create a set of sample data
        ItemLaforteFactory.create_batch(6)

    def test_can_get_item_laforte_list(self):
        """
        Ensure we can get a list of item_laforte.
        """

        url = reverse("itemlaforte-list", kwargs={'item_pk': 1})
        response = self.client.get(url)
        
        # ORM side
        item_laforte = ItemLaforte.objects.all()
        self.assertEqual(item_laforte.count(), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEM_LAFORTE_STRUCTURE)
    def test_has_valid_item_laforte_values(self, field, expected_type):
        """
        Ensure we can get a list of item_laforte.
        """

        url = reverse("itemlaforte-list", kwargs={'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item in response.data:
            # Ensure all keys are present
            self.assertEqual(sorted(item.keys()), ITEM_LAFORTE_FIELDS)

            # Ensure all values have the expected type
            if expected_type is int:
                for item in response.data:
                    self.assertIsInstance(item[field], int)
            elif expected_type is str:
                for item in response.data:
                    self.assertIsInstance(item[field], str)
            self.assertIsNot(item[field], "")

    def test_get_an_item_laforte(self):
        """
        Ensure we can get an ItemLaforte objects
        using an existing id
        """

        item_laforte = ItemLaforte.objects.first()
        url = reverse('itemlaforte-detail',
                      kwargs={
                          'item_pk': item_laforte.item.id,
                          'pk': item_laforte.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_laforte(self):
        """
        Ensure we can create an ItemLaforte object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemLaforteFactory)
        
        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.
        data['item'] = 1
        data['laforte'] = 2

        url = reverse('itemlaforte-list', kwargs={'item_pk': data['item']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEM_LAFORTE_FIELDS
        )

        # kwars for the related tables
        url = reverse('itemlaforte-detail',
                    kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
                    )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_delete_an_item_laforte(self):
        """
        Ensure we can delete an ItemLaforte object
        """

        item_laforte = ItemLaforte.objects.first()

        # Delete this object
        url = reverse(
            'itemlaforte-detail',
            kwargs={'item_pk': item_laforte.item.id,
                    'pk': item_laforte.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Item removed
        url_get = reverse(
            'itemlaforte-detail',
            kwargs={'item_pk': item_laforte.item.id,
                    'pk': item_laforte.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)





