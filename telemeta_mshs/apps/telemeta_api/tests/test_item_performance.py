# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ItemPerformance tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_performance import ItemPerformanceFactory
from ..models.item import Item
from ..models.performance_collection import PerformanceCollection
from ..models.item_performance import ItemPerformance
from ..models.instrument import Instrument
from ..models.emit_vox import EmitVox

from .keycloak import get_token

# Expected structure for ItemPerformance objects
ITEMPERFORMANCE_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('performance', dict),
]

# Expected keys for MODEL objects
ITEMPERFORMANCE_FIELDS = sorted([item[0] for item in ITEMPERFORMANCE_STRUCTURE])


@pytest.mark.django_db
class TestItemPerformanceList(APITestCase):
    """
    This class manage all ItemPerformance tests
    """
    
    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        self.url = "/api/item/1/performance"
        self.url_detail =  self.url + "/1"

        
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])
        
        # Create a set of sample data
        ItemPerformanceFactory.create_batch(6)

    def test_can_get_itemperformance_list(self):
        """
        Ensure ItemPerformance objects exists
        """
        
        # ORM side
        itemperformances = ItemPerformance.objects.all()
        self.assertEqual(len(itemperformances), 6)

        # API side
        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMPERFORMANCE_STRUCTURE)
    def test_has_valid_itemperformance_values(self, attribute, attribute_type):
        """
        Ensure PerformanceCollection objects have valid values
        """

        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for itemperformance in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(itemperformance.keys()), ITEMPERFORMANCE_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(itemperformance[attribute], basestring)
                else:
                    self.assertIsInstance(itemperformance[attribute], str)
            else:
                self.assertIsInstance(itemperformance[attribute], attribute_type)
            self.assertIsNot(itemperformance[attribute], '')

    def test_get_an_itemperformance(self):
        """
        Ensure we can get an ItemPerformance objects
        using an existing id
        """

        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_itemperformance(self):
        """
        Ensure we can create an ItemPerformance object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemPerformanceFactory)
        """  instrument = Instrument.objects.first()
        data['instrument'] = instrument.id
        emit = EmitVox.objects.first()
        data['emit'] = emit.id """
        performance= PerformanceCollection.objects.first()
        data['performance'] = performance.id
        data['item'] = 1
        
        response = self.client.post(self.url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMPERFORMANCE_FIELDS)
        response_get = self.client.get(self.url_detail)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_itemperformance(self):
        """
        Ensure we can delete an ItemPerformance object
        """

        # Delete this object
        response = self.client.delete(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemPerformance removed
        response_get = self.client.get(self.url_detail)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
