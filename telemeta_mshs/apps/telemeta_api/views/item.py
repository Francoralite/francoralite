# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import os
import settings
import mimetypes
import datetime

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from ..models.item import Item as ItemModel
from ..serializers.item import ItemSerializer
from .item_analysis import ItemAnalysisViewSet
import timeside.core
from telemeta.cache import TelemetaCache


class ItemViewSet(viewsets.ModelViewSet):
    """
    Item management
    """
    parser_classes = (MultiPartParser,)
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer

    cache_export = TelemetaCache(settings.TELEMETA_EXPORT_CACHE_DIR)
    decoders = timeside.core.processor.processors(
        timeside.core.api.IDecoder)
    analyzers = timeside.core.processor.processors(
        timeside.core.api.IAnalyzer)
    value_analyzers = timeside.core.processor.processors(
        timeside.core.api.IValueAnalyzer)

    def analyze(self, item):

        # initialize parameters
        mime_type = ''

        # Initialize lists
        encoders_id = ['mp3_encoder']  # list of the encoders
        analyzers_sub = []
        encoders_sub = []

        source = item.get_source()[0]
        decoder = timeside.core.get_processor(
            'file_decoder')(source)
        pipe = decoder

        # Collect the many analyzers come from TimeSide
        for analyzer in self.value_analyzers:
            subpipe = analyzer()
            analyzers_sub.append(subpipe)
            pipe = pipe | subpipe

        # For each encoder create a file in the export directory
        for proc_id in encoders_id:
            encoder_cls = timeside.core.get_processor(proc_id)
            mime_type = encoder_cls.mime_type()
            cache_file = str(item.id) + '.' + encoder_cls.file_extension()
            media = self.cache_export.dir + os.sep + cache_file
            encoder = encoder_cls(output=media, overwrite=True)
            encoders_sub.append(encoder)
            pipe |= encoder

        pipe.run()

        if os.path.exists(source):
            mime_type = mimetypes.guess_type(source)[0]
            print(mime_type)
            analysis = ItemAnalysisViewSet(
                item=item, name='MIME type',
                analyzer_id='mime_type',
                unit='', value=mime_type)
            print(analysis.__dict__.values())
            # analysis.save()
            analysis = ItemAnalysisViewSet(
                item=item, name='Size',
                analyzer_id='size',
                unit='', value=item.size())
            # analysis.save()
            print(analysis.__dict__.values())

        analysis = ItemAnalysisViewSet(
            item=item, name='Channels',
            analyzer_id='channels',
            unit='', value=decoder.input_channels)
        # analysis.save()
        print(analysis.__dict__.values())
        analysis = ItemAnalysisViewSet(
            item=item, name='Samplerate',
            analyzer_id='samplerate', unit='Hz',
            value=unicode(decoder.input_samplerate))
        # analysis.save()
        print(analysis.__dict__.values())
        analysis = ItemAnalysisViewSet(
            item=item, name='Resolution',
            analyzer_id='resolution', unit='bits',
            value=unicode(decoder.input_width))
        # analysis.save()
        print(analysis.__dict__.values())
        analysis = ItemAnalysisViewSet(
            item=item, name='Duration',
            analyzer_id='duration', unit='s',
            value=unicode(datetime.timedelta(
                0, decoder.input_duration)))
        # analysis.save()
        print(analysis.__dict__.values())

        for analyzer in analyzers_sub:
            for key in analyzer.results.keys():
                result = analyzer.results[key]
                value = result.data_object.value
                if value.shape[0] == 1:
                    value = value[0]
                analysis = ItemAnalysisViewSet(
                    item=item, name=result.name,
                    analyzer_id=result.id, unit=result.unit,
                    value=unicode(value))
                # analysis.save()
                print(analysis.__dict__)

        for encoder in encoders_sub:
            is_transcoded_flag = self.get_is_transcoded_flag(
                item=item, mime_type=mime_type)
            is_transcoded_flag.value = True
            # is_transcoded_flag.save()
            print(is_transcoded_flag.__dict__)

        print(decoder.__dict__)

    # def get_is_transcoded_flag(self, item, mime_type):
    #     try:
    #         is_transcoded_flag, c = \
    #             MediaItemTranscodingFlag.objects.get_or_create(
    #             item=item,
    #             mime_type=mime_type,
    #             defaults={'value': False})
    #     except MediaItemTranscodingFlag.MultipleObjectsReturned:
    #         flags = MediaItemTranscodingFlag.objects.filter(
    #             item=item,
    #             mime_type=mime_type)
    #         value = all([f.value for f in flags])
    #         is_transcoded_flag = flags[0]
    #         is_transcoded_flag.value = value
    #         is_transcoded_flag.save()
    #         for f in flags[1:]:
    #             f.delete()
    #     return is_transcoded_flag

    """
    Override the create method, to create itemanalysis records
    """
    # def perform_create(self, serializer):
    #     # file_obj = self.validated_data['file']
    #     request = (serializer.context['request'])
    #     file_obj = request.FILES['file']
    #
    #     instance = serializer.save()
    #     raise Exception(instance)
    #     serializer.data['file'].save(file_obj.name, file_obj)
    #
    #     # Test if there is a file
    #     if file_obj:
    #
    #         # initialyze parameters
    #         encoders_id = ['mp3_encoder']
    #         mime_type = ''
    #
    #         # Initialize lists
    #         analyzers_sub = []
    #         encoders_sub = []
    #
    #         self.analyze(request)
    #
    #
    #     self.mime_type = mime_type
