"""
Coupe tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.coupe import CoupeFactory
from ..models.coupe import Coupe

from .keycloak import get_token

# Expected structure for Coupe objects
COUPE_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for Coupe objects
COUPE_FIELD = sorted([item[0] for item in COUPE_STRUCTURE])


@pytest.mark.django_db
class TestCoupeList(APITestCase):
    """
    This class manage all Acquisition tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")

        CoupeFactory.create_batch(6)

    def test_can_get_coupe_list(self):
        """
        Ensure Coupe objects exists
        """
        url = reverse('coupe-list')

        # ORM side
        coupes = Coupe.objects.all()
        self.assertEqual(len(coupes), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(COUPE_STRUCTURE)
    def test_has_valid_coupe_values(self, attribute, attribute_type):
        """
        Ensure Coupe objects have valid values
        """

        url = reverse('coupe-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for coupe in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(coupe.keys()), COUPE_FIELD)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(coupe[attribute], str)
            else:
                self.assertIsInstance(coupe[attribute], attribute_type)
            self.assertIsNot(coupe[attribute], '')

    def test_get_an_coupe(self):
        """
        Ensure we can get an Coupe objects using an existing id
        """

        item = Coupe.objects.first()
        url = reverse('coupe-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_coupe(self):
        """
        Ensure we can create an Coupe object
        """

        data = factory.build(dict, FACTORY_CLASS=CoupeFactory)
        url = reverse('coupe-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), COUPE_FIELD)

        url = reverse(
            'coupe-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_coupe(self):
        """
        Ensure we can update an Coupe object
        """

        item = Coupe.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('coupe-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse('coupe-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), COUPE_FIELD)
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_coupe(self):
        """
        Ensure we can patch an Coupe object
        """

        item = Coupe.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse('coupe-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), COUPE_FIELD)
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_coupe(self):
        """
        Ensure we can delete an Coupe object
        """

        item = Coupe.objects.first()

        # Delete this object
        url = reverse('coupe-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Coupe removed
        url_get = reverse('coupe-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
