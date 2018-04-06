"""
Institution tests
"""

import pytest
import factory
from django.forms.models import model_to_dict
from django.core.management import call_command
from django.core.urlresolvers import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.institution import InstitutionFactory
from ..models.institution import Institution

# Expected structure for Institution objects
INSTITUTION_STRUCTURE = [
    ('id', int),
    ('name', str),
]

# Expected keys for Institution objects
INSTITUTION_FIELDS = sorted([item[0] for item in INSTITUTION_STRUCTURE])


@pytest.mark.django_db
class TestInstitutionList(APITestCase):
    """
    This class manage all Institution tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """

        call_command('telemeta-setup-enumerations')


    def test_can_get_institution_list(self):
        """
        Ensure Institution objects exists
        """
        #url = reverse('institution-list')
        url = '/institution'

        for idx in range(6):
            data = factory.build(dict, FACTORY_CLASS=InstitutionFactory)
            response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # ORM side
        institutions = Institution.objects.all()
        self.assertEqual(len(institutions), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.json(), list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 6)


    @parameterized.expand(INSTITUTION_STRUCTURE)
    def test_has_valid_institution_values(self, attribute, attribute_type):
        """
        Ensure Institution objects have valid values
        """

        url = reverse('institution-list')
        response = self.client.get(url)

        self.assertIsInstance(response.json(), list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for institution in response.json():
            with self.subTest(institution=institution):
                # Check only expected attributes returned
                self.assertEqual(
                    sorted(institution.keys()), INSTITUTION_FIELDS)

                # Ensure type of each attribute
                self.assertIsInstance(institution[attribute], attribute_type)
                self.assertIsNot(institution[attribute], '')


    def test_get_an_institution(self):
        """
        Ensure we can get an Institution objects using an existing id
        """

        item = Institution.objects.first()
        url = reverse('institution-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), dict)


    def test_create_an_institution(self):
        """
        Ensure we can create an Institution object
        """

        data = factory.build(dict, FACTORY_CLASS=InstitutionFactory)
        url = reverse('institution-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(sorted(response.json().keys()), INSTITUTION_FIELDS)

        url = reverse(
            'institution-detail',
            kwargs={'pk': response.json()['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.json(), dict)


    def test_update_an_institution(self):
        """
        Ensure we can update an Institution object
        """

        item = Institution.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('institution-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).json()

        data['name'] = 'foobar_test_put'
        url = reverse('institution-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(sorted(response.json().keys()), INSTITUTION_FIELDS)
        self.assertEqual(response.json()['name'], 'foobar_test_put')


    def test_patch_an_institution(self):
        """
        Ensure we can patch an Institution object
        """

        item = Institution.objects.first()
        self.assertNotEqual(item.name, 'foobar_test_patch')

        # Update English name
        data = {'name': 'foobar_test_patch'}
        url = reverse('institution-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new name returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(sorted(response.json().keys()), INSTITUTION_FIELDS)
        self.assertEqual(response.json()['name'], 'foobar_test_patch')


    def test_delete_an_institution(self):
        """
        Ensure we can delete an Institution object
        """

        item = Institution.objects.first()

        # Delete this object
        url = reverse('institution-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Institution removed
        url_get = reverse('institution-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
