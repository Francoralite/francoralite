# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.language import Language as LanguageModel


class LanguageSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Language actions
    """

    identifier = serializers.CharField(max_length=3)
    part2B = serializers.CharField(max_length=3, required=False)
    part2T = serializers.CharField(max_length=3, required=False)
    part1 = serializers.CharField(max_length=1, required=False)
    scope = serializers.CharField(max_length=1, required=False)
    type = serializers.CharField(max_length=1, required=False)
    name = serializers.CharField(max_length=255)
    comment = serializers.CharField()

    class Meta:
        model = LanguageModel
        fields = '__all__'
