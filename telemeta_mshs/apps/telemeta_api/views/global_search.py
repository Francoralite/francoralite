# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import itertools
from django.db.models import Q
from rest_framework import generics

from ..models.authority import Authority
from ..serializers.global_search import GlobalSearchSerializer


class GlobalSearchList(generics.ListAPIView):
    serializer_class = GlobalSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        authorities = Authority.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query))
        all_results = list(itertools.chain(authorities))
        all_results.sort(key=lambda x: x.id)
        return all_results
