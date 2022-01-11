# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from collections import Counter
import itertools
from rest_framework import generics

from ..models.collection import Collection
from ..models.collection_informer import CollectionInformer
from ..models.collectioncollectors import CollectionCollectors
from ..models.collection_location import CollectionLocation
from ..models.collection_publisher import CollectionPublisher
from ..models.collection_language import CollectionLanguage
from ..models.item import Item
from ..models.item_informer import ItemInformer
from ..models.item_collector import ItemCollector
from ..models.item_dance import ItemDance
from ..models.item_language import ItemLanguage
from ..models.item_performance import ItemPerformance
from ..models.performance_collection import PerformanceCollection
from ..serializers.advanced_search import AdvancedSearchSerializer


class AdvancedSearchList(generics.ListAPIView):
    serializer_class = AdvancedSearchSerializer

    def get_related_entities(self, type, entity_name, table):
        result = []
        entities = self.request.query_params.get(entity_name, None)

        if entities is not None:
            value = self.request.query_params[entity_name]
            filter_entity = entity_name + '__exact'
            result = table.objects.select_related('type')\
                .filter(**{filter_entity: value})\
                .values_list(type, flat=True)
        return (entities, result)

    def getIntersection(self, s):
        """ return an intersection from a set of lists """
        i = set(s[0])
        for x in s[1:]:
            i = i & set(x)
        return i

    def get_queryset(self):
        all_results = []

        # Initialize data from ORM
        collections = Collection.objects.all()
        performances_col = PerformanceCollection.objects.all()
        items = Item.objects.all()
        items_ref = Item.objects.all()
        item_performances = ItemPerformance.objects.all()

        # Requeted ------------------------------------------------------
        instruments = self.request.query_params.get("instrument", [])
        dances = self.request.query_params.get("dance", [])
        locations = self.request.query_params.get("location", [])
        # ---------------------------------------------------- end requeted

        # Filtering ----------------------------------------------------
        if instruments:
            for instrument in instruments:
                performances_col = performances_col.filter(
                    instrument=instrument)

        # -- collections --
        if performances_col:
            collections = collections.filter(
                performancecollection__in=performances_col)

        if locations:
            collections = collections.filter(
                collectionlocation__location__in=locations)

        # -- items --
        if performances_col and instruments:
            item_performances = item_performances.filter(
                performance__in=performances_col)
            if item_performances:
                items = items.filter(
                    id__in=item_performances.values_list("item"))
            else:
                items = []

        if dances and items:
            items = items.filter(itemdance__dance__in=dances)
        # ---------------------------------------------------- end filtering

        # Controls : empty for non filtered entities --------------

        searching_item = (True, False)[
            instruments == [] and dances == []
        ]
        searching_collection = (True, False)[
            instruments == [] and locations == [] and dances != []
        ]

        if Counter(Item.objects.all()) == Counter(items) and searching_item == False:
            items = []
        if Counter(Collection.objects.all()) == Counter(collections) or searching_collection == False:
            collections = []

        # -------------------------------------------------------

        # Composing results
        all_results = list(itertools.chain(
            set(collections),
            set(items))
        )

        return all_results
