# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ItemAnalysis tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_analysis import ItemAnalysisFactory
from ..models.item_analysis import ItemAnalysis

# Models related
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_analysis objects
ITEM_ANALYSIS_STRUCTURE = [
    ('id', int),
    ('element_type', str),
    ('item', dict),
    ('analyzer_id', str),
    ('name', str),
    ('value', str),
    ('unit', str),

]

# Expected keys for MODEL objects
ITEM_ANALYSIS_FIELDS = sorted([item[0] for item in ITEM_ANALYSIS_STRUCTURE])


@pytest.mark.django_db
class TestItemAnalysisList(APITestCase):
    """
    This class manage all ItemAnalysis tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])
        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        ItemAnalysisFactory.create_batch(6)

    def test_can_get_item_analysis_list(self):
        """
        Ensure ItemAnalysis objects exists
        """
        url = reverse('itemanalysis-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_analysiss = ItemAnalysis.objects.all()
        self.assertEqual(len(item_analysiss), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(ITEM_ANALYSIS_STRUCTURE)
    def test_has_valid_item_analysis_values(self, attribute, attribute_type):
        """
        Ensure ItemAnalysis objects have valid values
        """

        url = reverse('itemanalysis-list', kwargs={'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_analysis in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_analysis.keys()), ITEM_ANALYSIS_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(item_analysis[attribute], basestring)
                else:
                    self.assertIsInstance(item_analysis[attribute], str)
            else:
                self.assertIsInstance(item_analysis[attribute], attribute_type)
            self.assertIsNot(item_analysis[attribute], '')

    def test_get_an_item_analysis(self):
        """
        Ensure we can get an ItemAnalysis objects
        using an existing id
        """

        item = ItemAnalysis.objects.first()
        url = reverse('itemanalysis-detail',
                      kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_analysis(self):
        """
        Ensure we can create an ItemAnalysis object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemAnalysisFactory)
        data['item'] = Item.objects.first().id

        url = reverse('itemanalysis-list', kwargs={
            'item_pk': Item.objects.first().id})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEM_ANALYSIS_FIELDS)

        url = reverse(
            'itemanalysis-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_item_analysis(self):
        """
        Ensure we can update an ItemAnalysis object
        """

        item = ItemAnalysis.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'itemanalysis-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        data['item'] = data['item']['id']
        url = reverse(
            'itemanalysis-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEM_ANALYSIS_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_item_analysis(self):
        """
        Ensure we can patch an ItemAnalysis object
        """

        item = ItemAnalysis.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'itemanalysis-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEM_ANALYSIS_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_item_analysis(self):
        """
        Ensure we can delete an ItemAnalysis object
        """

        item = ItemAnalysis.objects.first()

        # Delete this object
        url = reverse(
            'itemanalysis-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemAnalysis removed
        url_get = reverse(
            'itemanalysis-detail',
            kwargs={'item_pk': item.item.id, 'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
