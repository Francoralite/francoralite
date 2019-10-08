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

from .factories.location_gis import LocationGisFactory
from ..models.location import Location

from .keycloak import get_token

# Expected structure for Location objects
LOCATION_STRUCTURE = [
    ('id', int),
    ('code', str),
    ('name', str),
    ('notes', str),
    ('latitude', float),
    ('longitude', float)
]

# Expected keys for Institution objects
LOCATION_FIELDS = sorted([item[0] for item in LOCATION_STRUCTURE])


@pytest.mark.django_db
class TestLocationList(APITestCase):
    """
    This class manage all Location tests
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
        LocationGisFactory.create_batch(6)

    def test_can_get_location_list(self):
        """
        Ensure Location objects exists
        """
        url = reverse('location_gis-list')

        # ORM side
        locations = Location.objects.all()
        self.assertEqual(len(locations), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(LOCATION_STRUCTURE)
    def test_has_valid_location_values(self, attribute, attribute_type):
        """
        Ensure Location objects have valid values
        """

        url = reverse('location_gis-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for location in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(location.keys()), LOCATION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(location[attribute], basestring)
                else:
                    self.assertIsInstance(location[attribute], str)
            else:
                self.assertIsInstance(
                    location[attribute], attribute_type)
            self.assertIsNot(location[attribute], '')

    def test_get_a_location(self):
        """
        Ensure we can get an Location objects using an existing id
        """

        item = Location.objects.first()
        url = reverse('location_gis-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_location(self):
        """
        Ensure we can create an Location object
        """

        data = factory.build(dict, FACTORY_CLASS=LocationGisFactory)
        url = reverse('location_gis-list')

        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), LOCATION_FIELDS)

        url = reverse(
            'location_gis-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_a_location(self):
        """
        Ensure we can update an Location object
        """

        item = Location.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('location_gis-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse('location_gis-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), LOCATION_FIELDS)
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_a_location(self):
        """
        Ensure we can patch an Location object
        """

        item = Location.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse('location_gis-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), LOCATION_FIELDS)
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_a_location(self):
        """
        Ensure we can delete an Location object
        """

        item = Location.objects.first()

        # Delete this object
        url = reverse('location_gis-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Location removed
        url_get = reverse('location_gis-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
