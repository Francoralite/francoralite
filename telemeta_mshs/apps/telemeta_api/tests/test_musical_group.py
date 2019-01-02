# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
MusicalGroup tests
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

from .factories.musical_group import MusicalGroupFactory
from ..models.musical_group import MusicalGroup

# Expected structure for Musical_group objects
MUSICALGROUP_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for MODEL objects
MUSICALGROUP_FIELDS = sorted(
    [item[0] for item in MUSICALGROUP_STRUCTURE])


@pytest.mark.django_db
class TestMusicalGroupList(APITestCase):
    """
    This class manage all MusicalGroup tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        MusicalGroupFactory.create_batch(6)

    def test_can_get_musical_group_list(self):
        """
        Ensure MusicalGroup objects exists
        """
        url = reverse('musicalgroup-list')

        # ORM side
        musical_groups = MusicalGroup.objects.all()
        self.assertEqual(len(musical_groups), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(MUSICALGROUP_STRUCTURE)
    def test_has_valid_musical_group_values(
            self, attribute, attribute_type):
        """
        Ensure MusicalGroup objects have valid values
        """

        url = reverse('musicalgroup-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for musical_group in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(
                    musical_group.keys()), MUSICALGROUP_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        musical_group[attribute], basestring)
                else:
                    self.assertIsInstance(
                        musical_group[attribute], str)
            else:
                self.assertIsInstance(
                    musical_group[attribute], attribute_type)
            self.assertIsNot(musical_group[attribute], '')

    def test_get_an_musical_group(self):
        """
        Ensure we can get an MusicalGroup objects
        using an existing id
        """

        item = MusicalGroup.objects.first()
        url = reverse('musicalgroup-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_musical_group(self):
        """
        Ensure we can create an MusicalGroup object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=MusicalGroupFactory)
        url = reverse('musicalgroup-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MUSICALGROUP_FIELDS)

        url = reverse(
            'musicalgroup-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_musical_group(self):
        """
        Ensure we can update an MusicalGroup object
        """

        item = MusicalGroup.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'musicalgroup-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse(
            'musicalgroup-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MUSICALGROUP_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_musical_group(self):
        """
        Ensure we can patch an MusicalGroup object
        """

        item = MusicalGroup.objects.first()

        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse(
            'musicalgroup-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            MUSICALGROUP_FIELDS)

        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_musical_group(self):
        """
        Ensure we can delete an MusicalGroup object
        """

        item = MusicalGroup.objects.first()

        # Delete this object
        url = reverse(
            'musicalgroup-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure MusicalGroup removed
        url_get = reverse(
            'musicalgroup-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
