# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Institution tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.institution import InstitutionFactory
from ..models.institution import Institution

from .keycloak import get_token

# Expected structure for Institution objects
INSTITUTION_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for Institution objects
INSTITUTION_FIELDS = sorted([item[0] for item in INSTITUTION_STRUCTURE])


@pytest.mark.django_db
class TestInstitutionList(APITestCase):
    """
    This class manage all Institution tests
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
        InstitutionFactory.create_batch(6)

    def test_can_get_institution_list(self):
        """
        Ensure Institution objects exists
        """
        url = reverse('institution-list')

        # ORM side
        institutions = Institution.objects.all()
        self.assertEqual(len(institutions), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(INSTITUTION_STRUCTURE)
    def test_has_valid_institution_values(self, attribute, attribute_type):
        """
        Ensure Institution objects have valid values
        """

        url = reverse('institution-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for institution in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(institution.keys()), INSTITUTION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(institution[attribute], basestring)
                else:
                    self.assertIsInstance(institution[attribute], str)
            else:
                self.assertIsInstance(institution[attribute], attribute_type)
            self.assertIsNot(institution[attribute], '')

    def test_get_an_institution(self):
        """
        Ensure we can get an Institution objects using an existing id
        """

        item = Institution.objects.first()
        url = reverse('institution-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_institution(self):
        """
        Ensure we can create an Institution object
        """

        data = factory.build(dict, FACTORY_CLASS=InstitutionFactory)
        url = reverse('institution-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), INSTITUTION_FIELDS)

        url = reverse(
            'institution-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_institution(self):
        """
        Ensure we can update an Institution object
        """

        item = Institution.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('institution-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse('institution-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), INSTITUTION_FIELDS)
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_institution(self):
        """
        Ensure we can patch an Institution object
        """

        item = Institution.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse('institution-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), INSTITUTION_FIELDS)
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_institution(self):
        """
        Ensure we can delete an Institution object
        """

        item = Institution.objects.first()

        # Delete this object
        url = reverse('institution-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Institution removed
        url_get = reverse('institution-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
