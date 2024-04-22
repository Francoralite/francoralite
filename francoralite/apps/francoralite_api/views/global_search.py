# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import itertools
from django.db.models import Q
from rest_framework import generics

from ..models.authority import Authority
from ..models.location import Location
from ..models.fond import Fond
from ..models.mission import Mission
from ..models.collection import Collection
from ..models.item import Item
from ..serializers.global_search import GlobalSearchSerializer


class GlobalSearchList(generics.ListAPIView):
    serializer_class = GlobalSearchSerializer

    RESULTS_LIMIT = 5

    def get_queryset(self):
        query = self.request.query_params.get('q', None)

        return list(itertools.chain(*(
            model.distinct()[:self.RESULTS_LIMIT]
            for model in (
                Authority.objects.filter(
                    Q(first_name__icontains=query) |
                    Q(last_name__icontains=query)),
                Location.objects.filter(
                    Q(name__icontains=query)),
                Fond.objects.filter(
                    Q(title__icontains=query)),
                Mission.objects.filter(
                    Q(title__icontains=query)),
                Collection.objects.filter(
                    Q(title__icontains=query) |
                    Q(alt_title__icontains=query)),
                Item.objects.filter(
                    Q(title__icontains=query) |
                    Q(alt_title__icontains=query) |
                    Q(text__icontains=query) |  # paroles
                    Q(deposit_digest__icontains=query) |  # résumé
                    Q(itemkeyword__keyword__name__icontains=query)),
            )
        )))
