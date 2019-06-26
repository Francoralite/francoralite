# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from django.core.management.base import BaseCommand
from django.db import Error
from coirault_skos import skos
from ...models.skos_collection import SkosCollection


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.cpt_chapter = 0
        self.cpt_chapter_updated = 0

    def add_arguments(self, parser):
        parser.add_argument('rdf_file',
                            nargs=1, type=str,
                            help='RDF Coirault file to be import in database')

    def handle(self, *args, **options):
        if options['rdf_file']:
            file_name = options['rdf_file']
            # Create an instance of Skos
            reader = skos.Skos()
            # Read the RDF file to import
            reader.open(file_name=file_name[0])

            # Retrieve every chapter
            chapters = reader.read_chapter()
            for chapter in chapters:
                self.stdout.write('Chapter %s' % chapter["number"])
                # Create or modify a chapter
                self.create_chapter(chapter=chapter)

                # Retrieve every topic
                topics = reader.read_topic(chapter=chapter["uri"])
                for topic in topics:
                    self.stdout.write('\tTopic %s' % topic["number"])

                    # Retrieve every song
                    songs = reader.read_song(topic=topic["uri"])
                    for song in songs:
                        self.stdout.write('.', ending='')

            self.stdout.write('-----------------')
            self.stdout.write('\tChapter')
            self.stdout.write('\t\tcreated = %s' % str(self.cpt_chapter))
            self.stdout.write(
                '\t\tupdated = %s' % str(self.cpt_chapter_updated))
            self.stdout.write('End of Coirault import.')

    def create_chapter(self, chapter):
        try:
            rec, created = SkosCollection.objects.update_or_create(
                name=chapter["name"],
                uri=chapter["uri"],
                number=chapter["number"],
                type="chapter"
            )
            if created is True:
                self.cpt_chapter = self.cpt_chapter + 1
            else:
                self.cpt_chapter_updated = self.cpt_chapter_updated + 1

        except Exception(Error):
            self.stdout.write("Error %s" % Error)
