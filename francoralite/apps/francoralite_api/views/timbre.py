# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import generics

from ..models.item import Item
from ..serializers.core import SimpleSerializer


class TimbreView(generics.ListAPIView):
    serializer_class = SimpleSerializer

    keycloak_scopes = {
        'GET': 'item:view',
    }

    def get_queryset(self):
        search = self.request.query_params.get('search', None)

        qs = Item.objects.values_list('timbre', flat=True)
        qs = qs.exclude(timbre=None).exclude(timbre='')

        if search:
            qs = qs.filter(timbre__icontains=search)

        qs = qs.order_by('timbre').distinct()

        return qs
