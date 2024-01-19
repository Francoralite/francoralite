# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import generics

from ..models.collection import Collection
from ..serializers.core import SimpleSerializer


class CulturalAreaView(generics.ListAPIView):
    serializer_class = SimpleSerializer

    keycloak_scopes = {
        'GET': 'collection:view',
    }

    def get_queryset(self):
        search = self.request.query_params.get('search', None)

        qs = Collection.objects.values_list('cultural_area', flat=True)
        qs = qs.exclude(cultural_area=None).exclude(cultural_area='')

        if search:
            qs = qs.filter(cultural_area__icontains=search)

        qs = qs.order_by('cultural_area').distinct()

        return qs
