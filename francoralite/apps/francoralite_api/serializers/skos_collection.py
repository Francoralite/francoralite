# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.skos_collection import SkosCollection as SkosCollectionModel
from .asymetric_related_field import AsymetricRelatedField


class SubSkosCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkosCollectionModel
        fields = '__all__'


class SkosCollectionSerializer(serializers.ModelSerializer):
    """
    Common serializer for all SkosCollection actions
    """

    number = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    uri = serializers.URLField(required=True)
    type = serializers.CharField(required=True)
    collection = AsymetricRelatedField.from_serializer(
        SubSkosCollectionSerializer, kwargs={
            'required': False, 'allow_null': True})

    class Meta:
        model = SkosCollectionModel
        depth = 2
        fields = '__all__'
