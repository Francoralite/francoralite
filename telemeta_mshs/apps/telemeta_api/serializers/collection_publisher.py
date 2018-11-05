# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .collection import CollectionSerializer
from .authority import AuthoritySerializer

from ..models.collection_publisher import (
    CollectionPublisher as CollectionPublisherModel)

# Add nested/related table
from ..models.collection import Collection as CollectionModel
from ..models.authority import Authority as AuthorityModel


class CollectionPublisherSerializer(serializers.ModelSerializer):
    """
    Common serializer for all CollectionPublisher actions
    """

    collection = CollectionSerializer(required=True)
    publisher = AuthoritySerializer(required=True)

    class Meta:
        model = CollectionPublisherModel
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details
               of CollectionPublisher
        :return: returns a successfully created ext_collection record
        """

        # Add nested/related data

        collection_data = validated_data.pop('collection')
        # Create an oject Collection with the data converted in dict
        collection = CollectionModel.objects.create(**collection_data)

        publisher_data = validated_data.pop('publisher')
        # Create an oject publisher (Authority) with the data converted in dict
        publisher = AuthorityModel.objects.create(**publisher_data)

        # Create an oject collection_publishers
        collection_publishers = \
            CollectionPublisherModel.objects.create(
                collection=collection, publisher=publisher, **validated_data)

        return collection_publishers
