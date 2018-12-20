# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers
from ..models.emit_vox import EmitVox as EmitVoxModel


class EmitVoxSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = EmitVoxModel
        fields = '__all__'
