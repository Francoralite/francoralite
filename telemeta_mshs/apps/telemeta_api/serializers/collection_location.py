# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

# Add nested/related serializers
from .MediaCollection import MediacollectionSerializer
from .location import LocationSerializer

from ..models.collection_location import(
    CollectionLocation as CollectionLocationModel)

# Add nested/related table
from telemeta.models.collection import MediaCollection as MediacollectionModel
from telemeta.models.location import Location as LocationModel


class CollectionLocationSerializer(serializers.ModelSerializer):
    """
    Common serializer for all CollectionLocation actions
    """

    collection = MediacollectionSerializer(required=True)
    location = LocationSerializer(required=True)

    class Meta:
        model = CollectionLocationModel
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details
               of CollectionLocation
        :return: returns a successfully created ext_collection record
        """

        # Add nested/related data
        collection_data = validated_data.pop('collection')
        # Create an oject Mediacollection with the data converted in dict
        collection = MediacollectionModel.objects.create(**collection_data)

        location_data = validated_data.pop('location')
        # Create an oject location (Location) with the data converted in dict
        location = LocationModel.objects.create(**location_data)

        # Create an oject collection_locations
        collection_locations = \
            CollectionLocationModel.objects.create(
                collection=collection, location=location, **validated_data)

        return collection_locations
