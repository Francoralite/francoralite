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

from .factories.item_musical_group import ItemMusicalGroupFactory
from ..models.item_musical_group import ItemMusicalGroup
# Models related
from ..models.musical_group import MusicalGroup
from ..models.item import Item

from .keycloak import get_token

# Expected structure for Item_musical_group objects
ITEMMUSICALGROUP_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('musical_group', dict),
]

# Expected keys for MODEL objects
ITEMMUSICALGROUP_FIELDS = sorted(
    [item[0] for item in ITEMMUSICALGROUP_STRUCTURE])


@pytest.mark.django_db
class TestItemMusicalGroupList(APITestCase):
    """
    This class manage all ItemMusicalGroup tests
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
        ItemMusicalGroupFactory.create_batch(1)

    def test_can_get_item_musical_group_list(self):
        """
        Ensure ItemMusicalGroup objects exists
        """
        # kwargs for the related tables
        url = reverse('itemmusicalgroup-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_musical_groups = ItemMusicalGroup.objects.all()
        self.assertEqual(len(item_musical_groups), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMMUSICALGROUP_STRUCTURE)
    def test_has_valid_item_musical_group_values(self,
                                                 attribute, attribute_type):
        """
        Ensure ItemMusicalGroup objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemmusicalgroup-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_musical_group in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_musical_group.keys()), ITEMMUSICALGROUP_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        item_musical_group[attribute], basestring)
                else:
                    self.assertIsInstance(
                        item_musical_group[attribute], str)
            else:
                self.assertIsInstance(
                    item_musical_group[attribute], attribute_type)
            self.assertIsNot(item_musical_group[attribute], '')

    def test_get_an_item_musical_group(self):
        """
        Ensure we can get an ItemMusicalGroup objects
        using an existing id
        """

        item = ItemMusicalGroup.objects.first()
        # kwargs for the related tables
        url = reverse('itemmusicalgroup-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.musical_group.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_musical_group(self):
        """
        Ensure we can create an ItemMusicalGroup object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemMusicalGroupFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.
        data['item'] = Item.objects.first().id
        data['musical_group'] = MusicalGroup.objects.first().id

        url = reverse('itemmusicalgroup-list', kwargs={
            'item_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMMUSICALGROUP_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemmusicalgroup-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['musical_group']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_musical_group(self):
        """
        Ensure we can delete an ItemMusicalGroup object
        """

        item = ItemMusicalGroup.objects.first()

        # Delete this object
        #  kwargs for the related tables
        url = reverse(
            'itemmusicalgroup-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.musical_group.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemMusicalGroup removed
        #  kwargs for the related tables
        url_get = reverse(
            'itemmusicalgroup-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.musical_group.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
