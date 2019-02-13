# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .asymetric_related_field import AsymetricRelatedField

# Add nested/related serializers
from .item import ItemSerializer
from .domain_music import DomainMusicSerializer

from ..models.item_domain_music import(
    ItemDomainMusic as ItemDomainMusicModel)

# Add nested/related table
from telemeta.models.collection import MediaCollection as MediacollectionModel
from ..models.item_domain_music import ItemDomainMusic as ItemDomainMusicModel


class ItemDomainMusicSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ItemDomainMusic actions
    """

    # fields of the serializer
    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True})
    domain_music = AsymetricRelatedField.from_serializer(
        DomainMusicSerializer, kwargs={'required': True})

    class Meta:
        model = ItemDomainMusicModel
        fields = '__all__'

    # TODO : use it with with a complete create
    # def create(self, validated_data):
    #     """
    #     Overriding the default create method of the Model serializer.
    #     :param validated_data: data containing all the details
    #            of ItemDomainMusic
    #     :return: returns a successfully created ext_collection record
    #     """
    #
    #     # FIXIT : Add nested/related data
    #     collection_data = validated_data.pop('collection')
    #     # Create an oject Mediacollection with the data converted in dict
    #     collection = MediacollectionModel.objects.create(**collection_data)
    #
    #     collector_data = validated_data.pop('collector')
    #     # Create an oject collector (Authority) with the data converted in dict
    #     collector = AuthorityModel.objects.create(**collector_data)
    #
    #     # Create an oject item_domain_musics
    #     item_domain_musics = \
    #         ItemDomainMusicModel.objects.create(
    #             collection=collection, collector=collector, **validated_data)
    #
    #     return item_domain_musics
