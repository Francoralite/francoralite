# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models.hornbostelsachs import HornbostelSachs as HornbostelSachsModel

class HornbostelSachsSerializer(serializers.ModelSerializer):
    number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=HornbostelSachsModel.objects.all())])
    name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = HornbostelSachsModel
        fields = '__all__'
