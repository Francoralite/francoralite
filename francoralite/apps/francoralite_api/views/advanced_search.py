# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import itertools
from rest_framework import generics

from ..models.collection import Collection
from ..models.instrument import Instrument
from ..models.item import Item
from ..serializers.advanced_search import AdvancedSearchSerializer


class AdvancedSearchList(generics.ListAPIView):
    serializer_class = AdvancedSearchSerializer

    def get_queryset(self):

        # Initialize data from ORM (-> querysets)
        collections_qs = Collection.objects.all()
        items_qs = Item.objects.all()

        # Requeted ------------------------------------------------------
        instruments = self.request.query_params.getlist("instrument", [])
        dances = self.request.query_params.getlist("dance", [])
        locations = self.request.query_params.getlist("location", [])
        # ---------------------------------------------------- end requeted

        # Filtering ----------------------------------------------------
        if instruments:
            # Filter : instrument AND instrument AND ...
            for instrument in instruments:
                collections_qs = collections_qs.filter(id__in=Instrument.objects.filter(
                    id=instrument).values_list('performancecollection__collection'))
                items_qs = items_qs.filter(id__in=Instrument.objects.filter(
                    id=instrument).values_list('performancecollection__itemperformance__item'))

        if locations:
            # Filter : location OR location OR ...
            collections_qs = collections_qs.filter(
                collectionlocation__location__in=locations)
            items_qs = items_qs.filter(
                collection__collectionlocation__location__in=locations)

        if dances:
            # Filter : dance OR dance OR ...
            collections_qs = collections_qs.filter(
                collection__itemdance__dance__in=dances)
            items_qs = items_qs.filter(itemdance__dance__in=dances)
        # ---------------------------------------------------- end filtering

        # Composing results
        all_results = list(itertools.chain(
            set(collections_qs),
            set(items_qs),
        ))

        return all_results
