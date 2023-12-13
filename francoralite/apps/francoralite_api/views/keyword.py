# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.keyword import Keyword as KeywordModel
from ..serializers.keyword import KeywordSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    """
    Keyword management
    """

    queryset = KeywordModel.objects.all()
    serializer_class = KeywordSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'keyword:view',
        'POST': 'keyword:add',
        'PATCH': 'keyword:update',
        'PUT': 'keyword:update',
        'DELETE': 'keyword:delete',
    }
