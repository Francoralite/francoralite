# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.acquisition_mode import AcquisitionMode as AcquisitionModel


class AcquisitionModeSerializer(serializers.ModelSerializer):
    """
    Common serializer for all acquisition mode actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField()

    class Meta:
        model = AcquisitionModel
        fields = '__all__'
