# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
Test fake data for RefLaforte
"""

import factory
import pytest

from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.ref_laforte import RefLaforteFactory
from ..models.ref_laforte import RefLaforte

from .keycloak import get_token

# Expected structure for Keyword objects
KEYWORD_STRUCTURE = [
    ("id", int),
    ("number", str),
    ("name", str),
]

# Expected keys for MODEL objects
KEYWORD_FIELDS = sorted([item[0] for item in KEYWORD_STRUCTURE])


@pytest.mark.django_db
class TestRefLaforte(APITestCase):
    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")

        # Create a set of sample data
        RefLaforteFactory.create_batch(6)

    def test_can_list_ref_laforte(self):
        """
        Test that we can list RefLaforte
        """
        url = reverse("ref_laforte-list")

        # ORM side
        ref_lafortes = RefLaforte.objects.all()
        self.assertEqual(ref_lafortes.count(), 6)

        # API side
        response = self.client.get(url)

        # Testing
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(KEYWORD_STRUCTURE)
    def test_has_valid_laforte_values(self, field, expected_type):
        """
        Test that we can list RefLaforte
        """
        url = reverse("ref_laforte-list")
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for item in response.data:
            # Ensure all keys are present
            self.assertEqual(sorted(item.keys()), KEYWORD_FIELDS)

            # Ensure all values have the expected type
            if expected_type is int:
                for item in response.data:
                    self.assertIsInstance(item[field], int)
            elif expected_type is str:
                for item in response.data:
                    self.assertIsInstance(item[field], str)
            self.assertIsNot(item[field], "")

    def test_get_one_ref_laforte(self):
        """
        Test that we can get one RefLaforte
        """
        item = RefLaforte.objects.first()
        url = reverse("ref_laforte-detail", kwargs={"pk": item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_ref_laforte(self):
        """
        Ensure we can create a RefLaforte object
        """

        data = factory.build(dict, FACTORY_CLASS=RefLaforteFactory)
        url = reverse("ref_laforte-list")
        response = self.client.post(url, data, format="json")

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), KEYWORD_FIELDS)

        url = reverse("ref_laforte-detail", kwargs={"pk": response.data["id"]})
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_a_ref_laforte(self):
        """
        Ensure we can update a RefLaforte object
        """
        item = RefLaforte.objects.first()
        self.assertNotEqual(item.number, "foobar_test_put")

        # Get existing object from API
        url = reverse("ref_laforte-detail", kwargs={"pk": item.id})
        data = self.client.get(url).data

        data["number"] = "foobar_test_put"
        url = reverse("ref_laforte-detail", kwargs={"pk": item.id})
        response = self.client.put(url, data, format="json")

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), KEYWORD_FIELDS)

        self.assertEqual(response.data["number"], "foobar_test_put")

    def test_patch_a_ref_laforte(self):
        """
        Ensure we can patch a RefLaforte object
        """
        item = RefLaforte.objects.first()

        self.assertNotEqual(item.number, "foobar_test_patch")

        data = {"number": "foobar_test_patch"}
        url = reverse("ref_laforte-detail", kwargs={"pk": item.id})
        response = self.client.patch(url, data, format="json")

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), KEYWORD_FIELDS)

        self.assertEqual(response.data["number"], "foobar_test_patch")

    def test_delete_a_ref_laforte(self):
        """
        Ensure we can delete a RefLaforte object
        """
        item = RefLaforte.objects.first()
        url = reverse("ref_laforte-detail", kwargs={"pk": item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure object is deleted
        url_get = reverse("ref_laforte-detail", kwargs={"pk": item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
