# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item Domain Vocal tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_domain_vocal import ItemDomainVocalFactory
from ..models.item_domain_vocal import ItemDomainVocal
# Models related
from ..models.domain_vocal import DomainVocal
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_domain_vocal objects
ITEMDOMAINVOCAL_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('domain_vocal', dict),
]

# Expected keys for MODEL objects
ITEMDOMAINVOCAL_FIELDS = sorted(
    [item[0] for item in ITEMDOMAINVOCAL_STRUCTURE])


@pytest.mark.django_db
class TestItemDomainVocalList(APITestCase):
    """
    This class manage all ItemDomainVocal tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        ItemDomainVocalFactory.create_batch(6)

    def test_can_get_item_domain_vocal_list(self):
        """
        Ensure ItemDomainVocal objects exists
        """
        # kwargs for the related tables
        url = reverse('itemdomainvocal-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_domain_vocals = ItemDomainVocal.objects.all()
        self.assertEqual(len(item_domain_vocals), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMDOMAINVOCAL_STRUCTURE)
    def test_has_valid_item_domain_vocal_values(self,
                                                attribute, attribute_type):
        """
        Ensure ItemDomainVocal objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemdomainvocal-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_domain_vocal in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_domain_vocal.keys()), ITEMDOMAINVOCAL_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(item_domain_vocal[attribute], str)
            else:
                self.assertIsInstance(
                    item_domain_vocal[attribute], attribute_type)
            self.assertIsNot(item_domain_vocal[attribute], '')

    def test_get_an_item_domain_vocal(self):
        """
        Ensure we can get an ItemDomainVocal objects
        using an existing id
        """

        item = ItemDomainVocal.objects.first()
        # kwargs for the related tables
        url = reverse('itemdomainvocal-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.domain_vocal.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_domain_vocal(self):
        """
        Ensure we can create an ItemDomainVocal object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemDomainVocalFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = Item.objects.last().id
        data['domain_vocal'] = DomainVocal.objects.first().id

        url = reverse('itemdomainvocal-list', kwargs={
            'item_pk': data['item']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMDOMAINVOCAL_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemdomainvocal-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_domain_vocal(self):
        """
        Ensure we can delete an ItemDomainVocal object
        """

        item = ItemDomainVocal.objects.first()

        # Delete this object
        # kwargs for the related tables
        url = reverse(
            'itemdomainvocal-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.domain_vocal.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemDomainVocal removed
        # kwargs for the related tables
        url_get = reverse(
            'itemdomainvocal-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.domain_vocal.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
