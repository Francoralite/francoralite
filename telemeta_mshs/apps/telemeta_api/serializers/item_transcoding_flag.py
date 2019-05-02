# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.item_transcoding_flag import (
    ItemTranscodingFlag as ItemTranscodingFlagModel)
from .item import ItemSerializer
from .asymetric_related_field import AsymetricRelatedField


class ItemTranscodingFlagSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ItemTranscodingFlag actions
    """

    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True})
    mime_type = serializers.CharField(required=True)
    date = serializers.DateTimeField(required=True)
    value = serializers.BooleanField(required=True)

    class Meta:
        model = ItemTranscodingFlagModel
        fields = '__all__'
