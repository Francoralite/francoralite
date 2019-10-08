# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

"""
MediaResource tests
"""

import pytest


from django.core.management import call_command
from rest_framework.test import APITestCase

from .factories.MediaResource import MediaresourceFactory

from .keycloak import get_token


@pytest.mark.django_db
class TestMediaresourceList(APITestCase):
    """
    This class manage all Mediaresource tests
    """

    def test_Resource_Abstract(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self)
        self.client.credentials(
            HTTP_AUTHORIZATION=self.auth_headers["HTTP_AUTHORIZATION"])
        call_command('telemeta-setup-enumerations')

        self.instance = MediaresourceFactory.create()

        self.instance.public_access = "metadata"
        self.assertEqual(self.instance.public_access_label(),
                         "Metadata only")

        self.instance.public_access = "full"
        self.assertEqual(self.instance.public_access_label(),
                         "Sound and metadata")

        self.instance.public_access = "fake"
        self.assertEqual(self.instance.public_access_label(),
                         "Private data")
