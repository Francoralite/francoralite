# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Item_Coirault tests
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

from .factories.item_coirault import ItemCoiraultFactory
from ..models.item_coirault import ItemCoirault
# Models related
from ..models.skos_concept import SkosConcept
from ..models.item import Item

# Expected structure for Item_coirault objects
ITEMCOIRAULT_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('coirault', dict),
]

# Expected keys for MODEL objects
ITEMCOIRAULT_FIELDS = sorted(
    [item[0] for item in ITEMCOIRAULT_STRUCTURE])


@pytest.mark.django_db
class TestItemCoiraultList(APITestCase):
    """
    This class manage all ItemCoirault tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        ItemCoiraultFactory.create_batch(1)

    def test_can_get_item_coirault_list(self):
        """
        Ensure ItemCoirault objects exists
        """
        # kwargs for the related tables
        url = reverse('itemcoirault-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_coiraults = ItemCoirault.objects.all()
        self.assertEqual(len(item_coiraults), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMCOIRAULT_STRUCTURE)
    def test_has_valid_item_coirault_values(self, attribute, attribute_type):
        """
        Ensure ItemCoirault objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemcoirault-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_coirault in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_coirault.keys()), ITEMCOIRAULT_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(item_coirault[attribute], basestring)
                else:
                    self.assertIsInstance(item_coirault[attribute], str)
            else:
                self.assertIsInstance(item_coirault[attribute], attribute_type)
            self.assertIsNot(item_coirault[attribute], '')

    def test_get_an_item_coirault(self):
        """
        Ensure we can get an ItemCoirault objects
        using an existing id
        """

        item = ItemCoirault.objects.first()
        # kwargs for the related tables
        url = reverse('itemcoirault-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.coirault.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_coirault(self):
        """
        Ensure we can create an ItemCoirault object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemCoiraultFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = Item.objects.first().id
        data['coirault'] = SkosConcept.objects.first().id

        url = reverse('itemcoirault-list', kwargs={
            'item_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMCOIRAULT_FIELDS)

        url = reverse(
            'itemcoirault-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['coirault']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_coirault(self):
        """
        Ensure we can delete an ItemCoirault object
        """

        item = ItemCoirault.objects.first()

        # Delete this object
        url = reverse(
            'itemcoirault-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.coirault.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemCoirault removed
        url_get = reverse(
            'itemcoirault-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.coirault.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
