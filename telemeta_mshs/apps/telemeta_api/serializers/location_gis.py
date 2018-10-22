# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.location import Location as LocationModel


class LocationGisSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Location GIS actions
    """

    code = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)

    class Meta:
        model = LocationModel
        fields = '__all__'
