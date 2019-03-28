# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.item_analysis import ItemAnalysis as ItemAnalysisModel
from .item import ItemSerializer
from .asymetric_related_field import AsymetricRelatedField


class ItemAnalysisSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ItemAnalysis actions
    """

    # FIXIT ----
    element_type = serializers.CharField()
    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True})
    analyzer_id = serializers.CharField(required=True)
    name = serializers.CharField()
    value = serializers.CharField()
    unit = serializers.CharField(allow_blank=True)

    class Meta:
        model = ItemAnalysisModel
        fields = '__all__'
