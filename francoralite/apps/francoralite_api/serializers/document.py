# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.document import Document as DocumentModel


class DocumentSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Document actions
    """
    id_nakala = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    description = serializers.CharField(allow_blank=True)
    credits = serializers.CharField(allow_blank=True)
    date = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = DocumentModel
        fields = '__all__'
