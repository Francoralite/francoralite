# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from ..models.fond import Fond as FondModel
from ..models.mission import Mission as MissionModel
from ..serializers.fond import FondSerializer


class FondViewSet(viewsets.ModelViewSet):
    """
    Fond management
    """

    queryset = FondModel.objects.all()
    serializer_class = FondSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('institution',)
    # ordering = ('institution', 'code',)
    # search_fields = ('institution__name', 'code', 'title')
    filter_fields = ('code', 'title')

    keycloak_scopes = {
        'GET': 'fond:view',
        'POST': 'fond:add',
        'PATCH': 'fond:update',
        'PUT': 'fond:update',
        'DELETE': 'fond:delete'
    }

    def list_missions(self, id_fonds, field='id'):
        # Retrieve the missions, related to the current fonds
        missions = MissionModel.objects.filter(
            fonds_id=id_fonds).values_list(
                field, flat=True)

        return missions

    @detail_route()
    def dates(self, request, pk=None):
        """
        Determine the max and th min dates from
          the related missions of a fonds
        """
        instance = self.get_object()

        # Retrieve the collections, related to the current fonds

        # Dates (start and end) of list_missions
        from_years = self.list_missions(
            id_fonds=instance.id,
            field='recorded_from_year')
        to_years = self.list_missions(
            id_fonds=instance.id,
            field='recorded_to_year')

        date_start = ""
        date_end = ""
        # Use the min(early) an max(late)
        if len(from_years) >= 1:
            date_start = min(from_years)
        if len(to_years) >= 1:
            date_end = max(to_years)

        return Response((date_start, date_end))
