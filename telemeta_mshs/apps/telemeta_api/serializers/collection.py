# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.collection import Collection as CollectionModel
from .mission import MissionSerializer
from .mediatype import MediaTypeSerializer
from .asymetric_related_field import AsymetricRelatedField


class CollectionSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Collection actions
    """

    title = serializers.CharField(required=True)
    alt_title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    recording_context = serializers.CharField(required=False)
    recorded_from_year = serializers.DateField(required=False)
    recorded_to_year = serializers.DateField(required=False)
    year_published = serializers.IntegerField(required=False)
    public_access = serializers.CharField(required=True)
    mission = AsymetricRelatedField.from_serializer(
         MissionSerializer, kwargs={'required': True})
    code_partner = serializers.CharField(required=False)
    location_details = serializers.CharField(required=False)
    media_type = AsymetricRelatedField.from_serializer(
         MediaTypeSerializer, kwargs={'required': False})

    class Meta:
        model = CollectionModel
        fields = '__all__'
