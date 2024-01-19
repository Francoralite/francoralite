# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.metadata_author import MetadataAuthor as MetadataAuthorModel


class MetadataSerializer(serializers.ModelSerializer):
    """
    Common serializer for all metadata author actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = MetadataAuthorModel
        fields = '__all__'
