# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>
from rest_framework import serializers

from .MediaCollection import MediacollectionSerializer
from ..models.ext_media_collection import(
    ExtMediaCollection as ExtMediaCollectionModel)
from telemeta.models.collection import MediaCollection as MediacollectionModel


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
        # Create an oject Mediacollection with the data converted in dict
        collection = MediacollectionModel.objects.create(**collection_data)
        # Create an oject ExtMediacollection, and add it Mediacollection
        extCollection = \
            ExtMediaCollectionModel.objects.create(
                media_collection=collection, **validated_data)

        return extCollection

    def update(self, instance, validated_data):
        """
        Overriding the default update method of the Model serializer.
        :param validated_data: data containing all the details
               of ext_collection
        :return: returns a successfully created ext_collection record
        """
        collection_id = instance.media_collection.id
        try:
            if(collection_id):
                MediacollectionModel.objects.filter(id=collection_id).update(
                    **validated_data['media_collection'])
        except:
            pass

        # Update the extended fields
        instance.location_details = validated_data.get(
            'location_details', instance.location_details)
        instance.cultural_area = validated_data.get(
            'cultural_area', instance.cultural_area)
        instance.language = validated_data.get(
            'language', instance.language)

        instance.save()

        return instance
