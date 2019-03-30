# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from ..models.item_analysis import ItemAnalysis as ItemAnalysisModel
from ..serializers.item_analysis import ItemAnalysisSerializer


class ItemAnalysisViewSet(viewsets.ModelViewSet):
    """
    ItemAnalysis management
    """

    queryset = ItemAnalysisModel.objects.all()
    serializer_class = ItemAnalysisSerializer

    keycloak_scopes = {
        'GET': 'item_analysis:view',
        'POST': 'item_analysis:add',
        'PATCH': 'item_analysis:update',
        'PUT': 'item_analysis:update',
        'DELETE': 'item_analysis:delete'
    }
