# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from ..models.performance import Performance as PerformanceModel
from .asymetric_related_field import AsymetricRelatedField
from .instrument import InstrumentSerializer
from .emit_vox import EmitVoxSerializer


class PerformanceSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Performance actions
    """

    number = serializers.IntegerField(required=True)
    instrument = AsymetricRelatedField.from_serializer(
        InstrumentSerializer, kwargs={'required': True})
    emit = AsymetricRelatedField.from_serializer(
        EmitVoxSerializer, kwargs={'required': True})

    class Meta:
        model = PerformanceModel
        fields = '__all__'
