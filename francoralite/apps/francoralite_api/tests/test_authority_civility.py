# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Authority_civility tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.authority_civility import AuthorityCivilityFactory
from ..models.authority_civility import AuthorityCivility
from ..models.authority import Authority
from ..models.civility import Civility

from .keycloak import get_token

# Expected structure for Authority_civility objects
AUTHORITYCIVILITY_STRUCTURE = [
    ('id', int),
    ('authority', dict),
    ('civility', dict),
]

# Expected keys for MODEL objects
AUTHORITYCIVILITY_FIELDS = sorted(
    [item[0] for item in AUTHORITYCIVILITY_STRUCTURE])


@pytest.mark.django_db
class TestAuthorityCivilityList(APITestCase):
    """
    This class manage all AuthorityCivility tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)

        # Create a set of sample data
        AuthorityCivilityFactory.create_batch(6)

    def test_can_get_authority_civility_list(self):
        """
        Ensure AuthorityCivility objects exists
        """

        url = reverse('authoritycivility-list', kwargs={
            'authority_pk': 1})

        # ORM side
        authority_civilities = AuthorityCivility.objects.all()
        self.assertEqual(len(authority_civilities), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(AUTHORITYCIVILITY_STRUCTURE)
    def test_has_valid_authority_civility_values(self,
                                                  attribute, attribute_type):
        """
        Ensure AuthorityCivility objects have valid values
        """

        url = reverse('authoritycivility-list', kwargs={
            'authority_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for authority_civility in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(authority_civility.keys()), AUTHORITYCIVILITY_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(authority_civility[attribute], str)
            else:
                self.assertIsInstance(
                    authority_civility[attribute], attribute_type)
            self.assertIsNot(authority_civility[attribute], '')

    def test_get_a_authority_civility(self):
        """
        Ensure we can get an AuthorityCivility objects
        using an existing id
        """

        item = AuthorityCivility.objects.first()
        url = reverse('authoritycivility-detail', kwargs={
                      'authority_pk': item.authority.id,
                      'pk': item.civility.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_authority_civility(self):
        """
        Ensure we can create a AuthorityCivility object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=AuthorityCivilityFactory)

        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.-
        data['civility'] = 2
        data['authority'] = 1

        url = reverse('authoritycivility-list', kwargs={
            'authority_pk': data['authority']})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            AUTHORITYCIVILITY_FIELDS)

        url = reverse(
            'authoritycivility-detail',
            kwargs={'authority_pk': response.data['authority']['id'],
                    'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_a_authority_civility(self):
        """
        Ensure we can delete a AuthorityCivility object
        """

        item = AuthorityCivility.objects.first()

        # Delete this object
        url = reverse(
            'authoritycivility-detail', kwargs={
                'authority_pk': item.authority.id,
                'pk': item.civility.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure AuthorityCivility removed
        url_get = reverse(
            'authoritycivility-detail', kwargs={
                'authority_pk': item.authority.id,
                'pk': item.civility.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
