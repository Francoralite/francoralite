# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from ..models.document_item import (
    DocumentItem as DocumentItemModel)
from .item import ItemSerializer
from .document import DocumentSerializer
from .asymetric_related_field import AsymetricRelatedField


class DocumentItemSerializer(DocumentSerializer):
    """
    Common serializer for all DocumentItem actions
    """
    item = AsymetricRelatedField.from_serializer(
         ItemSerializer, kwargs={'required': True})

    class Meta:
        model = DocumentItemModel
        fields = '__all__'
