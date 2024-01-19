# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models.ref_laforte import RefLaforte as RefLaforteModel


class RefLaforteSerializer(serializers.ModelSerializer):
    """
    Common serializer for all RefLaforte actions
    """

    number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=RefLaforteModel.objects.all())]
    )
    name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = RefLaforteModel
        fields = "__all__"
