# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from ..models.skos_concept import SkosConcept as SkosConceptModel
from ..serializers.skos_concept import SkosConceptSerializer


class SkosConceptViewSet(viewsets.ReadOnlyModelViewSet):
    """
    SkosConcept management
    """

    queryset = SkosConceptModel.objects.all()
    serializer_class = SkosConceptSerializer

    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('collection', 'number')
    ordering = ('name', 'number', 'collection')
    search_fields = ('name', 'number', 'uri', 'abstract')

    keycloak_scopes = {
        'GET': 'skos_concept:view',
    }
