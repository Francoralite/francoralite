# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.item_marker import ItemMarker as ItemMarkerModel
from .item import ItemSerializer
from .user import CurrentUserSerializer
from .asymetric_related_field import AsymetricRelatedField


class ItemMarkerSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ItemMarker actions
    """

    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True})
    time = serializers.FloatField()
    title = serializers.CharField(allow_blank=True)
    date = serializers.DateTimeField()
    description = serializers.CharField(allow_blank=True)
    # FIXIT --------------------
    # author = AsymetricRelatedField.from_serializer(
    #      CurrentUserSerializer, kwargs={'required': False})

    class Meta:
        model = ItemMarkerModel
        fields = '__all__'
