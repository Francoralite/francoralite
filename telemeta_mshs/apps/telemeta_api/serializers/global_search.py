# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from ..models.authority import Authority as AuthorityModel
from .authority import AuthoritySerializer


class GlobalSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorityModel
        fields = ('first_name', 'last_name')

    def to_native(self, obj):
        if isinstance(obj, AuthorityModel):
            serializer = AuthoritySerializer(obj)
        else:
            raise Exception("Not an authority instance!")
        return serializer.data
