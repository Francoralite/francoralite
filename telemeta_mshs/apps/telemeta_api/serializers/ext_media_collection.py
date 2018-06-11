# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>
from rest_framework import serializers

from .MediaCollection import MediacollectionSerializer
from ..models.ext_media_collection import(
    ExtMediaCollection as ExtMediaCollectionModel)


class ExtMediacollectionSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ExtMediaCollection actions
    """

    media_collection = MediacollectionSerializer(required=True)
    location_details = serializers.CharField()
    cultural_area = serializers.CharField()
    language = serializers.CharField()

    class Meta:
        model = ExtMediaCollectionModel
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details
               of ext_collection
        :return: returns a successfully created ext_collection record
        """

        collection_data = validated_data.pop('media_collection')
        collection = MediacollectionSerializer.create(
            MediacollectionSerializer(), validated_data=collection_data)

        extCollection, created = \
            ExtMediaCollectionModel.objects.update_or_create(
                media_collection=collection,
                location_details=validated_data.pop('location_details'),
                cultural_area=validated_data.pop('cultural_area'),
                language=validated_data.pop('language'))

        return extCollection

    def update(self, instance, validated_data):
        instance.media_collection = validated_data['media_collection']
        instance.save()

        return instance
