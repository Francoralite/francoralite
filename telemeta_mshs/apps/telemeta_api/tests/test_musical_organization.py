# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
MusicalOrganization tests
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

from .factories.musical_organization import MusicalOrganizationFactory
from ..models.musical_organization import MusicalOrganization

# Expected structure for Musical_organization objects
MUSICALORGANIZATION_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
MUSICALORGANIZATION_FIELDS = sorted(
    [item[0] for item in MUSICALORGANIZATION_STRUCTURE])


@pytest.mark.django_db
class TestMusicalOrganizationList(APITestCase):
    """
    This class manage all MusicalOrganization tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        MusicalOrganizationFactory.create_batch(6)

    def test_can_get_musical_organization_list(self):
        """
        Ensure MusicalOrganization objects exists
        """
        url = reverse('musicalorganization-list')

        # ORM side
        musical_organizations = MusicalOrganization.objects.all()
        self.assertEqual(len(musical_organizations), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(MUSICALORGANIZATION_STRUCTURE)
    def test_has_valid_musical_organization_values(
            self, attribute, attribute_type):
        """
        Ensure MusicalOrganization objects have valid values
        """

        url = reverse('musicalorganization-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for musical_organization in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    musical_organization.keys()), MUSICALORGANIZATION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        musical_organization[attribute], basestring)
                else:
                    self.assertIsInstance(
                        musical_organization[attribute], str)
            else:
                self.assertIsInstance(
                    musical_organization[attribute], attribute_type)
            self.assertIsNot(musical_organization[attribute], '')

    def test_get_an_musical_organization(self):
        """
        Ensure we can get an MusicalOrganization objects
        using an existing id
        """

        item = MusicalOrganization.objects.first()
        url = reverse('musicalorganization-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_musical_organization(self):
        """
        Ensure we can create an MusicalOrganization object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=MusicalOrganizationFactory)
        url = reverse('musicalorganization-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MUSICALORGANIZATION_FIELDS)

        url = reverse(
            'musicalorganization-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_musical_organization(self):
        """
        Ensure we can update an MusicalOrganization object
        """

        item = MusicalOrganization.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'musicalorganization-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'musicalorganization-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MUSICALORGANIZATION_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_musical_organization(self):
        """
        Ensure we can patch an MusicalOrganization object
        """

        item = MusicalOrganization.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'musicalorganization-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MUSICALORGANIZATION_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_musical_organization(self):
        """
        Ensure we can delete an MusicalOrganization object
        """

        item = MusicalOrganization.objects.first()

        # Delete this object
        url = reverse(
            'musicalorganization-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure MusicalOrganization removed
        url_get = reverse(
            'musicalorganization-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
