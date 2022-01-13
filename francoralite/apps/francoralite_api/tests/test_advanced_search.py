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

    def _test_informer(self):
        url = "/advancedsearch/?informer=4"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["id"], 1)  # item 1
        self.assertEqual(response.data[2]["id"], 2)  # item 2

    def _test_collector(self):
        url = "/advancedsearch/?collector=8"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], 1)  # item 1
        self.assertEqual(response.data[1]["id"], 2)  # item 2

        url = "/advancedsearch/?collector=6"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], 2)  # collection 2

    def test_location(self):
        url = "/advancedsearch/?location=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 3)  # collection 3
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 1)  # item 1
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 2)  # item 2

    def test_dance(self):
        url = "/advancedsearch/?dance=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 1)  # item 1
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2

        url = "/advancedsearch/?dance=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2

        url = "/advancedsearch/?dance=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_multi_criteria(self):
        """
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 3)  # collection 3
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2

        """
        - instrument : 2 - voix d'homme
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?instrument=2&instrument=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 3)  # collection 3

        """
        - dance : 2 - valse
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?dance=2&instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # Collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2

        """
        - dance : 1 - polka
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?dance=1&instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # Collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2

        """
        - dance : 2 - valse
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?dance=2&instrument=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_multi_criteria_or(self):
        """
        - instrument : 2 - voix d'homme
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?instrument=2&instrument=1&instrument_t=o"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 3)  # collection 3
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2
        
        """
        - dance : 2 - valse
        - dance : 1 - polka
        """
        url = "/advancedsearch/?dance=2&dance=1&dance_t=o"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 1)  # item 1
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2
