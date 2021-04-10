# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
document_mission factory to execute tests
"""

import factory
from ...models.document_mission import DocumentMission
# Import nested/related factories
from .document import DocumentFactory


class DocumentMissionFactory(DocumentFactory):
    """
    DocumentMission factory
    """

    class Meta:
        model = DocumentMission
        django_get_or_create = (
            'mission',)

    # Nested/related factories
    mission = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.mission.MissionFactory")
