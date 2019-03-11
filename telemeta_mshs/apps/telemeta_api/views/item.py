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
from ..models.item_transcoding_flag import (
    ItemTranscodingFlag as ItemTranscodingFlagModel
)
from ..serializers.item import ItemSerializer
from ..serializers.item_analysis import ItemAnalysisSerializer
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
            analysis = ItemAnalysisSerializer(
                data={
                    'element_type': 'analysis',
                    'item': item.id,
                    'name': 'MIME type',
                    'analyzer_id': 'mime_type',
                    'unit': '',
                    'value': mime_type}
            )
            analysis.is_valid()
            analysis.save()
            analysis = ItemAnalysisSerializer(
                data={
                    'element_type': 'analysis',
                    'item': item.id,
                    'name': 'Size',
                    'analyzer_id': 'size',
                    'unit': '',
                    'value': item.size()}
            )
            analysis.is_valid()
            analysis.save()

        analysis = ItemAnalysisSerializer(
            data={
                'element_type': 'analysis',
                'item': item.id,
                'name': 'Channels',
                'analyzer_id': 'channels',
                'unit': '',
                'value': decoder.input_channels}
        )
        analysis.is_valid()
        analysis.save()
        analysis = ItemAnalysisSerializer(
            data={
                'element_type': 'analysis',
                'item': item.id,
                'name': 'Samplerate',
                'analyzer_id': 'samplerate',
                'unit': 'Hz',
                'value': decoder.input_channels}
        )
        analysis.is_valid()
        analysis.save()
        analysis = ItemAnalysisSerializer(
            data={
                'element_type': 'analysis',
                'item': item.id,
                'name': 'Resolution',
                'analyzer_id': 'resolution',
                'unit': 'bits',
                'value': unicode(decoder.input_width)}
        )
        analysis.is_valid()
        analysis.save()
        analysis = ItemAnalysisSerializer(
            data={
                'element_type': 'analysis',
                'item': item.id,
                'name': 'Duration',
                'analyzer_id': 'duration',
                'unit': 's',
                'value': unicode(datetime.timedelta(
                    0, decoder.input_duration))}
        )
        analysis.is_valid()
        analysis.save()

        for analyzer in analyzers_sub:
            for key in analyzer.results.keys():
                result = analyzer.results[key]
                value = result.data_object.value
                if value.shape[0] == 1:
                    value = value[0]
                analysis = ItemAnalysisSerializer(
                    data={
                        'element_type': 'analysis',
                        'item': item.id,
                        'name': result.name,
                        'analyzer_id': result.id,
                        'unit': result.unit,
                        'value': unicode(value)}
                )
                analysis.is_valid()
                analysis.save()

        for encoder in encoders_sub:
            # Retrieve the transcoded_flag record
            is_transcoded_flag = self.get_is_transcoded_flag(
                item=item, mime_type=mime_type)
            # Boolean value to True : the item is transcoded.
            is_transcoded_flag.value = True
            is_transcoded_flag.save()

        print(decoder.__dict__)
        print(item.__dict__)
        self.mime_type = mime_type

    def get_is_transcoded_flag(self, item, mime_type):
        try:
            # Create a ItemTranscodingFlag record.
            # The item is not transcoded : value=False
            is_transcoded_flag, c = \
                    ItemTranscodingFlagModel.objects.get_or_create(
                        item=item,
                        mime_type=mime_type,
                        defaults={'value': False})
        except ItemTranscodingFlagModel.MultipleObjectsReturned:
            # ... So, the record exists ...
            # Searching related records, corresponding to the mime_type
            flags = ItemTranscodingFlagModel.objects.filter(
                item=item,
                mime_type=mime_type)
            # Value is True if ALL flags.valu are True
            value = all([f.value for f in flags])
            # Use the first ItemTranscodingFlag record
            is_transcoded_flag = flags[0]
            # Set with the new value
            is_transcoded_flag.value = value
            # Save it
            is_transcoded_flag.save()
            # Delete the others records
            for f in flags[1:]:
                f.delete()
        # Return the record with the right values
        return is_transcoded_flag

    """
    Override the create method, to create related records
    """
    def perform_create(self, serializer):
        # Save the serializer -> create an id
        serializer.save()
        # Retrieve the item
        id = serializer.data['id']
        item = ItemModel.objects.get(pk=id)

        # Test if there is a saved item record
        if item:
            # Create many related records, regards to a
            #    related sound in the TimeSide player.
            self.analyze(item)
