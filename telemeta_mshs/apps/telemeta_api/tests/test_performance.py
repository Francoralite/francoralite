# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Performance tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.performance import PerformanceFactory
from ..models.performance import Performance
from ..models.instrument import Instrument
from ..models.emit_vox import EmitVox

from .keycloak import get_token

# Expected structure for Performance objects
PERFORMANCE_STRUCTURE = [
    ('id', int),
    ('number', int),
    ('instrument', dict),
    ('emit', dict),
]

# Expected keys for MODEL objects
PERFORMANCE_FIELDS = sorted([item[0] for item in PERFORMANCE_STRUCTURE])


@pytest.mark.django_db
class TestPerformanceList(APITestCase):
    """
    This class manage all Performance tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        PerformanceFactory.create_batch(6)

    def test_can_get_performance_list(self):
        """
        Ensure Performance objects exists
        """
        url = reverse('performance-list')

        # ORM side
        performances = Performance.objects.all()
        self.assertEqual(len(performances), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(PERFORMANCE_STRUCTURE)
    def test_has_valid_performance_values(self, attribute, attribute_type):
        """
        Ensure Performance objects have valid values
        """

        url = reverse('performance-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for performance in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(performance.keys()), PERFORMANCE_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(performance[attribute], basestring)
                else:
                    self.assertIsInstance(performance[attribute], str)
            else:
                self.assertIsInstance(performance[attribute], attribute_type)
            self.assertIsNot(performance[attribute], '')

    def test_get_an_performance(self):
        """
        Ensure we can get an Performance objects
        using an existing id
        """

        item = Performance.objects.first()
        url = reverse('performance-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_performance(self):
        """
        Ensure we can create an Performance object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=PerformanceFactory)

        instrument = Instrument.objects.first()
        data["instrument"] = instrument.id
        emit = EmitVox.objects.first()
        data["emit"] = emit.id

        url = reverse('performance-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            PERFORMANCE_FIELDS)

        url = reverse(
            'performance-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_performance(self):
        """
        Ensure we can update an Performance object
        """

        item = Performance.objects.first()
        self.assertNotEqual(item.number, 42)

        # Get existing object from API
        url_get = reverse(
            'performance-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['number'] = 42
        url = reverse(
            'performance-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            PERFORMANCE_FIELDS)
        self.assertEqual(response.data['number'], '42')

    def test_patch_an_performance(self):
        """
        Ensure we can patch an Performance object
        """

        item = Performance.objects.first()
        self.assertNotEqual(item.number, 12)

        data = {'number': 12}
        url = reverse(
            'performance-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            PERFORMANCE_FIELDS)
        self.assertEqual(response.data['number'], 12)

    def test_delete_an_performance(self):
        """
        Ensure we can delete an Performance object
        """

        item = Performance.objects.first()

        # Delete this object
        url = reverse(
            'performance-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Performance removed
        url_get = reverse(
            'performance-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
