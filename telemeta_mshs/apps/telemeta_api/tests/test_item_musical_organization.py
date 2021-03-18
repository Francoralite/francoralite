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
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_musical_organization import ItemMusicalOrganizationFactory
from ..models.item_musical_organization import ItemMusicalOrganization
# Models related
from ..models.musical_organization import MusicalOrganization
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_musical_organization objects
ITEMMUSICALORGANIZATION_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('musical_organization', dict),
]

# Expected keys for MODEL objects
ITEMMUSICALORGANIZATION_FIELDS = sorted(
    [item[0] for item in ITEMMUSICALORGANIZATION_STRUCTURE])


@pytest.mark.django_db
class TestItemMusicalOrganizationList(APITestCase):
    """
    This class manage all ItemMusicalOrganization tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        ItemMusicalOrganizationFactory.create_batch(1)

    def test_can_get_item_musical_organization_list(self):
        """
        Ensure ItemMusicalOrganization objects exists
        """
        # kwargs for the related tables
        url = reverse('itemmusicalorganization-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_musical_organizations = ItemMusicalOrganization.objects.all()
        self.assertEqual(len(item_musical_organizations), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMMUSICALORGANIZATION_STRUCTURE)
    def test_has_valid_item_musical_organization_values(self,
                                                        attribute,
                                                        attribute_type):
        """
        Ensure ItemMusicalOrganization objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemmusicalorganization-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_musical_organization in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_musical_organization.keys()),
                ITEMMUSICALORGANIZATION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        item_musical_organization[attribute], basestring)
                else:
                    self.assertIsInstance(
                        item_musical_organization[attribute], str)
            else:
                self.assertIsInstance(
                    item_musical_organization[attribute], attribute_type)
            self.assertIsNot(item_musical_organization[attribute], '')

    def test_get_an_item_musical_organization(self):
        """
        Ensure we can get an ItemMusicalOrganization objects
        using an existing id
        """

        item = ItemMusicalOrganization.objects.first()
        #  kwargs for the related tables
        url = reverse('itemmusicalorganization-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.musical_organization.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_musical_organization(self):
        """
        Ensure we can create an ItemMusicalOrganization object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemMusicalOrganizationFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = Item.objects.first().id
        data['musical_organization'] = MusicalOrganization.objects.first().id

        url = reverse('itemmusicalorganization-list', kwargs={
            'item_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMMUSICALORGANIZATION_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemmusicalorganization-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['musical_organization']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_musical_organization(self):
        """
        Ensure we can delete an ItemMusicalOrganization object
        """

        item = ItemMusicalOrganization.objects.first()

        # Delete this object
        #  kwargs for the related tables
        url = reverse(
            'itemmusicalorganization-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.musical_organization.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemMusicalOrganization removed
        #  kwargs for the related tables
        url_get = reverse(
            'itemmusicalorganization-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.musical_organization.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
