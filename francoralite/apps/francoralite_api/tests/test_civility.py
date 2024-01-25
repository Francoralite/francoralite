"""
Civility tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.civility import CivilityFactory
from ..models.civility import Civility

from .keycloak import get_token

# Expected structure for Civility objects
CIVILITY_STRUCTURE = [
    ('id', int),
    ('name', str),
]

# Expected keys for Civility objects
CIVILITY_FIELD = sorted([item[0] for item in CIVILITY_STRUCTURE])


@pytest.mark.django_db
class TestCivilityList(APITestCase):
    """
    This class manage all Civility tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")

        CivilityFactory.create_batch(6)

    def test_can_get_civility_list(self):
        """
        Ensure Civility objects exists
        """
        url = reverse('civility-list')

        # ORM side
        civilities = Civility.objects.all()
        self.assertEqual(len(civilities), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(CIVILITY_STRUCTURE)
    def test_has_valid_civility_values(self, attribute, attribute_type):
        """
        Ensure Civility objects have valid values
        """

        url = reverse('civility-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for civility in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(civility.keys()), CIVILITY_FIELD)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(civility[attribute], str)
            else:
                self.assertIsInstance(civility[attribute], attribute_type)
            self.assertIsNot(civility[attribute], '')

    def test_get_an_civility(self):
        """
        Ensure we can get an Civility objects using an existing id
        """

        item = Civility.objects.first()
        url = reverse('civility-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_civility(self):
        """
        Ensure we can create an Civility object
        """

        data = factory.build(dict, FACTORY_CLASS=CivilityFactory)
        url = reverse('civility-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), CIVILITY_FIELD)

        url = reverse(
            'civility-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_civility(self):
        """
        Ensure we can update an Civility object
        """

        item = Civility.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('civility-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse('civility-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), CIVILITY_FIELD)
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_civility(self):
        """
        Ensure we can patch an Civility object
        """

        item = Civility.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse('civility-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), CIVILITY_FIELD)
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_civility(self):
        """
        Ensure we can delete an Civility object
        """

        item = Civility.objects.first()

        # Delete this object
        url = reverse('civility-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Civility removed
        url_get = reverse('civility-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
