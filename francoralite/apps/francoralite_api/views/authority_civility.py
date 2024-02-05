# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.authority_civility import (
        AuthorityCivility as AuthorityCivilityModel)
from ..serializers.authority_civility import AuthorityCivilitySerializer


class AuthorityCivilityViewSet(viewsets.ModelViewSet):
    """
    AuthorityCivility management
    """

    queryset = AuthorityCivilityModel.objects.all()
    serializer_class = AuthorityCivilitySerializer

    keycloak_scopes = {
        'GET': 'authority_civility:view',
        'POST': 'authority_civility:add',
        'PATCH': 'authority_civility:update',
        'PUT': 'authority_civility:update',
        'DELETE': 'authority_civility:delete'
    }

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = AuthorityCivilityModel.objects.filter(
                authority_id=self.kwargs['authority_pk'])
        return queryset
