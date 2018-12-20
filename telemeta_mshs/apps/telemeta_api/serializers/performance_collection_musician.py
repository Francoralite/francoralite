# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from ..models.performance_collection_musician import (
    PerformanceCollectionMusician as PerformanceCollectionMusicianModel)
from .asymetric_related_field import AsymetricRelatedField
from .performance_collection import PerformanceCollectionSerializer
from .authority import AuthoritySerializer


class PerformanceCollectionMusicianSerializer(serializers.ModelSerializer):
    performance_collection = AsymetricRelatedField.from_serializer(
        PerformanceCollectionSerializer, kwargs={'required': True})
    musician = AsymetricRelatedField.from_serializer(
        AuthoritySerializer, kwargs={'required': True})

    class Meta:
        model = PerformanceCollectionMusicianModel
        fields = '__all__'
