# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Dance tests
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

from .factories.dance import DanceFactory
from ..models.dance import Dance

from .keycloak import get_token

# Expected structure for Dance objects
DANCE_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
DANCE_FIELDS = sorted(
    [item[0] for item in DANCE_STRUCTURE])


@pytest.mark.django_db
class TestDanceList(APITestCase):
    """
    This class manage all Dance tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        DanceFactory.create_batch(6)

    def test_can_get_dance_list(self):
        """
        Ensure Dance objects exists
        """
        url = reverse('dance-list')

        # ORM side
        dances = Dance.objects.all()
        self.assertEqual(len(dances), 6)

        # API side
        response = self.client.get(url, **self.auth_headers)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(DANCE_STRUCTURE)
    def test_has_valid_dance_values(
            self, attribute, attribute_type):
        """
        Ensure Dance objects have valid values
        """

        url = reverse('dance-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for dance in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    dance.keys()), DANCE_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        dance[attribute], basestring)
                else:
                    self.assertIsInstance(
                        dance[attribute], str)
            else:
                self.assertIsInstance(
                    dance[attribute], attribute_type)
            self.assertIsNot(dance[attribute], '')

    def test_get_an_dance(self):
        """
        Ensure we can get an Dance objects
        using an existing id
        """

        item = Dance.objects.first()
        url = reverse('dance-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_dance(self):
        """
        Ensure we can create an Dance object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=DanceFactory)
        url = reverse('dance-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DANCE_FIELDS)

        url = reverse(
            'dance-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_dance(self):
        """
        Ensure we can update an Dance object
        """

        item = Dance.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'dance-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'dance-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DANCE_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_dance(self):
        """
        Ensure we can patch an Dance object
        """

        item = Dance.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'dance-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DANCE_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_dance(self):
        """
        Ensure we can delete an Dance object
        """

        item = Dance.objects.first()

        # Delete this object
        url = reverse(
            'dance-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Dance removed
        url_get = reverse(
            'dance-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
