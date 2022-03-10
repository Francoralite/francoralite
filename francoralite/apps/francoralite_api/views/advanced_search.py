# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db import models
from rest_framework import generics
from rest_framework.response import Response

from ..models.authority import Authority
from ..models.coupe import Coupe
from ..models.collection import Collection
from ..models.collection_location import CollectionLocation
from ..models.dance import Dance
from ..models.domain_song import DomainSong
from ..models.domain_music import DomainMusic
from ..models.domain_tale import DomainTale
from ..models.domain_vocal import DomainVocal
from ..models.instrument import Instrument
from ..models.item import Item
from ..models.location import Location
from ..serializers.advanced_search import AdvancedSearchSerializer


class AdvancedSearchList(generics.GenericAPIView):
    serializer_class = AdvancedSearchSerializer

    def get(self, *args, **kwargs):

        # Initialize data from ORM (-> querysets)
        query_sets = [
            Collection.objects.all(),
            Item.objects.all(),
        ]

        # Filtering ----------------------------------------------------
        fields = (
            {
                'name': 'instrument',
                'sub_model': Instrument,
                'paths': (
                    'performancecollection__collection',
                    'performancecollection__itemperformance__item',
                ),
            }, {
                'name': 'location',
                'paths': (
                    'collectionlocation__location',
                    'collection__collectionlocation__location',
                ),
                'parameter_model': Location,
            }, {
                'name': 'dance',
                'paths': (
                    'collection__itemdance__dance',
                    'itemdance__dance',
                ),
                'parameter_model': Dance,
            }, {
                'name': 'collector',
                'paths': (
                    'collectioncollectors__collector',
                    'itemcollector__collector',
                ),
                'parameter_model': Authority,
            }, {
                'name': 'informer',
                'paths': (
                    'collectioninformer__informer',
                    'iteminformer__informer',
                ),
                'parameter_model': Authority,
            }, {
                'name': 'coupe',
                'sub_model': Coupe,
                'paths': ('items__collection', 'items'),
                'parameter_model': Coupe,
            }, {
                'name': 'usefulness',
                'paths': (
                    'collection__itemusefulness__usefulness',
                    'itemusefulness__usefulness'
                ),
            }, {
                'name': 'thematic',
                'paths': (
                    'collection__itemthematic__thematic',
                    'itemthematic__thematic'
                ),
            }, {
                'name': 'domain_music',
                'paths': (
                    'collection__itemdomainmusic__domain_music',
                    'itemdomainmusic__domain_music'
                ),
                'parameter_model': DomainMusic,
            }, {
                'name': 'domain_song',
                'paths': (
                    'collection__itemdomainsong__domain_song',
                    'itemdomainsong__domain_song'
                ),
                'parameter_model': DomainSong,
            }, {
                'name': 'domain_tale',
                'paths': (
                    'collection__itemdomaintale__domain_tale',
                    'itemdomaintale__domain_tale'
                ),
                'parameter_model': DomainTale,
            }, {
                'name': 'domain_vocal',
                'paths': (
                    'collection__itemdomainvocal__domain_vocal',
                    'itemdomainvocal__domain_vocal'
                ),
                'parameter_model': DomainVocal,
            }, {
                'name': 'refrain',
                'paths': (None, 'refrain'),
                'lookups': 'icontains',
            }, {
                'name': 'incipit',
                'paths': (None, 'incipit'),
                'lookups': 'icontains',
            }, {
                'name': 'timbre',
                'paths': (None, 'timbre'),
                'lookups': 'icontains',
            }, {
                'name': 'timbre_ref',
                'paths': (None, 'timbre_ref'),
                'lookups': 'icontains',
            },
        )

        or_operators = self.request.query_params.getlist('or_operators', [])

        for field in fields:
            values = self.request.query_params.getlist(field['name'], [])

            if not values:
                continue

            paths = field['paths']
            sub_model = field.get('sub_model')
            lookups = field.get('lookups')

            if field['name'] in or_operators:
                # Filter : value OR value OR ...
                for index, path in enumerate(paths):
                    if path is None:
                        query_sets[index] = query_sets[index].none()
                    elif lookups:
                        if sub_model:
                            raise NotImplementedError
                        # Use many joins
                        path = '%s__%s' % (path, lookups)
                        sub_filter = models.Q()
                        for value in values:
                            sub_filter |= models.Q(**{path: value})
                        query_sets[index] = query_sets[index].filter(sub_filter)
                    elif sub_model is not None:
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
                        if path is None:
                            query_sets[index] = query_sets[index].none()
                        elif sub_model is not None:
                            # Use a sub-query
                            if lookups:
                                raise NotImplementedError
                            query_sets[index] = query_sets[index].filter(
                                id__in=sub_model.objects.filter(
                                    id=value).values_list(path))
                        else:
                            # Use joins
                            if lookups:
                                path = '%s__%s' % (path, lookups)
                            query_sets[index] = query_sets[index].filter(
                                **{path: value})

        # Special dates filtering
        date_filter = models.Q()
        date_start = self.request.query_params.get('date_start', None)
        date_end = self.request.query_params.get('date_end', None)
        if date_start:
            date_filter &= models.Q(recorded_from_year__gte=date_start)
        if date_end:
            date_filter &= models.Q(recorded_to_year__lte=date_end)
        if date_filter:
            query_sets[0] = query_sets[0].filter(date_filter)
            query_sets[1] = query_sets[1].filter(
                collection__in=Collection.objects.filter(date_filter))
        # ---------------------------------------------------- end filtering

        # Collecting the locations
        locations_qs = CollectionLocation.objects.filter(collection__in=query_sets[0])

        # Building a list of parameter names by model
        parameter_models = {}
        for field in fields:
            model = field.get('parameter_model')
            if model:
                parameter_models.setdefault(model, []).append(field.get('name'))

        # Collecting parameter instances
        parameters = {}
        for model, names in parameter_models.items():
            keys = set(
                key
                for name in names
                for key in self.request.query_params.getlist(name, [])
            )
            if keys:
                serializer = self.get_serializer()
                for instance in model.objects.filter(id__in=keys):
                    serialized = serializer.to_representation(instance)
                    for name in names:
                        if str(instance.id) in self.request.query_params.getlist(name, []):
                            parameters.setdefault(name, []).append(serialized)

        # Composing results
        collections = self.get_serializer(query_sets[0].distinct(), many=True).data
        items = self.get_serializer(query_sets[1].distinct(), many=True).data
        locations = self.get_serializer(locations_qs.distinct(), many=True).data

        # Returning results
        return Response({
            'parameters': parameters,
            'results': {
                'collections': collections,
                'items': items,
                'locations': locations,
            },
        })
