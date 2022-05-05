# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import generics

from ..models.item import Item
from ..serializers.core import SimpleSerializer


class TimbreRefView(generics.ListAPIView):
    serializer_class = SimpleSerializer

    keycloak_scopes = {
        'GET': 'item:view',
    }

    def get_queryset(self):
        search = self.request.query_params.get('search', None)

        qs = Item.objects.values_list('timbre_ref', flat=True)
        qs = qs.exclude(timbre_ref=None).exclude(timbre_ref='')

        if search:
            qs = qs.filter(timbre_ref__icontains=search)

        qs = qs.order_by('timbre_ref').distinct()

        return qs
