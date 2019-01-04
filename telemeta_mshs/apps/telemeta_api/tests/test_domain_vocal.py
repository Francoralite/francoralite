# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
DomainVocal tests
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

from .factories.domain_vocal import DomainVocalFactory
from ..models.domain_vocal import DomainVocal

# Expected structure for Domain_vocal objects
DOMAINVOCAL_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
DOMAINVOCAL_FIELDS = sorted(
    [item[0] for item in DOMAINVOCAL_STRUCTURE])


@pytest.mark.django_db
class TestDomainVocalList(APITestCase):
    """
    This class manage all DomainVocal tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        DomainVocalFactory.create_batch(6)

    def test_can_get_domain_vocal_list(self):
        """
        Ensure DomainVocal objects exists
        """
        url = reverse('domainvocal-list')

        # ORM side
        domain_vocals = DomainVocal.objects.all()
        self.assertEqual(len(domain_vocals), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(DOMAINVOCAL_STRUCTURE)
    def test_has_valid_domain_vocal_values(
            self, attribute, attribute_type):
        """
        Ensure DomainVocal objects have valid values
        """

        url = reverse('domainvocal-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for domain_vocal in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    domain_vocal.keys()), DOMAINVOCAL_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        domain_vocal[attribute], basestring)
                else:
                    self.assertIsInstance(
                        domain_vocal[attribute], str)
            else:
                self.assertIsInstance(
                    domain_vocal[attribute], attribute_type)
            self.assertIsNot(domain_vocal[attribute], '')

    def test_get_an_domain_vocal(self):
        """
        Ensure we can get an DomainVocal objects
        using an existing id
        """

        item = DomainVocal.objects.first()
        url = reverse('domainvocal-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_domain_vocal(self):
        """
        Ensure we can create an DomainVocal object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=DomainVocalFactory)
        url = reverse('domainvocal-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINVOCAL_FIELDS)

        url = reverse(
            'domainvocal-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_domain_vocal(self):
        """
        Ensure we can update an DomainVocal object
        """

        item = DomainVocal.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'domainvocal-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'domainvocal-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINVOCAL_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_domain_vocal(self):
        """
        Ensure we can patch an DomainVocal object
        """

        item = DomainVocal.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'domainvocal-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINVOCAL_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_domain_vocal(self):
        """
        Ensure we can delete an DomainVocal object
        """

        item = DomainVocal.objects.first()

        # Delete this object
        url = reverse(
            'domainvocal-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure DomainVocal removed
        url_get = reverse(
            'domainvocal-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
