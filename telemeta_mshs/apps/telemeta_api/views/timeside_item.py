# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from ..models.item import Item
from ..models.item_analysis import ItemAnalysis
from ..serializers.timeside_item import TimeSideSerializer


class TimeSideViewSet(viewsets.ViewSet):
    """
    Calls for TimeSide's features
    """

    """
    Permet de collecter tous les enregistrements de type Analysis liés à un
     élément item. Ces Analysis sont regroupés dans une liste puis renvoyés
     sous la forme d'un fichier XML.
    Un enregistrement de type *analysis* stocke une ( et une seule) propriété
     de méta-donnée. Ex. : la durée d'un enregistrement.

    Args:
        public_id (type?): public ID of an item

    Returns:
        type: HTTP response with an XML file

    Raises:
        Exception: description

    """
    serializer_class = TimeSideSerializer

    @detail_route()
    def analyze(self, request, pk=None):
        data = dict()  # data to return

        try:
            # Search an item with the right code field
            item = Item.objects.get(code=pk)
            # Extract some data of the item
            data['duration'] = str(item.approx_duration)
            analyses = ItemAnalysis.objects.all()  # filter(item_id=item.id)

            for analysis in analyses:
                data[analysis.name] = analysis.value
        except BaseException:
            # Nothing to return
            pass

        return Response(data)
