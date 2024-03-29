# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models.fond import Fond as FondModel
from .acquisition_mode import AcquisitionModeSerializer
from .institution import InstitutionSerializer
from .asymetric_related_field import AsymetricRelatedField


class FondSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Fond actions
    """

    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    code = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=FondModel.objects.all())]
        )
    institution = AsymetricRelatedField.from_serializer(
         InstitutionSerializer, kwargs={'required': True})
    code_partner = serializers.CharField(allow_blank=True)
    acquisition_mode = AsymetricRelatedField.from_serializer(
        AcquisitionModeSerializer, kwargs={'required': False})
    conservation_site = serializers.CharField(allow_blank=True)
    comment = serializers.CharField(allow_blank=True)

    missions_count = serializers.IntegerField(required=False, read_only=True)
    collections_count = serializers.IntegerField(required=False, read_only=True)
    items_count = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = FondModel
        fields = '__all__'
