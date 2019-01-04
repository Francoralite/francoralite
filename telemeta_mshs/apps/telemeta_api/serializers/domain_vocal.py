# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.domain_vocal import (
    DomainVocal as DomainVocalModel)


class DomainVocalSerializer(serializers.ModelSerializer):
    """
    Common serializer for all DomainVocal actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False)

    class Meta:
        model = DomainVocalModel
        fields = '__all__'
