# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Fond tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.fond import FondFactory, FondFactoryMission
from ..models.fond import Fond
from ..models.mission import Mission
from ..models.institution import Institution
from ..models.acquisition_mode import AcquisitionMode

from .keycloak import get_token

# Expected structure for Fond objects
FOND_STRUCTURE = [
    ('id', int),
    ('title', str),
    ('alt_title', str),
    ('description', str),
    ('code', str),
    ('institution', dict),
    ('code_partner', str),
    ('acquisition_mode', dict),
    ('conservation_site', str),
    ('comment', str)
]

# Expected keys for MODEL objects
FOND_FIELDS = sorted([item[0] for item in FOND_STRUCTURE])


@pytest.mark.django_db
class TestFondList(APITestCase):
    """
    This class manage all Fond tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        
        # Create a set of sample data
        FondFactoryMission.create_batch(6, missions__nb_missions=4)

    def test_can_get_fond_list(self):
        """
        Ensure Fond objects exists
        """
        url = reverse('fond-list')

        # ORM side
        fonds = Fond.objects.all()
        self.assertEqual(len(fonds), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)


    def test_can_get_fond_missions_list(self):
        """
        Ensure related missions exist
        """
        url = reverse('mission-list')
        
        # ORM side
        missions = Mission.objects.all()
        self.assertEqual(len(missions), 24)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 24)


    def test_fond_dates(self):
        """
        Max and min dates from the related missions of a fonds
        """

        item = Fond.objects.first()
        url = '/api/fond/' + str(item.id) + "/dates"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_fond_informers(self):
        """
        Informers from the related collections of a fonds
        """

        item = Fond.objects.first()
        url = '/api/fond/' + str(item.id) + "/informers"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)


    def test_fond_collectors(self):
        """
        Informers from the related collections of a fonds
        """

        item = Fond.objects.first()
        url = '/api/fond/' + str(item.id) + "/collectors"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        
        
    def test_fond_duration(self):
        """
        Total duration of a fond : sum of mission/collection/items durations of this fond
        """
        item = Fond.objects.first()
        url = '/api/fond/' + str(item.id) + "/duration"
        response = self.client.get(url)
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, str)
        self.assertNotEqual(response.data, "0:00:00")
        self.assertNotEqual(response.data, "")


    @parameterized.expand(FOND_STRUCTURE)
    def test_has_valid_fond_values(self, attribute, attribute_type):
        """
        Ensure Fond objects have valid values
        """

        url = reverse('fond-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for fond in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(fond.keys()), FOND_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(fond[attribute], str)
            else:
                self.assertIsInstance(fond[attribute], attribute_type)
            self.assertIsNot(fond[attribute], '')

    def test_get_a_fond(self):
        """
        Ensure we can get an Fond objects
        using an existing id
        """

        item = Fond.objects.first()
        url = reverse('fond-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_fond(self):
        """
        Ensure we can create an Fond object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=FondFactory)

        institution = Institution.objects.first()
        acquisition_mode = AcquisitionMode.objects.first()
        # Write the Location object in the authority data object.
        data['institution'] = institution.id
        data['acquisition_mode'] = acquisition_mode.id

        url = reverse('fond-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            FOND_FIELDS)

        url = reverse(
            'fond-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_a_fond(self):
        """
        Ensure we can update an Fond object
        """

        item = Fond.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'fond-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['title'] = 'foobar_test_put'
        url = reverse(
            'fond-detail',
            kwargs={'pk': item.id})
        data['institution'] = data['institution']['id']
        data['acquisition_mode'] = data['acquisition_mode']['id']
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            FOND_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_put')

    def test_patch_a_fond(self):
        """
        Ensure we can patch an Fond object
        """

        item = Fond.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_patch')

        data = {'title': 'foobar_test_patch'}
        url = reverse(
            'fond-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            FOND_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_patch')
        
    def test_uniq_code_fond(self):
        """
        Ensure we don't validate a non-uniq fond code
        """

        item = Fond.objects.first()
        code_1 = item.code
        item = Fond.objects.last()

        data = {'code': code_1}
        url = reverse(
            'fond-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure code 409 returned
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_delete_a_fond(self):
        """
        Ensure we can delete an Fond object
        """

        item = Fond.objects.first()

        # Delete this object
        url = reverse(
            'fond-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Fond removed
        url_get = reverse(
            'fond-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
