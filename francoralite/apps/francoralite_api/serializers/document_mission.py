# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ..models.document_mission import DocumentMission as DocumentMissionModel
from .mission import MissionSerializer
from .document import DocumentSerializer
from .asymetric_related_field import AsymetricRelatedField


class DocumentMissionSerializer(DocumentSerializer):
    """
    Common serializer for all DocumentMission actions
    """
    mission = AsymetricRelatedField.from_serializer(
         MissionSerializer, kwargs={'required': True})

    class Meta:
        model = DocumentMissionModel
        fields = '__all__'
