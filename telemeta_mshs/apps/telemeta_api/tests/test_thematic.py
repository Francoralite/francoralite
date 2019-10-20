# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Thematic tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.thematic import ThematicFactory
from ..models.thematic import Thematic

from .keycloak import get_token

# Expected structure for Thematic objects
THEMATIC_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
THEMATIC_FIELDS = sorted(
    [item[0] for item in THEMATIC_STRUCTURE])


@pytest.mark.django_db
class TestThematicList(APITestCase):
    """
    This class manage all Thematic tests
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
        ThematicFactory.create_batch(6)

    def test_can_get_thematic_list(self):
        """
        Ensure Thematic objects exists
        """
        url = reverse('thematic-list')

        # ORM side
        thematics = Thematic.objects.all()
        self.assertEqual(len(thematics), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(THEMATIC_STRUCTURE)
    def test_has_valid_thematic_values(
            self, attribute, attribute_type):
        """
        Ensure Thematic objects have valid values
        """

        url = reverse('thematic-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for thematic in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    thematic.keys()), THEMATIC_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        thematic[attribute], basestring)
                else:
                    self.assertIsInstance(
                        thematic[attribute], str)
            else:
                self.assertIsInstance(
                    thematic[attribute], attribute_type)
            self.assertIsNot(thematic[attribute], '')

    def test_get_an_thematic(self):
        """
        Ensure we can get an Thematic objects
        using an existing id
        """

        item = Thematic.objects.first()
        url = reverse('thematic-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_thematic(self):
        """
        Ensure we can create an Thematic object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ThematicFactory)
        url = reverse('thematic-list')
        print("+-+-+-+")
        print(data)
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            THEMATIC_FIELDS)

        url = reverse(
            'thematic-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_thematic(self):
        """
        Ensure we can update an Thematic object
        """

        item = Thematic.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'thematic-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'thematic-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            THEMATIC_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_thematic(self):
        """
        Ensure we can patch an Thematic object
        """

        item = Thematic.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'thematic-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            THEMATIC_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_thematic(self):
        """
        Ensure we can delete an Thematic object
        """

        item = Thematic.objects.first()

        # Delete this object
        url = reverse(
            'thematic-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Thematic removed
        url_get = reverse(
            'thematic-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
