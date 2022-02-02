# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import datetime

from rest_framework import generics

from ..models.coupe import Coupe
from ..models.collection import Collection
from ..models.instrument import Instrument
from ..models.item import Item
from ..serializers.advanced_search import AdvancedSearchSerializer


class AdvancedSearchList(generics.ListAPIView):
    serializer_class = AdvancedSearchSerializer

    def get_queryset(self):

        # Initialize data from ORM (-> querysets)
        query_sets = [
            Collection.objects.all(),
            Item.objects.all(),
        ]

        # Filtering ----------------------------------------------------
        filters = (
            (
                'instrument',
                (
                    'performancecollection__collection',
                    'performancecollection__itemperformance__item',
                ),
                Instrument,
            ),
            (
                'location',
                (
                    'collectionlocation__location',
                    'collection__collectionlocation__location',
                ),
                None,
            ),
            (
                'dance',
                (
                    'collection__itemdance__dance',
                    'itemdance__dance',
                ),
                None,
            ),
            (
                'collector',
                (
                    'collectioncollectors__collector',
                    'itemcollector__collector',
                ),
                None,
            ),
            (
                'informer',
                (
                    'collectioninformer__informer',
                    'iteminformer__informer',
                ),
                None,
            ),
            (
                'coupe',
                (
                    'items__collection',
                    'items'
                ),
                Coupe,
            ),
            (
                'refrain', None, None,
            ),
            (
                'incipit', None, None,
            ),
            (
                'timbre', None, None,
            ),
            (
                'timbre_ref', None, None,
            ),
            (
                'usefulness',
                (
                    'collection__itemusefulness__usefulness',
                    'itemusefulness__usefulness'
                ),
                None,
            ),
            (
                'thematic',
                (
                    'collection__itemthematic__thematic',
                    'itemthematic__thematic'
                ),
                None,
            ),
            (
                'domain_music',
                (
                    'collection__itemdomainmusic__domain_music',
                    'itemdomainmusic__domain_music'
                ),
                None,
            ),
            (
                'domain_song',
                (
                    'collection__itemdomainsong__domain_song',
                    'itemdomainsong__domain_song'
                ),
                None,
            ),
            (
                'domain_tale',
                (
                    'collection__itemdomaintale__domain_tale',
                    'itemdomaintale__domain_tale'
                ),
                None,
            ),
            (
                'domain_vocal',
                (
                    'collection__itemdomainvocal__domain_vocal',
                    'itemdomainvocal__domain_vocal'
                ),
                None,
            ),
            (
                'date', None, 'items',
            ),
        )

        or_operators = self.request.query_params.getlist('or_operators', [])

        for name, paths, sub_model in filters:
            values = self.request.query_params.getlist(name, [])
            
            if not values:
                continue
            if name == "refrain":
                # Filtering only on items
                query_sets[0] = Collection.objects.none()
                query_sets[1] = query_sets[1].filter(
                    refrain__icontains=values[0])
                # Only one refrain field, so continue ...
                continue
            if name == "incipit":
                # Filtering only on items
                query_sets[0] = Collection.objects.none()
                query_sets[1] = query_sets[1].filter(
                    incipit__icontains=values[0])
                # Only one incipit field, so continue ...
                continue
            if name == "timbre":
                # Filtering only on items
                query_sets[0] = Collection.objects.none()
                query_sets[1] = query_sets[1].filter(
                    timbre__icontains=values[0])
                # Only one timbre field, so continue ...
                continue
            if name == "timbre_ref":
                # Filtering only on items
                query_sets[0] = Collection.objects.none()
                query_sets[1] = query_sets[1].filter(
                    timbre_ref__icontains=values[0])
                # Only one timbre_ref field, so continue ...
                continue
            if name == "date":
                # Exctract dates
                date_from, date_to = values[0].split('_')
                # There is no date from
                if date_from == "":
                    date_from = "0001-01-01"
                # There is no date to
                if date_to == "":
                    date_to = datetime.date.today()
                
                query_sets[0] = Collection.objects.filter(
                    recorded_from_year__gte=date_from,
                    recorded_to_year__lte=date_to,)
                # Items that are related to collections
                query_sets[1] =  query_sets[1].filter(collection__in=query_sets[0])
                
                continue
            if name in or_operators:
                # Filter : value OR value OR ...
                for index, path in enumerate(paths):
                    if sub_model is not None:
                        # Use a sub-query
                        query_sets[index] = query_sets[index].filter(
                            id__in=sub_model.objects.filter(
                                id__in=values).values_list(path))
                    else:
                        # Use joins
                        query_sets[index] = query_sets[index].filter(
                            **{'%s__in' % path: values})
            else:
                # Filter : value AND value AND ...
                for value in values:
                    for index, path in enumerate(paths):
                        if sub_model is not None:
                            # Use a sub-query
                            query_sets[index] = query_sets[index].filter(
                                id__in=sub_model.objects.filter(
                                    id=value).values_list(path))
                        else:
                            # Use joins
                            query_sets[index] = query_sets[index].filter(
                                **{path: value})
        # ---------------------------------------------------- end filtering

        # Composing results
        all_results = [item for qs in query_sets for item in qs.distinct()]

        return all_results
