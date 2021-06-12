# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .collection import CollectionSerializer
from .language import LanguageSerializer
from .asymetric_related_field import AsymetricRelatedField

from ..models.collection_language import (
    CollectionLanguage as CollectionLanguageModel)


class CollectionLanguageSerializer(serializers.ModelSerializer):
    """
    Common serializer for all CollectionLanguage actions
    """

    # Fields of the serializer
    collection = AsymetricRelatedField.from_serializer(
        CollectionSerializer, kwargs={'required': True})
    language = AsymetricRelatedField.from_serializer(
        LanguageSerializer, kwargs={'required': True})

    class Meta:
        model = CollectionLanguageModel
        fields = '__all__'
    # TODO : use it with with a complete create
    # def create(self, validated_data):
    #     """
    #     Overriding the default create method of the Model serializer.
    #     :param validated_data: data containing all the details
    #            of CollectionLanguage
    #     :return: returns a successfully created ext_collection record
    #     """
    #
    #     # Add nested/related data
    #     collection_data = validated_data.pop('collection')
    #     # Create an oject Mediacollection with the data converted in dict
    #     collection = CollectionModel.objects.create(**collection_data)
    #
    #     language_data = validated_data.pop('language')
    #     # Create an oject language (Language) with the data converted in dict
    #     language = LanguageModel.objects.create(**language_data)
    #
    #     # Create an oject collection_languages
    #     collection_languages = \
    #         CollectionLanguageModel.objects.create(
    #             collection=collection, language=language, **validated_data)
    #
    #     return collection_languages
