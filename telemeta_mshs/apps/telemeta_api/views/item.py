# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import os
import settings
import mimetypes
import datetime
from django.http import Http404


from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from ..models.item import Item as ItemModel
from ..models.item_transcoding_flag import (
    ItemTranscodingFlag as ItemTranscodingFlagModel
)
from ..serializers.item import ItemSerializer
from ..serializers.item_analysis import ItemAnalysisSerializer
import timeside.core
from telemeta.views.core import serve_media
from telemeta.cache import TelemetaCache


class ItemViewSet(viewsets.ModelViewSet):
    """
    Item management
    """
    parser_classes = (MultiPartParser,)
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer

    cache_export = TelemetaCache(settings.TELEMETA_EXPORT_CACHE_DIR)
    MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT')
    CACHE_DIR = os.path.join(MEDIA_ROOT, 'cache')
    cache_data = TelemetaCache(
        getattr(settings, 'TELEMETA_DATA_CACHE_DIR', CACHE_DIR))

    # using the settings parameters
    default_grapher_id = getattr(
         settings, 'TIMESIDE_DEFAULT_GRAPHER_ID', ('waveform_centroid'))
    default_grapher_sizes = getattr(
        settings, 'TIMESIDE_DEFAULT_GRAPHER_SIZES', ['346x130', ])

    graphers = timeside.core.processor.processors(
        timeside.core.api.IGrapher)
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
        graphers_sub = []
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

        default_grapher = self.get_grapher(self.default_grapher_id)
        # grapher : compose the path and filenam for each spectrogram
        for size in self.default_grapher_sizes:
            width = size.split('x')[0]  # extract firt part --> width
            height = size.split('x')[1]  # extract second part --> height
            image_file = '.'.join(
                [item.public_id, self.default_grapher_id, size.replace(
                    'x', '_'), 'png'])
            path = self.cache_data.dir + os.sep + image_file
            graph = default_grapher(width=int(width), height=int(height))
            graphers_sub.append({'graph': graph, 'path': path})
            # Append the process to the pipe
            pipe |= graph

        # For each encoder create a file in the export directory
        for proc_id in encoders_id:
            encoder_cls = timeside.core.get_processor(proc_id)
            mime_type = encoder_cls.mime_type()
            cache_file = str(item.id) + '.' + encoder_cls.file_extension()
            media = self.cache_export.dir + os.sep + cache_file
            encoder = encoder_cls(output=media, overwrite=True)
            encoders_sub.append(encoder)
            pipe |= encoder

        # Execute the pipe
        pipe.run()

        # grapher : write the files
        for grapher in graphers_sub:
            # Add a watermak on the spectrogram
            grapher['graph'].watermark('timeside', opacity=.6, margin=(5, 5))
            # Write/create the PNG file
            f = open(grapher['path'], 'w')
            grapher['graph'].render(grapher['path'])
            f.close()

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

    def get_graphers(self):
        graphers = []
        # FIXME --------
        # user = self.request.user
        # graphers_access = (user.is_staff
        #                    or user.is_superuser
        #                    or user.has_perm('can_run_analysis'))
        graphers_access = True
        for grapher in self.graphers:
            # If not access rights --> got to the next iteration
            if (not graphers_access
                    and grapher.id() not in self.public_graphers):
                continue
            if grapher.id() == self.default_grapher_id:
                graphers.insert(
                    0, {'name': grapher.name(), 'id': grapher.id()})
            elif not hasattr(grapher, '_staging'):
                graphers.append(
                    {'name': grapher.name(), 'id': grapher.id()})
            elif not grapher._staging:
                graphers.append(
                    {'name': grapher.name(), 'id': grapher.id()})
        return graphers

    def get_grapher(self, id):
        for grapher in self.graphers:
            if grapher.id() == id:
                break
        return grapher

    def item_visualize(self, public_id, grapher_id, width, height):
        try:
            width = int(width)
            height = int(height)
        except Exception:
            pass

        if not isinstance(width, int) or not isinstance(height, int):
            size = self.default_grapher_sizes[0]
            width = int(size.split('x')[0])
            height = int(size.split('x')[1])

        item = ItemModel.objects.get(code=public_id)
        mime_type = 'image/png'

        source, source_type = item.get_source()

        grapher = self.get_grapher(grapher_id)

        if grapher.id() != grapher_id:
            raise Http404

        size = str(width) + '_' + str(height)
        image_file = '.'.join([public_id, grapher_id, size, 'png'])

        # FIX waveform grapher name change
        old_image_file = '.'.join([public_id, 'waveform', size, 'png'])
        if 'waveform_centroid' in grapher_id and \
                self.cache_data.exists(old_image_file):
            image_file = old_image_file

        path = self.cache_data.dir + os.sep + image_file
        if not self.cache_data.exists(image_file):
            source, _ = item.get_source()
            if source:
                decoder = timeside.core.get_processor('file_decoder')(source)
                graph = grapher(width=width, height=height)
                (decoder | graph).run()
                graph.watermark('timeside', opacity=.6, margin=(5, 5))
                # f = open(path, 'w')
                graph.render(output=path)
                # f.close()
                self.cache_data.add_file(image_file)

        response = serve_media(path, content_type=mime_type)
        return response

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

    def perform_update(self, serializer):
        instance = serializer.save()
        self.analyze(instance)
