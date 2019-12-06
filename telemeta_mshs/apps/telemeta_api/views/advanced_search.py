# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

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
        limit = 5
        all_results = []

        # Collections --------------------------------
        collections_id = []
        list_coll_entities = [
            ('informer', CollectionInformer),
            ('collector', CollectionCollectors),
            ('location', CollectionLocation),
            ('publisher', CollectionPublisher),
            ('language', CollectionLanguage)
        ]

        # Query collections related
        merge_collection = []
        for l in list_coll_entities:
            entities, coll = self.get_related_entities(
                "collection", l[0], l[1])
            if entities is not None:
                merge_collection.append(coll)

        # Intersection of the values_list
        if len(merge_collection) > 0:
            collections_id = self.getIntersection(merge_collection)

        # Composing the list of collection IDs
        kwargs = {}
        kwargs['id__in'] = [x for x in collections_id]

        # Query collections with the Ids
        collections = Collection.objects.filter(**kwargs)[:limit]

        # Items --------------------------------
        items_id = []
        list_item_entities = [
            ('informer', ItemInformer),
            ('collector', ItemCollector),
            ('dance', ItemDance),
            ('language', ItemLanguage)
        ]

        # Query items related
        merge_item = []
        for l in list_item_entities:
            entities, coll = self.get_related_entities("item", l[0], l[1])
            if entities is not None:
                merge_item.append(coll)

        # Intersection of the values_list
        if len(merge_item) > 0:
            items_id = self.getIntersection(merge_item)

        # Composing the list of item IDs
        kwargs = {}
        kwargs['id__in'] = [x for x in items_id]

        # Query items with the Ids
        items = Item.objects.filter(**kwargs)[:limit]
        import sys
        print '-------- items ---------'
        print items
        print '------------------'
        sys.stdout.flush()

        all_results = list(itertools.chain(
            collections,
            items))
        # all_results["collection"] = list(collections)
        # all_results["item"] = list(items)

        return all_results
