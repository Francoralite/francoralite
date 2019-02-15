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

from django.forms.models import model_to_dict
from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.item_usefulness import ItemUsefulnessFactory
from ..models.item_usefulness import ItemUsefulness
# Models related
from ..models.usefulness import Usefulness
from ..models.item import Item

# Expected structure for Item_usefulness objects
ITEMUSEFULNESS_STRUCTURE = [
    ('id', int),
    ('item', dict),
    ('usefulness', dict),
]

# Expected keys for MODEL objects
ITEMUSEFULNESS_FIELDS = sorted(
    [item[0] for item in ITEMUSEFULNESS_STRUCTURE])


@pytest.mark.django_db
class TestItemUsefulnessList(APITestCase):
    """
    This class manage all ItemUsefulness tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        ItemUsefulnessFactory.create_batch(1)

    def test_can_get_item_usefulness_list(self):
        """
        Ensure ItemUsefulness objects exists
        """
        # kwargs for the related tables
        url = reverse('itemusefulness-list', kwargs={
            'item_pk': 1})

        # ORM side
        item_usefulnesss = ItemUsefulness.objects.all()
        self.assertEqual(len(item_usefulnesss), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(ITEMUSEFULNESS_STRUCTURE)
    def test_has_valid_item_usefulness_values(self,
                                              attribute, attribute_type):
        """
        Ensure ItemUsefulness objects have valid values
        """

        # kwargs for the related tables
        url = reverse('itemusefulness-list', kwargs={
            'item_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item_usefulness in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(item_usefulness.keys()), ITEMUSEFULNESS_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        item_usefulness[attribute], basestring)
                else:
                    self.assertIsInstance(
                        item_usefulness[attribute], str)
            else:
                self.assertIsInstance(
                    item_usefulness[attribute], attribute_type)
            self.assertIsNot(item_usefulness[attribute], '')

    def test_get_an_item_usefulness(self):
        """
        Ensure we can get an ItemUsefulness objects
        using an existing id
        """

        item = ItemUsefulness.objects.first()
        # kwargs for the related tables
        url = reverse('itemusefulness-detail', kwargs={
                      'item_pk': item.item.id,
                      'pk': item.usefulness.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_item_usefulness(self):
        """
        Ensure we can create an ItemUsefulness object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=ItemUsefulnessFactory)

        # Convert the related entity in dictionnaryself.
        #  Then they will be easily converted in JSON format.-
        data['item'] = Item.objects.first().id
        data['usefulness'] = Usefulness.objects.first().id

        url = reverse('itemusefulness-list', kwargs={
            'item_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            ITEMUSEFULNESS_FIELDS)

        # kwargs for the related tables
        url = reverse(
            'itemusefulness-detail',
            kwargs={'item_pk': response.data['item']['id'],
                    'pk': response.data['usefulness']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_an_item_usefulness(self):
        """
        Ensure we can delete an ItemUsefulness object
        """

        item = ItemUsefulness.objects.first()

        # Delete this object
        # kwargs for the related tables
        url = reverse(
            'itemusefulness-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.usefulness.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure ItemUsefulness removed
        # kwargs for the related tables
        url_get = reverse(
            'itemusefulness-detail', kwargs={
                'item_pk': item.item.id,
                'pk': item.usefulness.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
