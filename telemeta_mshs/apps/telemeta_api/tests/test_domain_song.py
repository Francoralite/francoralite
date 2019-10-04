# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
DomainSong tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.domain_song import DomainSongFactory
from ..models.domain_song import DomainSong

from .keycloak import get_token

# Expected structure for Domain_song objects
DOMAINSONG_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
DOMAINSONG_FIELDS = sorted(
    [item[0] for item in DOMAINSONG_STRUCTURE])


@pytest.mark.django_db
class TestDomainSongList(APITestCase):
    """
    This class manage all DomainSong tests
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
        DomainSongFactory.create_batch(6)

    def test_can_get_domain_song_list(self):
        """
        Ensure DomainSong objects exists
        """
        url = reverse('domainsong-list')

        # ORM side
        domain_songs = DomainSong.objects.all()
        self.assertEqual(len(domain_songs), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(DOMAINSONG_STRUCTURE)
    def test_has_valid_domain_song_values(
            self, attribute, attribute_type):
        """
        Ensure DomainSong objects have valid values
        """

        url = reverse('domainsong-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for domain_song in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    domain_song.keys()), DOMAINSONG_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        domain_song[attribute], basestring)
                else:
                    self.assertIsInstance(
                        domain_song[attribute], str)
            else:
                self.assertIsInstance(
                    domain_song[attribute], attribute_type)
            self.assertIsNot(domain_song[attribute], '')

    def test_get_an_domain_song(self):
        """
        Ensure we can get an DomainSong objects
        using an existing id
        """

        item = DomainSong.objects.first()
        url = reverse('domainsong-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_domain_song(self):
        """
        Ensure we can create an DomainSong object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=DomainSongFactory)
        url = reverse('domainsong-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINSONG_FIELDS)

        url = reverse(
            'domainsong-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_domain_song(self):
        """
        Ensure we can update an DomainSong object
        """

        item = DomainSong.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'domainsong-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'domainsong-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINSONG_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_domain_song(self):
        """
        Ensure we can patch an DomainSong object
        """

        item = DomainSong.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'domainsong-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            DOMAINSONG_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_domain_song(self):
        """
        Ensure we can delete an DomainSong object
        """

        item = DomainSong.objects.first()

        # Delete this object
        url = reverse(
            'domainsong-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure DomainSong removed
        url_get = reverse(
            'domainsong-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
