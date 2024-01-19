# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Test Coirault
"""

# Context from Class or Interface francoralite/apps/francoralite_api/tests/test_coirault.py:TestCoirault

import factory
import pytest
import sys

from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase


from .keycloak import get_token

from .factories.skos_concept import SkosConceptFactory
from ..models.skos_concept import SkosConcept
from icecream import ic


COIRAULT_STRUCTURE = [
    ("id", int),
    ("number", str),
    ("name", str),
    ("uri", str),
    ("abstract", str),
    ("collection", int),
]

COIRAULT_FIELDS = sorted([item[0] for item in COIRAULT_STRUCTURE])


@pytest.mark.django_db
class TestCoiraultList(APITestCase):
    """
    This class manage all Coirault tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)

        # Create a set of sample data
        SkosConceptFactory.create_batch(6)

    def test_can_get_coirault_list(self):
        """
        Ensure Coirault objects exists
        """
        url = reverse("coirault-list")
        ic(url)

        # ORM side
        coiraults = SkosConcept.objects.all()
        self.assertEqual(len(coiraults), 6)
        ic(coiraults)

        # API side
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 6)
