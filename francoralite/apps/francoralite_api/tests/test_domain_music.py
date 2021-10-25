# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
DomainMusic tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.domain_music import DomainMusicFactory
from ..models.domain_music import DomainMusic

from .keycloak import get_token

# Expected structure for Domain_music objects
DOMAINMUSIC_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
DOMAINMUSIC_FIELDS = sorted(
    [item[0] for item in DOMAINMUSIC_STRUCTURE])


@pytest.mark.django_db
class TestDomainMusicList(APITestCase):
    """
    This class manage all DomainMusic tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")
        
        # Create a set of sample data
        DomainMusicFactory.create_batch(6)

    def test_can_get_domain_music_list(self):
        """
        Ensure DomainMusic objects exists
        """
        url = reverse('domainmusic-list')

        # ORM side
        domain_musics = DomainMusic.objects.all()
        self.assertEqual(len(domain_musics), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(DOMAINMUSIC_STRUCTURE)
    def test_has_valid_domain_music_values(
            self, attribute, attribute_type):
        """
        Ensure DomainMusic objects have valid values
        """

        url = reverse('domainmusic-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for domain_music in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    domain_music.keys()), DOMAINMUSIC_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(domain_music[attribute], str)
            else:
                self.assertIsInstance(
                    domain_music[attribute], attribute_type)
            self.assertIsNot(domain_music[attribute], '')

    def test_get_an_domain_music(self):
        """
        Ensure we can get an DomainMusic objects
        using an existing id
        """

        item = DomainMusic.objects.first()
        url = reverse('domainmusic-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_domain_music(self):
        """
        Ensure we can create an DomainMusic object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=DomainMusicFactory)
        url = reverse('domainmusic-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINMUSIC_FIELDS)

        url = reverse(
            'domainmusic-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_domain_music(self):
        """
        Ensure we can update an DomainMusic object
        """

        item = DomainMusic.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'domainmusic-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'domainmusic-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINMUSIC_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_domain_music(self):
        """
        Ensure we can patch an DomainMusic object
        """

        item = DomainMusic.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'domainmusic-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINMUSIC_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_domain_music(self):
        """
        Ensure we can delete an DomainMusic object
        """

        item = DomainMusic.objects.first()

        # Delete this object
        url = reverse(
            'domainmusic-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure DomainMusic removed
        url_get = reverse(
            'domainmusic-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
