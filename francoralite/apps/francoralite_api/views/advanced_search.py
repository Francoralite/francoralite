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
from ..models.mediatype import MediaType
from ..models.recording_context import RecordingContext
from ..models.skos_concept import SkosConcept
from ..models.thematic import Thematic
from ..models.usefulness import Usefulness
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
                'name': 'code_external',
                'paths': (
                    'code_partner',
                    'code_partner',
                ),
                'lookups': 'icontains',
                'parameter_field': 'code_external_fulltext',
            }, {
                'name': 'code_internal',
                'paths': (
                    'code',
                    'code',
                ),
                'parsers': (
                    lambda code: code[:18],
                    None,
                ),
                'lookups': 'istartswith',
                'parameter_field': 'code_internal_fulltext',
            }, {
                'name': 'coirault',
                'paths': (
                    'collection__itemcoirault__coirault',
                    'itemcoirault__coirault',
                ),
                'parameter_model': SkosConcept,
            }, {
                'name': 'collector',
                'paths': (
                    'collectioncollectors__collector',
                    'itemcollector__collector',
                ),
                'parameter_model': Authority,
            }, {
                'name': 'collector_civility',
                'paths': (
                    'collectioncollectors__collector__civility',
                    'itemcollector__collector__civility',
                ),
                'lookups': 'exact',
                'parameter_model': Authority,
                'parameter_field': 'civility',
            }, {
                'name': 'coupe',
                'sub_model': Coupe,
                'paths': ('items__collection', 'items'),
                'parameter_model': Coupe,
            }, {
                'name': 'cultural_area',
                'paths': (
                    'cultural_area',
                    'collection__cultural_area',
                ),
                'lookups': 'exact',
                'parameter_model': Collection,
                'parameter_field': 'cultural_area',
            }, {
                'name': 'dance',
                'paths': (
                    'collection__itemdance__dance',
                    'itemdance__dance',
                ),
                'parameter_model': Dance,
            }, {
                'name': 'domain_music',
                'paths': (
                    'collection__itemdomainmusic__domain_music',
                    'itemdomainmusic__domain_music',
                ),
                'parameter_model': DomainMusic,
            }, {
                'name': 'domain_song',
                'paths': (
                    'collection__itemdomainsong__domain_song',
                    'itemdomainsong__domain_song',
                ),
                'parameter_model': DomainSong,
            }, {
                'name': 'domain_tale',
                'paths': (
                    'collection__itemdomaintale__domain_tale',
                    'itemdomaintale__domain_tale',
                ),
                'parameter_model': DomainTale,
            }, {
                'name': 'domain_vocal',
                'paths': (
                    'collection__itemdomainvocal__domain_vocal',
                    'itemdomainvocal__domain_vocal',
                ),
                'parameter_model': DomainVocal,
            }, {
                'name': 'incipit',
                'paths': (None, 'incipit'),
                'lookups': 'icontains',
            }, {
                'name': 'informer',
                'paths': (
                    'collectioninformer__informer',
                    'iteminformer__informer',
                ),
                'parameter_model': Authority,
            }, {
                'name': 'informer_civility',
                'paths': (
                    'collectioninformer__informer__civility',
                    'iteminformer__informer__civility',
                ),
                'lookups': 'exact',
                'parameter_model': Authority,
                'parameter_field': 'civility',
            }, {
                'name': 'instrument',
                'sub_model': Instrument,
                'paths': (
                    'performancecollection__collection',
                    'performancecollection__itemperformance__item',
                ),
                'parameter_model': Instrument,
            }, {
                'name': 'jingle',
                'paths': (None, 'jingle'),
                'lookups': 'icontains',
            }, {
                'name': 'location',
                'paths': (
                    'collectionlocation__location',
                    'collection__collectionlocation__location',
                ),
                'parameter_model': Location,
            }, {
                'name': 'media_type',
                'paths': ('media_type', 'media_type'),
                'parameter_model': MediaType,
            }, {
                'name': 'recording_context',
                'paths': ('recording_context', 'collection__recording_context'),
                'parameter_model': RecordingContext,
            }, {
                'name': 'refrain',
                'paths': (None, 'refrain'),
                'lookups': 'icontains',
            }, {
                'name': 'text',
                'paths': (None, 'text'),
                'lookups': 'icontains',
            }, {
                'name': 'thematic',
                'paths': (
                    'collection__itemthematic__thematic',
                    'itemthematic__thematic',
                ),
                'parameter_model': Thematic,
            }, {
                'name': 'timbre',
                'paths': (
                    'collection__timbre',
                    'timbre',
                ),
                'lookups': 'exact',
                'parameter_model': Item,
                'parameter_field': 'timbre',
            }, {
                'name': 'timbre_ref',
                'paths': (
                    'collection__timbre_ref',
                    'timbre_ref',
                ),
                'lookups': 'exact',
                'parameter_model': Item,
                'parameter_field': 'timbre_ref',
            }, {
                'name': 'usefulness',
                'paths': (
                    'collection__itemusefulness__usefulness',
                    'itemusefulness__usefulness',
                ),
                'parameter_model': Usefulness,
            },
        )

        operators = {}

        for field in fields:
            raw_values = self.request.query_params.getlist(field['name'], [])
            operator = (self.request.query_params.get(field['name'] + '_operator', None) or '').lower()

            if not raw_values:
                continue

            paths = field['paths']
            parsers = field.get('parsers')
            sub_model = field.get('sub_model')
            lookups = field.get('lookups')

            if operator in ('or', 'nor'):
                # Filter : value OR value OR ...
                for index, path in enumerate(paths):
                    # Parse values when parser is defined
                    values = filter(None, tuple(
                        parsers[index](value) for value in raw_values
                    ) if parsers and parsers[index] else raw_values)
                    if not values:
                        continue
                    # Add filter to the queryset
                    if path is None:
                        query_sets[index] = query_sets[index].none()
                    else:
                        if lookups:
                            if sub_model:
                                raise NotImplementedError
                            # Use many joins
                            path = '%s__%s' % (path, lookups)
                            sub_filter = models.Q()
                            for value in values:
                                sub_filter |= models.Q(**{path: value})
                        elif sub_model is not None:
                            # Use a sub-query
                            sub_query = sub_model.objects.filter(
                                id__in=values,
                                **{'%s__isnull' % path: False},
                            ).values_list(path)
                            sub_filter = models.Q(id__in=sub_query)
                        else:
                            # Use joins
                            sub_filter = models.Q(**{'%s__in' % path: values})

                        if operator == 'nor':
                            # Invert filter in case of NOR operator
                            sub_filter = ~ sub_filter

                        query_sets[index] = query_sets[index].filter(sub_filter)

            elif operator in ('and', ''):
                operator = 'and'
                # Filter : value AND value AND ...
                for raw_value in raw_values:
                    for index, path in enumerate(paths):
                        # Parse value when parser is defined
                        value = parsers[index](raw_value) \
                            if parsers and parsers[index] else raw_value
                        if not value:
                            continue
                        # Add filter to the queryset
                        if path is None:
                            query_sets[index] = query_sets[index].none()
                        elif sub_model is not None:
                            # Use a sub-query
                            if lookups:
                                raise NotImplementedError
                            sub_query = sub_model.objects.filter(
                                id=value,
                                **{'%s__isnull' % path: False},
                            ).values_list(path)
                            query_sets[index] = query_sets[index].filter(
                                id__in=sub_query,
                            )
                        else:
                            # Use joins
                            if lookups:
                                path = '%s__%s' % (path, lookups)
                            query_sets[index] = query_sets[index].filter(
                                **{path: value})

            else:
                raise NotImplementedError('Opérateur inconnu : ' + operator)

            operators[field['name']] = operator

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

        # Special domains filtering (domain AND domain AND ...)
        domains = self.request.query_params.getlist('domain', None)
        if domains:
            for domain in domains:
                query_sets[0] = query_sets[0].filter(collection__domain__icontains=domain)
                query_sets[1] = query_sets[1].filter(domain__icontains=domain)
        # ---------------------------------------------------- end filtering

        # Collecting the locations
        locations_qs = CollectionLocation.objects.filter(collection__in=query_sets[0])

        # Collecting static parameters
        parameters_instances = {}
        parameters = {
            # autocomplete fields
            'instances': parameters_instances,
            'operators': operators,
            # other fields
            'date_start': date_start,
            'date_end': date_end,
            'domain': domains,
            'incipit': self.request.query_params.get('incipit', None),
            'jingle': self.request.query_params.get('jingle', None),
            'refrain': self.request.query_params.get('refrain', None),
            'text': self.request.query_params.get('text', None),
        }

        # Building a list of parameter names by model and optional field
        parameter_names = {}
        for field in fields:
            parameter_model = field.get('parameter_model')
            parameter_field = field.get('parameter_field')
            if parameter_model or parameter_field:
                parameter_config = parameter_model, parameter_field
                parameter_names.setdefault(parameter_config, []).append(field.get('name'))

        # Collecting parameter instances
        for (model, field), names in parameter_names.items():
            values = set(
                value
                for name in names
                for value in self.request.query_params.getlist(name, [])
            )
            if values:
                # Case of a full text search field from model
                if model and field:
                    values_qs = model.objects.filter(**{'%s__in' % field: values})
                    values_qs = values_qs.values_list(field, flat=True)
                    values_qs = values_qs.order_by(field).distinct()
                    for value in values_qs:
                        for name in names:
                            if value in self.request.query_params.getlist(name, []):
                                parameters_instances.setdefault(name, []).append(value)
                    continue

                # Case of a full text search field from full text
                if field:
                    for name in names:
                        parameters_instances[name] = sorted(set(
                            value for value in values
                            if value in self.request.query_params.getlist(name, [])
                        ))
                    continue

                # Case of an enumeration model
                serializer = self.get_serializer()
                for instance in model.objects.filter(id__in=values):
                    serialized = serializer.to_representation(instance)
                    for name in names:
                        if str(instance.id) in self.request.query_params.getlist(name, []):
                            parameters_instances.setdefault(name, []).append(serialized)

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
