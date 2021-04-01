# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Instrument tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.instrument import InstrumentFactory
from ..models.instrument import Instrument
from ..models.hornbostelsachs import HornbostelSachs

from .keycloak import get_token

# Expected structure for Instrument objects
INSTRUMENT_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
    ('typology',dict),
]

# Expected keys for MODEL objects
INSTRUMENT_FIELDS = sorted([item[0] for item in INSTRUMENT_STRUCTURE])


@pytest.mark.django_db
class TestInstrumentList(APITestCase):
    """
    This class manage all Instrument tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])


        # Create a set of sample data
        InstrumentFactory.create_batch(6)

    def test_can_get_instrument_list(self):
        """
        Ensure Instrument objects exists
        """
        url = reverse('instrument-list')

        # ORM side
        instruments = Instrument.objects.all()
        self.assertEqual(len(instruments), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(INSTRUMENT_STRUCTURE)
    def test_has_valid_instrument_values(self, attribute, attribute_type):
        """
        Ensure Instrument objects have valid values
        """

        url = reverse('instrument-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for instrument in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(instrument.keys()), INSTRUMENT_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(instrument[attribute], basestring)
                else:
                    self.assertIsInstance(instrument[attribute], str)
            else:
                self.assertIsInstance(instrument[attribute], attribute_type)
            self.assertIsNot(instrument[attribute], '')

    def test_get_an_instrument(self):
        """
        Ensure we can get an Instrument objects
        using an existing id
        """

        item = Instrument.objects.first()
        url = reverse('instrument-detail',
                      kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_instrument(self):
        """
        Ensure we can create an Instrument object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=InstrumentFactory)

        typology = HornbostelSachs.objects.first()
        # Write the HornbostelSachs object in the item data object.
        data['typology'] = typology.id

        url = reverse('instrument-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            INSTRUMENT_FIELDS)

        url = reverse(
            'instrument-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_instrument(self):
        """
        Ensure we can update an Instrument object
        """

        item = Instrument.objects.first()
        self.assertNotEqual(item.notes, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse(
            'instrument-detail',
            kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['notes'] = 'foobar_test_put'
        data['typology'] = data['typology']['id']

        url = reverse(
            'instrument-detail',
            kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            INSTRUMENT_FIELDS)

        self.assertEqual(response.data['notes'], 'foobar_test_put')

    def test_patch_an_instrument(self):
        """
        Ensure we can patch an Instrument object
        """

        item = Instrument.objects.first()

        self.assertNotEqual(item.notes, 'foobar_test_patch')

        data = {'notes': 'foobar_test_patch'}
        url = reverse(
            'instrument-detail',
            kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new notes returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            INSTRUMENT_FIELDS)
        self.assertEqual(response.data['notes'], 'foobar_test_patch')

    def test_delete_an_instrument(self):
        """
        Ensure we can delete an Instrument object
        """

        item = Instrument.objects.first()

        # Delete this object
        url = reverse(
            'instrument-detail',
            kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Instrument removed
        url_get = reverse(
            'instrument-detail',
            kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
