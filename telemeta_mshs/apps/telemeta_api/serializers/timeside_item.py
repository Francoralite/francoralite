# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

# from ..models.thematic import (
#     Thematic as ThematicModel)


class TimeSideSerializer(serializers.Serializer):
    duration = serializers.CharField(required=False)

    class Meta:
        fields = '__all__'
