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

from .factories.collection_language import CollectionLanguageFactory
from ..models.collection_language import CollectionLanguage
from telemeta.models.language import Language
from ..models.collection import Collection

# Expected structure for Collection_language objects
COLLECTIONLANGUAGE_STRUCTURE = [
    ('id', int),
    ('collection', dict),
    ('language', dict),
]

# Expected keys for MODEL objects
COLLECTIONLANGUAGE_FIELDS = sorted(
    [item[0] for item in COLLECTIONLANGUAGE_STRUCTURE])


@pytest.mark.django_db
class TestCollectionLanguageList(APITestCase):
    """
    This class manage all CollectionLanguage tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')

        # Create a set of sample data
        CollectionLanguageFactory.create_batch(1)

    def test_can_get_collection_language_list(self):
        """
        Ensure CollectionLanguage objects exists
        """
        url = reverse('collectionlanguage-list', kwargs={
            'collection_pk': 1})

        # ORM side
        collection_languages = CollectionLanguage.objects.all()
        self.assertEqual(len(collection_languages), 1)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @parameterized.expand(COLLECTIONLANGUAGE_STRUCTURE)
    def test_has_valid_collection_language_values(self,
                                                  attribute, attribute_type):
        """
        Ensure CollectionLanguage objects have valid values
        """

        url = reverse('collectionlanguage-list', kwargs={
            'collection_pk': 1})
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for collection_language in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(collection_language.keys()), COLLECTIONLANGUAGE_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(collection_language[attribute], basestring)
                else:
                    self.assertIsInstance(collection_language[attribute], str)
            else:
                self.assertIsInstance(
                    collection_language[attribute], attribute_type)
            self.assertIsNot(collection_language[attribute], '')

    def test_get_a_collection_language(self):
        """
        Ensure we can get a CollectionLanguage objects
        using an existing id
        """

        item = CollectionLanguage.objects.first()
        #  kwargs for the related tables
        url = reverse('collectionlanguage-detail', kwargs={
                      'collection_pk': item.collection.id,
                      'pk': item.language.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_collection_language(self):
        """
        Ensure we can create a CollectionLanguage object
        """

        data = factory.build(
            dict,
            FACTORY_CLASS=CollectionLanguageFactory)

        # Convert the related entity in dictionnary.
        #  Then they will be easily converted in JSON format.
        data['language'] = Language.objects.first().id
        data['collection'] = Collection.objects.first().id

        url = reverse('collectionlanguage-list', kwargs={
            'collection_pk': 1})
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(
            sorted(response.data.keys()),
            COLLECTIONLANGUAGE_FIELDS)

        url = reverse(
            'collectionlanguage-detail',
            kwargs={'collection_pk': response.data['collection']['id'],
                    'pk': response.data['language']['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_delete_a_collection_language(self):
        """
        Ensure we can delete a CollectionLanguage object
        """

        item = CollectionLanguage.objects.first()

        # Delete this object

        # kwargs for the related tables
        url = reverse(
            'collectionlanguage-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.language.id}
        )
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure CollectionLanguage removed

        # kwargs for the related tables
        url_get = reverse(
            'collectionlanguage-detail', kwargs={
                'collection_pk': item.collection.id,
                'pk': item.language.id}
        )
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
