# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ..models.document_fond import DocumentFond as DocumentFondModel
from .fond import FondSerializer
from .document import DocumentSerializer
from .asymetric_related_field import AsymetricRelatedField


class DocumentFondSerializer(DocumentSerializer):
    """
    Common serializer for all DocumentFond actions
    """
    mission = AsymetricRelatedField.from_serializer(
         FondSerializer, kwargs={'required': True})

    class Meta:
        model = DocumentFondModel
        fields = '__all__'
