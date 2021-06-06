# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
PerformanceCollection tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.performancecollection import PerformanceCollectionFactory
from ..models.performance_collection import PerformanceCollection
from ..models.instrument import Instrument
from ..models.emit_vox import EmitVox

from .keycloak import get_token

# Expected structure for Performancecollection objects
PERFORMANCECOLLECTION_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('number', str),
    ('instrument', dict),
    ('emit', dict),
]

# Expected keys for MODEL objects
PERFORMANCECOLLECTION_FIELDS = sorted([item[0] for item in PERFORMANCECOLLECTION_STRUCTURE])


@pytest.mark.django_db
class TestPerformanceCollectionList(APITestCase):
    """
    This class manage all PerformanceCollection tests
    """
    
    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        self.url = "/api/collection/1/performance"
        self.url_detail =  self.url + "/1"

        
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])
        
        # Create a set of sample data
        PerformanceCollectionFactory.create_batch(6)

    def test_can_get_performancecollection_list(self):
        """
        Ensure PerformanceCollection objects exists
        """
        
        # ORM side
        performancecollections = PerformanceCollection.objects.all()
        self.assertEqual(len(performancecollections), 6)

        # API side
        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(PERFORMANCECOLLECTION_STRUCTURE)
    def test_has_valid_performancecollection_values(self, attribute, attribute_type):
        """
        Ensure PerformanceCollection objects have valid values
        """

        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for performancecollection in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(performancecollection.keys()), PERFORMANCECOLLECTION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(performancecollection[attribute], str)
            else:
                self.assertIsInstance(performancecollection[attribute], attribute_type)
            self.assertIsNot(performancecollection[attribute], '')

    def test_get_an_performancecollection(self):
        """
        Ensure we can get an PerformanceCollection objects
        using an existing id
        """

        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_performancecollection(self):
        """
        Ensure we can create an PerformanceCollection object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=PerformanceCollectionFactory)
        instrument = Instrument.objects.first()
        data['instrument'] = instrument.id
        emit = EmitVox.objects.first()
        data['emit'] = emit.id
        data['collection'] = 1
        
        response = self.client.post(self.url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            PERFORMANCECOLLECTION_FIELDS)
        response_get = self.client.get(self.url_detail)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_performancecollection(self):
        """
        Ensure we can update an PerformanceCollection object
        """

        item = PerformanceCollection.objects.first()
        self.assertNotEqual(item.number, 42)

        # Get existing object from API
        data = self.client.get(self.url_detail).data

        data['number'] = 42
        data['collection'] = item.collection.id
        data['instrument'] = item.instrument.id
        data['emit'] = item.emit.id

        response = self.client.put("/api/collection/1/performance/1", data, format='json')

        # Ensure new number is returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            PERFORMANCECOLLECTION_FIELDS)
        self.assertEqual(response.data['number'], str(42))

    def test_patch_an_performancecollection(self):
        """
        Ensure we can patch an PerformanceCollection object
        """

        item = PerformanceCollection.objects.first()
        self.assertNotEqual(item.number, 43)

        data = {'number': 43}
        response = self.client.patch(self.url_detail, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            PERFORMANCECOLLECTION_FIELDS)
        self.assertEqual(response.data['number'], '43')

    def test_delete_an_performancecollection(self):
        """
        Ensure we can delete an PerformanceCollection object
        """

        # Delete this object
        response = self.client.delete(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure PerformanceCollection removed
        response_get = self.client.get(self.url_detail)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
