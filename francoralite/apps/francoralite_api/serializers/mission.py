# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models.mission import Mission as MissionModel
from .fond import FondSerializer
from .asymetric_related_field import AsymetricRelatedField


class MissionSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Mission actions
    """

    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    code = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=MissionModel.objects.all())]
        )
    public_access = serializers.CharField(required=True)
    fonds = AsymetricRelatedField.from_serializer(
         FondSerializer, kwargs={'required': True})
    code_partner = serializers.CharField(allow_blank=True)

    class Meta:
        model = MissionModel
        fields = '__all__'
