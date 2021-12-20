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
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["id"], 2) # collection 2
        self.assertEqual(response.data[1]["id"], 1) # item 1
        self.assertEqual(response.data[2]["id"], 2) # item 2
        
    def test_collector(self):
        url = "/advancedsearch/?collector=8"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], 1) # item 1
        self.assertEqual(response.data[1]["id"], 2) # item 2
        
        url = "/advancedsearch/?collector=6"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], 2) # collection 2
        
    def test_location(self):
        url = "/advancedsearch/?location=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], 2) # collection 2
        
    def test_dance(self):
        url = "/advancedsearch/?dance=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], 1) # item 1
        self.assertEqual(response.data[1]["id"], 2) # item 2
        
        url = "/advancedsearch/?dance=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], 2) # item 2
        
        url = "/advancedsearch/?dance=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
