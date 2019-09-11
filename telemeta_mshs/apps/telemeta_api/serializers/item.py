# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.item import Item as ItemModel
from .collection import CollectionSerializer
from .mediatype import MediaTypeSerializer
from .coupe import CoupeSerializer
from .asymetric_related_field import AsymetricRelatedField


class ItemSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Item actions
    """

    # FIXIT ----
    # General -----------
    collection = AsymetricRelatedField.from_serializer(
        CollectionSerializer, kwargs={'required': True})
    title = serializers.CharField(required=True)
    alt_title = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    trans_title = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    description = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    code = serializers.CharField(required=True)
    code_partner = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    auto_period_access = serializers.BooleanField(required=False)
    remarks = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    date_edit = serializers.DateTimeField(required=False, read_only=True)
    media_type = AsymetricRelatedField.from_serializer(
        MediaTypeSerializer, kwargs={'required': False})
    approx_duration = serializers.DurationField(required=False)
    file = serializers.FileField(max_length=1024, allow_null=True)

    # Description -----------------------
    timbre = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    timbre_ref = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    melody = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)

    # Description / deposit  ---------
    domain = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    deposit_digest = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    deposit_names = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    deposit_places = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    deposit_periods = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)

    # Text ------------------------------
    text_bool = serializers.BooleanField(required=False)
    text = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    incipit = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    refrain = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    jingle = serializers.CharField(
        allow_null=True, allow_blank=True, required=False)
    coupe = AsymetricRelatedField.from_serializer(
         CoupeSerializer, kwargs={'required': False})

    # Text / references -----------------
    #

    class Meta:
        model = ItemModel
        fields = '__all__'
