# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models.instrument import Instrument as InstrumentModel
from .asymetric_related_field import AsymetricRelatedField
from .hornbostelsachs import HornbostelSachsSerializer


class InstrumentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=InstrumentModel.objects.all())]
        )
    notes = serializers.CharField(required=False, allow_blank=True)
    typology = AsymetricRelatedField.from_serializer(
        HornbostelSachsSerializer, kwargs={'required': False})

    class Meta:
        model = InstrumentModel
        fields = '__all__'
