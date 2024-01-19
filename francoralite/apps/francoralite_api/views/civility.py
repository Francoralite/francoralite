# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import generics

from ..models.authority import Authority
from ..serializers.core import SimpleSerializer


class CivilityView(generics.ListAPIView):
    serializer_class = SimpleSerializer

    keycloak_scopes = {
        'GET': 'authority:view',
    }

    def get_queryset(self):
        search = self.request.query_params.get('search', None)

        qs = Authority.objects.values_list('civility', flat=True)
        qs = qs.exclude(civility=None).exclude(civility='')

        if search:
            qs = qs.filter(civility__icontains=search)

        qs = qs.order_by('civility').distinct()

        return qs
