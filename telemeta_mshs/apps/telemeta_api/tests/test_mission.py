# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Mission tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.mission import MissionFactory, MissionCollectionFactory
from ..models.mission import Mission
from ..models.fond import Fond
from ..models.collection import Collection

from .keycloak import get_token

# Expected structure for Mission objects
MISSION_STRUCTURE = [
    ('id', int),
    ('title', str),
    ('description', str),
    ('code', str),
    ('public_access', str),
    ('fonds', dict),
    ('code_partner', str)
]

# Expected keys for MODEL objects
MISSION_FIELDS = sorted([item[0] for item in MISSION_STRUCTURE])


@pytest.mark.django_db
class TestMissionList(APITestCase):
    """
    This class manage all Mission tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        # Create a set of sample data
        MissionCollectionFactory.create_batch(6, collections__nb_collections=4)

    def test_can_get_mission_list(self):
        """
        Ensure Mission objects exists
        """
        url = reverse('mission-list')

        # ORM side
        missions = Mission.objects.all()
        self.assertEqual(len(missions), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)


    def test_can_get_mission_collections_list(self):
        """
        Ensure related collections exist
        """
        url = reverse('collection-list')
        
        # ORM side
        collections = Collection.objects.all()
        self.assertEqual(len(collections), 24)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 24)


    def test_mission_dates(self):
        """
        Max and min dates from the related collections of a mission
        """

        item = Mission.objects.first()
        url = '/api/mission/' + str(item.id) + "/dates"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_mission_informers(self):
        """
        Informers from the related collections of a mission
        """

        item = Mission.objects.first()
        url = '/api/mission/' + str(item.id) + "/informers"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list) 
    
    
    def test_mission_collectors(self):
        """
        Collectors from the related collections of a mission
        """

        item = Mission.objects.first()
        url = '/api/mission/' + str(item.id) + "/collectors"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
    
    
    def test_mission_locations(self):
        """
        Locations from the related collections of a mission
        """

        item = Mission.objects.first()
        url = '/api/mission/' + str(item.id) + "/locations"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)


    @parameterized.expand(MISSION_STRUCTURE)
    def test_has_valid_mission_values(self, attribute, attribute_type):
        """
        Ensure Mission objects have valid values
        """

        url = reverse('mission-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for mission in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(mission.keys()), MISSION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(mission[attribute], basestring)
                else:
                    self.assertIsInstance(mission[attribute], str)
            else:
                self.assertIsInstance(mission[attribute], attribute_type)
            self.assertIsNot(mission[attribute], '')

    def test_get_an_mission(self):
        """
        Ensure we can get an Mission objects
        using an existing id
        """

        item = Mission.objects.first()
        url = reverse('mission-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_mission(self):
        """
        Ensure we can create an Mission object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=MissionFactory)

        fonds = Fond.objects.first()
        data['fonds'] = fonds.id

        url = reverse('mission-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MISSION_FIELDS)

        url = reverse(
            'mission-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_mission(self):
        """
        Ensure we can update an Mission object
        """

        item = Mission.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'mission-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['title'] = 'foobar_test_put'
        url = reverse(
            'mission-detail',
            kwargs={'pk': item.id})
        data['fonds'] = data['fonds']['id']
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MISSION_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_put')

    def test_patch_an_mission(self):
        """
        Ensure we can patch an Mission object
        """

        item = Mission.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_patch')

        data = {'title': 'foobar_test_patch'}
        url = reverse(
            'mission-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MISSION_FIELDS)
        self.assertEqual(response.data['title'], 'foobar_test_patch')

    def test_delete_an_mission(self):
        """
        Ensure we can delete an Mission object
        """

        item = Mission.objects.first()

        # Delete this object
        url = reverse(
            'mission-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Mission removed
        url_get = reverse(
            'mission-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
