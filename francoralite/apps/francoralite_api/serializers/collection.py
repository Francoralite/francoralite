# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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
    alt_title = serializers.CharField(allow_blank=True)
    description = serializers.CharField(allow_blank=True)
    recording_context = serializers.CharField(allow_blank=True)
    recorded_from_year = serializers.CharField(
        allow_blank=True, required=False)
    recorded_to_year = serializers.CharField(allow_blank=True, required=False)
    year_published = serializers.IntegerField(allow_null=True, required=False)
    location_details = serializers.CharField(allow_blank=True)
    cultural_area = serializers.CharField(allow_blank=True)
    language = serializers.CharField(allow_blank=True)
    # publisher_collection = serializers.CharField(required=False)
    booklet_author = serializers.CharField(allow_blank=True)
    metadata_author = serializers.CharField(allow_blank=True)
    code = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CollectionModel.objects.all())]
        )
    code_partner = serializers.CharField(allow_blank=True)
    booklet_description = serializers.CharField(allow_blank=True)
    comment = serializers.CharField(allow_blank=True)
    media_type = AsymetricRelatedField.from_serializer(
         MediaTypeSerializer, kwargs={'required': False})
    physical_items_num = serializers.IntegerField(required=False)
    auto_period_access = serializers.BooleanField(required=False)
    legal_rights = AsymetricRelatedField.from_serializer(
         LegalRightsSerializer, kwargs={'required': False})

    class Meta:
        model = CollectionModel
        fields = '__all__'
