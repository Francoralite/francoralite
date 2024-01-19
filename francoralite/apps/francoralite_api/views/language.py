# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.language import Language as LanguageModel
from ..serializers.language import LanguageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    """
    Language management
    """

    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'language:view',
        'POST': 'language:add',
        'PATCH': 'language:update',
        'PUT': 'language:update',
        'DELETE': 'language:delete'
    }
