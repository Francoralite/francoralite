# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.publisher import Publisher as PublisherModel


class PublisherSerializer(serializers.ModelSerializer):
    """
    Common serializer for all publisher actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False)

    class Meta:
        model = PublisherModel
        fields = '__all__'
