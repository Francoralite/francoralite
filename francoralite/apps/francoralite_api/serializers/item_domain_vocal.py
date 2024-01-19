# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .asymetric_related_field import AsymetricRelatedField

# Add nested/related serializers
from .item import ItemSerializer
from .domain_vocal import DomainVocalSerializer

from ..models.item_domain_vocal import (
    ItemDomainVocal as ItemDomainVocalModel)

# Add nested/related table
# from ..models.domain_vocal import DomainVocal as DomainVocalModel
# from ..models.item import Item as ItemModel


class ItemDomainVocalSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ItemDomainVocal actions
    """

    # fields of the serializer
    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True})
    domain_vocal = AsymetricRelatedField.from_serializer(
        DomainVocalSerializer, kwargs={'required': True})

    class Meta:
        model = ItemDomainVocalModel
        fields = '__all__'

    # TODO : use it with with a complete create
    # def create(self, validated_data):
    #     """
    #     Overriding the default create method of the Model serializer.
    #     :param validated_data: data containing all the details
    #            of ItemDomainVocal
    #     :return: returns a successfully created ext_collection record
    #     """
    #
    #     # FIXIT : Add nested/related data
    #     collection_data = validated_data.pop('collection')
    #     # Create an oject Mediacollection with the data converted in dict
    #     collection = MediacollectionModel.objects.create(**collection_data)
    #
    #     collector_data = validated_data.pop('collector')
    #     # Create an oject collector (Authority) with
    #     #    the data converted in dict
    #     collector = AuthorityModel.objects.create(**collector_data)
    #
    #     # Create an oject item_domain_vocals
    #     item_domain_vocals = \
    #         ItemDomainVocalModel.objects.create(
    #             collection=collection, collector=collector, **validated_data)
    #
    #     return item_domain_vocals
