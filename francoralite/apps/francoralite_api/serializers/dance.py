# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models.dance import (
    Dance as DanceModel)


class DanceSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Dance actions
    """

    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=DanceModel.objects.all())])
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = DanceModel
        fields = '__all__'
