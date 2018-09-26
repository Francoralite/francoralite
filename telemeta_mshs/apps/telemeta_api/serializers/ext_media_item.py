# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from .media_item import MediaItemSerializer
from ..models.ext_media_item import ExtMediaItem as ExtMediaItemModel
from telemeta.models.item import MediaItem as MediaItemModel


class ExtMediaItemSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ExtMediaItem actions
    """

    media_item = MediaItemSerializer(required=True)
    mshs_alt_title = serializers.CharField(allow_null=True, allow_blank=True)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_timbre = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_timbre_ref = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_timbre_code = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_melody = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_domain = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_domain_song = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_domain_vocal = serializers.CharField(
        allow_null=True, allow_blank=True)
    mshs_domain_music = serializers.CharField(
        allow_null=True, allow_blank=True)
    mshs_domain_tale = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_details = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_function = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_dance = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_dance_details = serializers.CharField(
        allow_null=True, allow_blank=True)
    mshs_deposit_digest = serializers.CharField(
        allow_null=True, allow_blank=True)
    mshs_deposit_thematic = serializers.CharField(
        allow_null=True, allow_blank=True)
    mshs_deposit_names = serializers.CharField(
        allow_null=True, allow_blank=True)
    mshs_deposit_places = serializers.CharField(
        allow_null=True, allow_blank=True)
    mshs_deposit_periods = serializers.CharField(
        allow_null=True, allow_blank=True)
    mshs_text_bool = serializers.BooleanField()
    mshs_text = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_incipit = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_refrain = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_jingle = serializers.CharField(allow_null=True, allow_blank=True)
    mshs_ch_coupe = serializers.StringRelatedField()
    code = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = ExtMediaItemModel
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details
               of ext_media_item
        :return: returns a successfully created ext_media_item record
        """

        item_data = validated_data.pop('media_item')
        # Create an oject Mediaitem with the data converted in dict
        item = MediaItemModel.objects.create(**item_data)
        # Create an oject ExtMediaitem, and add it Mediaitem
        extItem = \
            ExtMediaItemModel.objects.create(
                media_item=item, **validated_data)

        return extItem

    def update(self, instance, validated_data):
        """
        Overriding the default update method of the Model serializer.
        :param validated_data: data containing all the details
               of Ext_media_item
        :return: returns a successfully created ext_item record
        """

        try:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
        except:
            pass

        instance.save()

        return instance
