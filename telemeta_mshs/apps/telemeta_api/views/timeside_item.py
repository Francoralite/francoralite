# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from ..models.item import Item
from ..models.item_analysis import ItemAnalysis
from ..serializers.timeside_item import TimeSideSerializer
from .item import ItemViewSet
import os
import settings
from telemeta.cache import TelemetaCache


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

    # using the settings parameters
    default_grapher_id = getattr(
         settings, 'TIMESIDE_DEFAULT_GRAPHER_ID', ('waveform_centroid'))
    default_grapher_sizes = getattr(
        settings, 'TIMESIDE_DEFAULT_GRAPHER_SIZES', ['346x130', ])
    default_width = int(default_grapher_sizes[0].split('x')[0])
    default_height = int(default_grapher_sizes[0].split('x')[1])

    # Convert a dict to a XML string
    def to_xml(self, dico):
        import xml.etree.ElementTree as ET
        root = ET.Element('telemeta')
        root.tag = 'data'

        for key in dico.keys():
            child = ET.SubElement(root, "data")
            child.set("id", key)
            child.set("name", key)
            child.set("unit", "")
            child.set("value", dico[key])

        return ET.tostring(root, method="xml")

    @detail_route(url_name="timeside-analyze")
    def analyze(self, request, pk=None):
        data = dict()  # data to return

        # try:
        #     # Search an item with the right code field
        #     item = Item.objects.get(pk=pk)
        #     # Extract some data of the item
        #     data['duration'] = str(item.approx_duration)
        #     analyses = ItemAnalysis.objects.all()  # filter(item_id=item.id)
        #
        #     for analysis in analyses:
        #         data[analysis.name] = analysis.value
        # except BaseException:
        #     # Nothing to return
        #     pass
        item = Item.objects.get(pk=pk)
        data['duration'] = str(item.approx_duration)
        # FIXIT -----------------------------------------
        xml = self.to_xml(data)

        # Yeeeeessssssssssssssssss   !!!!!!!!!!!!!!!!!
        return HttpResponse(xml, content_type="application/xml")

    @detail_route()
    def visualize(self, request, pk=None):
        # Parameters to be send to this endpoint
        grapher_id = self.request.query_params.get(
            'grapher_id', self.default_grapher_id)
        width_img = self.request.query_params.get(
            'width', self.default_width)
        height_img = self.request.query_params.get(
            'height', self.default_height)

        data = dict()  # data to return
        data['grapher'] = grapher_id
        data['width'] = width_img
        data['height'] = height_img
        try:
            # Search an item with the right code field
            item = Item.objects.get(pk=pk)
            vs = ItemViewSet()
            vs.item_visualize(
                public_id=item.code,
                grapher_id=grapher_id,
                width=width_img,
                height=height_img)
            data['item'] = str(item.id)
            data['code'] = str(item.code)

        except BaseException:
            # Nothing to return
            pass

        return Response(data)

    @detail_route(
        methods=['get'],
        url_path='soundimage/(?P<grapher>[A-Za-z0-9_.]+)/(?P<width>[0-9]+)x(?P<height>[0-9]+)', # noqa
        url_name='sound_image')
    def sound_image(self, request,
                    pk=None, grapher="", width="", height=""):

        MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
        CACHE_DIR = os.path.join(MEDIA_ROOT, 'cache')
        cache_data = TelemetaCache(
            getattr(settings, 'TELEMETA_DATA_CACHE_DIR', CACHE_DIR))
        # list_file = os.listdir(cache_data.dir)

        item = Item.objects.get(id=pk)
        image = str(cache_data.dir) + '/' + item.code \
            + '.' + grapher + '.' \
            + width + '_' + height + '.png'

        return Response(image)
