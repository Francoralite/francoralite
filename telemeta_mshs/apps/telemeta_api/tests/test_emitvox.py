"""
EmitVox tests
"""

import factory
import pytest
import sys

from django.core.management import call_command
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.emit_vox import EmitVoxFactory
from ..models.emit_vox import EmitVox

from .keycloak import get_token

# Expected structure for Coupe objects
EMITVOX_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for Coupe objects
EMITVOX_FIELD = sorted([item[0] for item in EMITVOX_STRUCTURE])


@pytest.mark.django_db
class TestEmitVoxList(APITestCase):
    """
    This class manage all EmitVox tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        EmitVoxFactory.create_batch(6)

    def test_can_get_emitvox_list(self):
        """
        Ensure EmitVox objects exists
        """
        url = reverse('emit_vox-list')

        # ORM side
        emitvoxes = EmitVox.objects.all()
        self.assertEqual(len(emitvoxes), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(EMITVOX_STRUCTURE)
    def test_has_valid_emitvox_values(self, attribute, attribute_type):
        """
        Ensure EmitVox objects have valid values
        """

        url = reverse('emit_vox-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for coupe in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(coupe.keys()), EMITVOX_FIELD)

            # Ensure type of each attribute
            if attribute_type == str:
                self.assertIsInstance(coupe[attribute], str)
            else:
                self.assertIsInstance(coupe[attribute], attribute_type)
            self.assertIsNot(coupe[attribute], '')

    def test_get_an_emitvox(self):
        """
        Ensure we can get an EmitVox objects using an existing id
        """

        item = EmitVox.objects.first()
        url = reverse('emit_vox-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_emitvox(self):
        """
        Ensure we can create an EmitVox object
        """

        data = factory.build(dict, FACTORY_CLASS=EmitVoxFactory)
        url = reverse('emit_vox-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), EMITVOX_FIELD)

        url = reverse(
            'emit_vox-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_emitvox(self):
        """
        Ensure we can update an EmitVox object
        """

        item = EmitVox.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('emit_vox-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse('emit_vox-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), EMITVOX_FIELD)
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_emitvox(self):
        """
        Ensure we can patch an EmitVox object
        """

        item = EmitVox.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse('emit_vox-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), EMITVOX_FIELD)
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_emitvox(self):
        """
        Ensure we can delete an EmitVox object
        """

        item = EmitVox.objects.first()

        # Delete this object
        url = reverse('emit_vox-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Coupe removed
        url_get = reverse('emit_vox-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
