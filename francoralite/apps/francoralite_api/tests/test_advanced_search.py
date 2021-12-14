import pytest
import sys

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

@pytest.mark.django_db
class TestAdvancedSearch(APITestCase):
    """
    This class tests advanced search
    """
    
    fixtures = ['francoralite.json']

    def test_informer(self):
        url = "/advancedsearch/?informer=4"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], 2) # mission 2
        self.assertEqual(response.data[1]["id"], 2) # item 2
