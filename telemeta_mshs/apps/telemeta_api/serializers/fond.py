# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.fond import Fond as FondModel
from .acquisition_mode import AcquisitionModeSerializer
from .institution import InstitutionSerializer
from .asymetric_related_field import AsymetricRelatedField


class FondSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Fond actions
    """

    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    descriptions = serializers.CharField(required=False)
    code = serializers.CharField(required=True)
    public_access = serializers.CharField(required=True)
    institution = AsymetricRelatedField.from_serializer(
         InstitutionSerializer, kwargs={'required': True})
    code_partner = serializers.CharField(required=False)
    acquisition_mode = AsymetricRelatedField.from_serializer(
        AcquisitionModeSerializer, kwargs={'required': False})
    conservation_site = serializers.CharField(required=True)
    comment = serializers.CharField(required=False)

    class Meta:
        model = FondModel
        fields = '__all__'
