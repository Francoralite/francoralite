import pytest
import sys

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

@pytest.mark.django_db
class TestVersions(APITestCase):
    """
    This class tests versions
    """

    def test_get_versions(self):
         url = reverse('versions')
         response = self.client.get(url)

         self.assertEqual(response.status_code, status.HTTP_200_OK)
         self.assertEqual(len(response.data), 3)
         self.assertEqual(len(response.data["git_commit"]), 61)
         self.assertEqual(response.data["python"][0:6], "3.8.12")
         self.assertEqual(response.data["django"], (3,1,14,"final",0) )
