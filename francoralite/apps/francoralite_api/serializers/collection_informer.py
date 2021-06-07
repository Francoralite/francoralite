# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .collection import CollectionSerializer
from .authority import AuthoritySerializer
from .asymetric_related_field import AsymetricRelatedField

from ..models.collection_informer import (
    CollectionInformer as CollectionInformerModel)


class CollectionInformerSerializer(serializers.ModelSerializer):
    """
    Common serializer for all CollectionInformer actions
    """

    collection = AsymetricRelatedField.from_serializer(
        CollectionSerializer, kwargs={'required': True})
    informer = AsymetricRelatedField.from_serializer(
        AuthoritySerializer, kwargs={'required': True})

    class Meta:
        model = CollectionInformerModel
        fields = '__all__'

    # TODO : use it with with a complete create
    # def create(self, validated_data):
    #     """
    #     Overriding the default create method of the Model serializer.
    #     :param validated_data: data containing all the details
    #            of CollectionInformer
    #     :return: returns a successfully created ext_collection record
    #     """
    #
    #     collection_data = validated_data.pop('collection')
    #     # Create an oject Mediacollection with the data converted in dict
    #     collection = CollectionModel.objects.create(**collection_data)
    #
    #     informer_data = validated_data.pop('informer')
    #     # Create an oject informer (Authority) with the data converted in dict
    #     informer = AuthorityModel.objects.create(**informer_data)
    #
    #     # Create an oject collection_informers
    #     collection_informers = \
    #         CollectionInformerModel.objects.create(
    #             collection=collection, informer=informer, **validated_data)
    #
    #     return collection_informers
