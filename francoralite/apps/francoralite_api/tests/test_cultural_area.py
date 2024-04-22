"""
CulturalArea tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.cultural_area import CulturalAreaFactory
from ..models.cultural_area import CulturalArea

from .keycloak import get_token

# Expected structure for CulturalArea objects
CULTURAL_AREA_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('geojson', str),
]

# Expected keys for CulturalArea objects
CULTURAL_AREA_FIELD = sorted([item[0] for item in CULTURAL_AREA_STRUCTURE])


@pytest.mark.django_db
class TestCulturalAreaList(APITestCase):
    """
    This class manage all Acquisition tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")

        CulturalAreaFactory.create_batch(6)

    def test_can_get_cultural_area_list(self):
        """
        Ensure CulturalArea objects exists
        """
        url = reverse('cultural_area-list')

        # ORM side
        cultural_areas = CulturalArea.objects.all()
        self.assertEqual(len(cultural_areas), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(CULTURAL_AREA_STRUCTURE)
    def test_has_valid_cultural_area_values(self, attribute, attribute_type):
        """
        Ensure CulturalArea objects have valid values
        """

        url = reverse('cultural_area-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for cultural_area in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(cultural_area.keys()), CULTURAL_AREA_FIELD)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(cultural_area[attribute], str)
            else:
                self.assertIsInstance(cultural_area[attribute], attribute_type)
            self.assertIsNot(cultural_area[attribute], '')

    def test_get_an_cultural_area(self):
        """
        Ensure we can get an CulturalArea objects using an existing id
        """

        item = CulturalArea.objects.first()
        url = reverse('cultural_area-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_cultural_area(self):
        """
        Ensure we can create an CulturalArea object
        """

        data = factory.build(dict, FACTORY_CLASS=CulturalAreaFactory)
        url = reverse('cultural_area-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), CULTURAL_AREA_FIELD)

        url = reverse(
            'cultural_area-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_cultural_area(self):
        """
        Ensure we can update an CulturalArea object
        """

        item = CulturalArea.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('cultural_area-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse('cultural_area-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), CULTURAL_AREA_FIELD)
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_cultural_area(self):
        """
        Ensure we can patch an CulturalArea object
        """

        item = CulturalArea.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse('cultural_area-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), CULTURAL_AREA_FIELD)
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_cultural_area(self):
        """
        Ensure we can delete an CulturalArea object
        """

        item = CulturalArea.objects.first()

        # Delete this object
        url = reverse('cultural_area-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure CulturalArea removed
        url_get = reverse('cultural_area-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
