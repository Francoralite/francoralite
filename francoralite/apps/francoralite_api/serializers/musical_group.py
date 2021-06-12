# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.musical_group import (
    MusicalGroup as MusicalGroupModel)


class MusicalGroupSerializer(serializers.ModelSerializer):
    """
    Common serializer for all MusicalGroup actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = MusicalGroupModel
        fields = '__all__'
