# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.skos_concept import SkosConcept as SkosConceptModel
from .asymetric_related_field import AsymetricRelatedField
from .skos_collection import SkosCollectionSerializer


class SkosConceptSerializer(serializers.ModelSerializer):
    """
    Common serializer for all SkosConcept actions
    """

    number = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    uri = serializers.URLField(required=True)
    abstract = serializers.CharField(required=False, allow_blank=True)
    collection = AsymetricRelatedField.from_serializer(
        SkosCollectionSerializer, kwargs={'required': False})

    class Meta:
        model = SkosConceptModel
        fields = '__all__'
