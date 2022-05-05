# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from ..models.domain_vocal import DomainVocal as DomainVocalModel
from ..serializers.domain_vocal import DomainVocalSerializer


class DomainVocalViewSet(viewsets.ModelViewSet):
    """
    DomainVocal management
    """

    queryset = DomainVocalModel.objects.all()
    serializer_class = DomainVocalSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)

    keycloak_scopes = {
        'GET': 'domain_vocal:view',
        'POST': 'domain_vocal:add',
        'PATCH': 'domain_vocal:update',
        'PUT': 'domain_vocal:update',
        'DELETE': 'domain_vocal:delete',
    }
