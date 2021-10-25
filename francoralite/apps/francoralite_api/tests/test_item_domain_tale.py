# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item Domain Tale tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_domain_tale import ItemDomainTaleFactory
from ..models.item_domain_tale import ItemDomainTale
# Models related
from ..models.domain_tale import DomainTale
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_domain_tale objects
ITEMDOMAINTALE_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('domain_tale', dict),
]

# Expected keys for MODEL objects
ITEMDOMAINTALE_FIELDS = sorted(
    [item[0] for item in ITEMDOMAINTALE_STRUCTURE])


@pytest.mark.django_db
class TestItemDomainTaleList(APITestCase):
    """
    This class manage all ItemDomainTale tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        
        # Create a set of sample data
        ItemDomainTaleFactory.create_batch(1)

    def test_can_get_item_domain_tale_list(self):
        """
        Ensure ItemDomainTale objects exists
        """
        # kwargs for the related tables
        url = reverse('itemdomaintale-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_domain_tales = ItemDomainTale.objects.all()
        self.assertEqual(len(item_domain_tales), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMDOMAINTALE_STRUCTURE)
    def test_has_valid_item_domain_tale_values(self,
                                               attribute, attribute_type):
        """
        Ensure ItemDomainTale objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemdomaintale-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_domain_tale in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_domain_tale.keys()), ITEMDOMAINTALE_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_domain_tale[attribute], str)
            else:
                self.assertIsInstance(
                    item_domain_tale[attribute], attribute_type)
            self.assertIsNot(item_domain_tale[attribute], '')

    def test_get_an_item_domain_tale(self):
        """
        Ensure we can get an ItemDomainTale objects
        using an existing id
        """

        item = ItemDomainTale.objects.first()
        # kwargs for the related tables
        url = reverse('itemdomaintale-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.domain_tale.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_domain_tale(self):
        """
        Ensure we can create an ItemDomainTale object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemDomainTaleFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = Item.objects.first().id
        data['domain_tale'] = DomainTale.objects.first().id

        url = reverse('itemdomaintale-list', kwargs={
            'item_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMDOMAINTALE_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemdomaintale-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['domain_tale']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_domain_tale(self):
        """
        Ensure we can delete an ItemDomainTale object
        """

        item = ItemDomainTale.objects.first()

        # Delete this object
        # kwargs for the related tables
        url = reverse(
            'itemdomaintale-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.domain_tale.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemDomainTale removed
        # kwargs for the related tables
        url_get = reverse(
            'itemdomaintale-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.domain_tale.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
