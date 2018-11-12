# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.collection import Collection as CollectionModel
from .mission import MissionSerializer
from .mediatype import MediaTypeSerializer
from .legal_rights import LegalRightsSerializer
from .asymetric_related_field import AsymetricRelatedField


class CollectionSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Collection actions
    """

    mission = AsymetricRelatedField.from_serializer(
        MissionSerializer, kwargs={'required': True})
    title = serializers.CharField(required=True)
    alt_title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    descriptions = serializers.CharField(required=False)
    recording_context = serializers.CharField(required=False)
    recorded_from_year = serializers.DateField(required=False)
    recorded_to_year = serializers.DateField(required=False)
    year_published = serializers.IntegerField(required=False)
    location_details = serializers.CharField(required=False)
    cultural_area = serializers.CharField(required=False)
    language = serializers.CharField(required=False)
    publisher_collection = serializers.CharField(required=False)
    booklet_author = serializers.CharField(required=False)
    metadata_author = serializers.CharField(required=False)
    public_access = serializers.CharField(required=True)
    code = serializers.CharField(required=True)
    code_partner = serializers.CharField(required=False)
    booklet_description = serializers.CharField(required=False)
    comment = serializers.CharField(required=False)
    media_type = AsymetricRelatedField.from_serializer(
         MediaTypeSerializer, kwargs={'required': False})
    physical_items_num = serializers.IntegerField(required=False)
    auto_period_access = serializers.BooleanField(required=False)
    legal_rights = AsymetricRelatedField.from_serializer(
         LegalRightsSerializer, kwargs={'required': False})
    public_access = serializers.CharField(required=True)

    class Meta:
        model = CollectionModel
        fields = '__all__'
