# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.domain_tale import (
    DomainTale as DomainTaleModel)


class DomainTaleSerializer(serializers.ModelSerializer):
    """
    Common serializer for all DomainTale actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = DomainTaleModel
        fields = '__all__'
