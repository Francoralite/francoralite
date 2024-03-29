# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from ..models.item_performance import (
    ItemPerformance as ItemPerformanceModel)
from .asymetric_related_field import AsymetricRelatedField
from .item import ItemSerializer
from .performance_collection import PerformanceCollectionSerializer


class ItemPerformanceSerializer(serializers.ModelSerializer):
    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True})
    performance = AsymetricRelatedField.from_serializer(
        PerformanceCollectionSerializer, kwargs={'required': True})


    class Meta:
        model = ItemPerformanceModel
        fields = '__all__'
