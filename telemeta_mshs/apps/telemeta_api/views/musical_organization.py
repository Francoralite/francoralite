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
