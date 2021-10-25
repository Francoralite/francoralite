# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:  2000  history | grep cookie / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
PerformanceCollectionMusician tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.performancecollectionmusician import PerformanceCollectionMusicianFactory
from ..models.performance_collection_musician import PerformanceCollectionMusician
from ..models.performance_collection import PerformanceCollection
from ..models.authority import Authority

from .keycloak import get_token

# Expected structure for Performancecollectionmusician objects
PERFORMANCECOLLECTIONMUSICIAN_STRUCTURE = [
    ('id', int),
    ('performance_collection', dict),
    ('musician', dict),
]

# Expected keys for MODEL objects
PERFORMANCECOLLECTIONMUSICIAN_FIELDS = sorted([item[0] for item in PERFORMANCECOLLECTIONMUSICIAN_STRUCTURE])


@pytest.mark.django_db
class TestPerformanceCollectionMusicianList(APITestCase):
    """
    This class manage all PerformanceCollectionMusician tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        self.url = "/api/collection/1/performance/1/musician"
        self.url_detail =  self.url + "/1"
        
        get_token(self)
                
        # Create a set of sample data
        PerformanceCollectionMusicianFactory.create_batch(6)

    def test_can_get_performancecollectionmusician_list(self):
        """
        Ensure PerformanceCollectionMusician objects exists
        """

        # ORM side
        performancecollectionmusicians = PerformanceCollectionMusician.objects.all()
        self.assertEqual(len(performancecollectionmusicians), 6)

        # API side
        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(PERFORMANCECOLLECTIONMUSICIAN_STRUCTURE)
    def test_has_valid_performancecollectionmusician_values(self, attribute, attribute_type):
        """
        Ensure PerformanceCollectionMusician objects have valid values
        """

        response = self.client.get(self.url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for performancecollectionmusician in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(performancecollectionmusician.keys()), PERFORMANCECOLLECTIONMUSICIAN_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(performancecollectionmusician[attribute], str)
            else:
                self.assertIsInstance(performancecollectionmusician[attribute], attribute_type)
            self.assertIsNot(performancecollectionmusician[attribute], '')

    def test_get_an_performancecollectionmusician(self):
        """
        Ensure we can get an PerformanceCollectionMusician objects
        using an existing id
        """

        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_performancecollectionmusician(self):
        """
        Ensure we can create an PerformanceCollectionMusician object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=PerformanceCollectionMusicianFactory)
        performance = PerformanceCollection.objects.first()
        data['performance_collection'] = performance.id
        musician = Authority.objects.first()
        data['musician'] = musician.id

        response = self.client.post(self.url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            PERFORMANCECOLLECTIONMUSICIAN_FIELDS)
        response_get = self.client.get(self.url_detail)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_performancecollectionmusician(self):
        """
        Ensure we can delete an PerformanceCollectionMusician object
        """

        item = PerformanceCollectionMusician.objects.first()

        # Delete this object
        response = self.client.delete(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure PerformanceCollectionMusician removed
        response_get = self.client.get(self.url_detail)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
