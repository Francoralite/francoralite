# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from ..models.performance_collection import (
    PerformanceCollection as PerformanceCollectionModel)
from .asymetric_related_field import AsymetricRelatedField
from .collection import CollectionSerializer
from .instrument import InstrumentSerializer
from .emit_vox import EmitVoxSerializer


class PerformanceCollectionSerializer(serializers.ModelSerializer):
    collection = AsymetricRelatedField.from_serializer(
        CollectionSerializer, kwargs={'required': False})
    number = serializers.CharField(required=True)
    instrument = AsymetricRelatedField.from_serializer(
        InstrumentSerializer, kwargs={'required': False})
    emit = AsymetricRelatedField.from_serializer(
        EmitVoxSerializer, kwargs={'required': False})

    class Meta:
        model = PerformanceCollectionModel
        fields = '__all__'
