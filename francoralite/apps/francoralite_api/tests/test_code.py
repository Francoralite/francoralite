import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.fond import FondFactory

from .keycloak import get_token

@pytest.mark.django_db
class TestCodeList(APITestCase):
    """
    This class manage all Acquisition tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")

        FondFactory.create_batch(300)

    def test_get_codes_external(self):
        response = self.client.get("/api/code_external/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 300)

    def test_get_codes_internal(self):
        response = self.client.get("/api/code_internal/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 300)
