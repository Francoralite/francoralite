# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from telemeta.models.location import Location as LocationModel


class LocationSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Location actions
    """

    name = serializers.CharField(required=True)
    type = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    is_authoritative = serializers.BooleanField()
    current_location = serializers.StringRelatedField()

    class Meta:
        model = LocationModel
        fields = '__all__'
