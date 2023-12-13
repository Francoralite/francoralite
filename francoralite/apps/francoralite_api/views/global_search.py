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

    def get_queryset(self):
        limit = 5
        query = self.request.query_params.get('q', None)
        authorities = Authority.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query))[:limit]
        locations = Location.objects.filter(
            Q(name__icontains=query))[:limit]
        fonds = Fond.objects.filter(
            Q(title__icontains=query))[:limit]
        missions = Mission.objects.filter(
            Q(title__icontains=query))[:limit]
        collections = Collection.objects.filter(
            Q(title__icontains=query) |
            Q(alt_title__icontains=query))[:limit]
        items = Item.objects.filter(
            Q(title__icontains=query) |
            Q(alt_title__icontains=query) |
            Q(itemkeyword__keyword__name__icontains=query))[:limit]
        all_results = list(itertools.chain(
            authorities,
            locations,
            fonds,
            missions,
            collections,
            items))
        return all_results
