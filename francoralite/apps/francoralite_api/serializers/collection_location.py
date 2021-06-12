# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .collection import CollectionSerializer
from .location_gis import LocationGisSerializer
from .asymetric_related_field import AsymetricRelatedField

from ..models.collection_location import (
    CollectionLocation as CollectionLocationModel)


class CollectionLocationSerializer(serializers.ModelSerializer):
    """
    Common serializer for all CollectionLocation actions
    """

    collection = AsymetricRelatedField.from_serializer(
        CollectionSerializer, kwargs={'required': True})
    location = AsymetricRelatedField.from_serializer(
        LocationGisSerializer, kwargs={'required': True})

    class Meta:
        model = CollectionLocationModel
        fields = '__all__'

    # TODO : use it with with a complete create
    # def create(self, validated_data):
    #     """
    #     Overriding the default create method of the Model serializer.
    #     :param validated_data: data containing all the details
    #            of CollectionLocation
    #     :return: returns a successfully created ext_collection record
    #     """
    #
    #     # Add nested/related data
    #     collection_data = validated_data.pop('collection')
    #     # Create an oject Mediacollection with the data converted in dict
    #     collection = CollectionModel.objects.create(**collection_data)
    #
    #     location_data = validated_data.pop('location')
    #     # Create an oject location (Location) with the data converted in dict
    #     location = LocationModel.objects.create(**location_data)
    #
    #     # Create an oject collection_locations
    #     collection_locations = \
    #         CollectionLocationModel.objects.create(
    #             collection=collection, location=location, **validated_data)
    #
    #     return collection_locations
