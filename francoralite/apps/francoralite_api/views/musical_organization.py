# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.musical_organization import (
    MusicalOrganization as MusicalOrganizationModel)
from ..serializers.musical_organization import MusicalOrganizationSerializer


class MusicalOrganizationViewSet(viewsets.ModelViewSet):
    """
    MusicalOrganization management
    """

    queryset = MusicalOrganizationModel.objects.all()
    serializer_class = MusicalOrganizationSerializer

    keycloak_scopes = {
        'GET': 'musical_organization:view',
        'POST': 'musical_organization:add',
        'PATCH': 'musical_organization:update',
        'PUT': 'musical_organization:update',
        'DELETE': 'musical_organization:delete'
    }
