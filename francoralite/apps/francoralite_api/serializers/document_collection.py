# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ..models.document_collection import (
    DocumentCollection as DocumentCollectionModel)
from .collection import CollectionSerializer
from .document import DocumentSerializer
from .asymetric_related_field import AsymetricRelatedField


class DocumentCollectionSerializer(DocumentSerializer):
    """
    Common serializer for all DocumentCollection actions
    """
    collection = AsymetricRelatedField.from_serializer(
         CollectionSerializer, kwargs={'required': True})

    class Meta:
        model = DocumentCollectionModel
        fields = '__all__'
