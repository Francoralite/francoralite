"""
Authority tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.authority import AuthorityFactory, AuthorityContribsFactory
from ..models.authority import Authority
from ..models.location import Location

from .keycloak import get_token

# Expected structure for Authority objects
AUTHORITY_STRUCTURE = [
    ('id', int),
    ('last_name', str),
    ('first_name', str),
    ('civility', str),
    ('alias', str),
    ('is_collector', int),
    ('is_informer', bool),
    ('is_author', bool),
    ('is_composer', bool),
    ('is_editor', bool),
    ('birth_date', str),
    ('birth_location', dict),
    ('death_date', str),
    ('death_location', dict),
    ('biography', str),
    ('uri', str),
]

# Expected keys for Institution objects
AUTHORITY_FIELDS = sorted([item[0] for item in AUTHORITY_STRUCTURE])


@pytest.mark.django_db
class TestAuthorityList(APITestCase):
    """
    This class manage all Authority tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        
        AuthorityContribsFactory.create_batch(6)

    def test_can_get_authority_list(self):
        """
        Ensure Authority objects exists
        """
        url = reverse('authority-list')

        # ORM side
        authorities = Authority.objects.all()
        self.assertEqual(len(authorities), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(AUTHORITY_STRUCTURE)
    def test_has_valid_authority_values(self, attribute, attribute_type):
        """
        Ensure Authority objects have valid values
        """

        url = reverse('authority-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for authority in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(authority.keys()), AUTHORITY_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                    self.assertIsInstance(authority[attribute], str)
            else:
                self.assertIsInstance(authority[attribute], attribute_type)
            self.assertIsNot(authority[attribute], '')

    def test_get_an_authority(self):
        """
        Ensure we can get an Authority objects using an existing id
        """

        item = Authority.objects.first()
        url = reverse('authority-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_authority(self):
        """
        Ensure we can create an Authority object
        """

        data = factory.build(dict, FACTORY_CLASS=AuthorityFactory)

        loc = Location.objects.first()
        # Write the Location object in the authority data object.
        data['birth_location'] = loc.id
        data['death_location'] = loc.id

        url = reverse('authority-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), AUTHORITY_FIELDS)

        url = reverse(
            'authority-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_contribs(self):
        item = Authority.objects.first()
        url = reverse('authority-contribs', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(len(response.data["informers"]), 6)
        self.assertEqual(len(response.data["collectors"]), 6)
        self.assertEqual(len(response.data["authors"]), 6)
        self.assertEqual(len(response.data["compositors"]), 6)

    def test_update_an_authority(self):
        """
        Ensure we can update an Authority object
        """

        item = Authority.objects.first()
        self.assertNotEqual(item.last_name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('authority-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['last_name'] = 'foobar_test_put'
        data['birth_location'] = data['birth_location']['id']
        data['death_location'] = data['death_location']['id']
        url = reverse('authority-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), AUTHORITY_FIELDS)
        self.assertEqual(response.data['last_name'], 'foobar_test_put')

    def test_patch_an_authority(self):
        """
        Ensure we can patch an Authority object
        """

        item = Authority.objects.first()
        self.assertNotEqual(item.last_name, 'foobar_test_patch')

        data = {'last_name': 'foobar_test_patch'}
        url = reverse('authority-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), AUTHORITY_FIELDS)
        self.assertEqual(response.data['last_name'], 'foobar_test_patch')

    def test_delete_an_authority(self):
        """
        Ensure we can delete an Authority object
        """

        item = Authority.objects.first()

        # Delete this object
        url = reverse('authority-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Authority removed
        url_get = reverse('authority-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
