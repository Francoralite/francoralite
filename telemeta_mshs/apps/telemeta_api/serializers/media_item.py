# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>
from rest_framework import serializers

# Add nested/related serializers
from .MediaCollection import MediacollectionSerializer
from .location import LocationSerializer
from .language import LanguageSerializer


from telemeta.models.item import MediaItem as MediaItemModel
# Add nested/related table
from telemeta.models.collection import MediaCollection as MediacollectionModel
from telemeta.models.location import Location as LocationModel
from telemeta.models.language import Language as LanguageModel


class MediaItemSerializer(serializers.ModelSerializer):
    """
    Common serializer for all MediaItem actions
    """

    title = serializers.CharField()
    alt_title = serializers.CharField()
    collector = serializers.CharField()
    collection = MediacollectionSerializer(required=True)
    recorded_from_date = serializers.DateField()
    recorded_to_date = serializers.DateField()
    public_access = serializers.CharField()

    location = LocationSerializer()
    location_comment = serializers.CharField()
    cultural_area = serializers.CharField()
    language = serializers.CharField()
    language_iso = LanguageSerializer()

    class Meta:
        model = MediaItemModel
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details
               of MediaItem
        :return: returns a successfully created media_item record
        """

        # Add nested/related data

        collection_data = validated_data.pop('collection')
        # Create an oject Mediacollection with the data converted in dict
        collection = MediacollectionModel.objects.create(**collection_data)

        location_data = validated_data.pop('location')
        # Create an oject Location with the data converted in dict
        location = LocationModel.objects.create(location_data)

        language_data = validated_data.pop('language_iso')
        # Create an oject Language with the data converted in dict
        language_iso = LanguageModel.objects.create(language_data)

        # Create an oject media_item
        media_item = \
            MediaItemModel.objects.create(
                collection=collection,
                location=location,
                language_iso=language_iso,
                **validated_data)

        return media_item
