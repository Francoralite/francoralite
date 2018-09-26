# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from telemeta.models.enum import Enumeration as EnumerationModel


class EnumerationSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Enumeration actions
    """

    value = serializers.CharField(required=True)
    notes = serializers.CharField()

    class Meta:
        model = EnumerationModel
        fields = '__all__'
