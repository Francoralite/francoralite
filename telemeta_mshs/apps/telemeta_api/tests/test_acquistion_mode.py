"""
Coupe tests
"""

import factory
import pytest
import sys

# from django.forms.models import model_to_dict
from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.acquistion_mode import AcquisitionModeFactory
from ..models.acquisition_mode import AcquisitionMode

from .keycloak import get_token

# Expected structure for Coupe objects
ACQUSITION_STRUCTURE = [
    ('id', int),
    ('name', str),
    ('notes', str),
]

# Expected keys for Coupe objects
ACQUISITION_FIELDS = sorted([item[0] for item in ACQUSITION_STRUCTURE])


@pytest.mark.django_db
class TestAcquistionList(APITestCase):
    """
    This class manage all acquisition mode tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])

        AcquisitionModeFactory.create_batch(6)

    def test_can_get_acquisition_list(self):
        """
        Ensure Coupe objects exists
        """
        url = reverse('acquisition_mode-list')

        # ORM side
        acquisitions = AcquisitionMode.objects.all()
        self.assertEqual(len(acquisitions), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(ACQUSITION_STRUCTURE)
    def test_has_valid_acquisition_values(self, attribute, attribute_type):
        """
        Ensure acquisition_mode objects have valid values
        """

        url = reverse('acquisition_mode-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for acquisition_mode in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(acquisition_mode.keys()), ACQUISITION_FIELDS)

            # Ensure type of each attribute
            if attribute_type == str:
                if sys.version_info.major == 2:
                    self.assertIsInstance(
                        acquisition_mode[attribute], basestring)
                else:
                    self.assertIsInstance(
                        acquisition_mode[attribute], str)
            else:
                self.assertIsInstance(
                    acquisition_mode[attribute], attribute_type)
            self.assertIsNot(acquisition_mode[attribute], '')

    def test_get_an_acquisition(self):
        """
        Ensure we can get an acquisition_mode objects using an existing id
        """

        item = AcquisitionMode.objects.first()
        url = reverse('acquisition_mode-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_an_acquisition(self):
        """
        Ensure we can create an acquisition_mode object
        """

        data = factory.build(dict, FACTORY_CLASS=AcquisitionModeFactory)
        url = reverse('acquisition_mode-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), ACQUISITION_FIELDS)

        url = reverse(
            'acquisition_mode-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_an_acquisition(self):
        """
        Ensure we can update an acquisition_mode object
        """

        item = AcquisitionMode.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('acquisition_mode-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['name'] = 'foobar_test_put'
        url = reverse('acquisition_mode-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), ACQUISITION_FIELDS)
        self.assertEqual(response.data['name'], 'foobar_test_put')

    def test_patch_an_acquisition(self):
        """
        Ensure we can patch an acquisition_mode object
        """

        item = AcquisitionMode.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        data = {'name': 'foobar_test_patch'}
        url = reverse('acquisition_mode-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), ACQUISITION_FIELDS)
        self.assertEqual(response.data['name'], 'foobar_test_patch')

    def test_delete_an_acquisition(self):
        """
        Ensure we can delete an acquisition_mode object
        """

        item = AcquisitionMode.objects.first()

        # Delete this object
        url = reverse('acquisition_mode-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure acquistion_mode removed
        url_get = reverse('acquisition_mode-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
