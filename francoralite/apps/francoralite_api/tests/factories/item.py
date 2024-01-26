# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Item factory to execute tests
"""

import factory
import factory.fuzzy
import datetime
from ...models.item import Item
from .mediatype import MediaTypeFactory
from .coupe import CoupeFactory
from .performancecollection import PerformanceCollectionFactory
from .performancecollectionmusician import PerformanceCollectionMusicianFactory
from .item_collector import ItemCollectorFactory
from .item_informer import ItemInformerFactory
from .item_author import ItemAuthorFactory
from .item_compositor import ItemCompositorFactory
from .item_dance import ItemDanceFactory
from .item_domain_music import ItemDomainMusicFactory
from .item_domain_song import ItemDomainSongFactory
from .item_domain_tale import ItemDomainTaleFactory
from .item_domain_vocal import ItemDomainVocalFactory
from .item_musical_group import ItemMusicalGroupFactory
from .item_musical_organization import ItemMusicalOrganizationFactory
from .item_thematic import ItemThematicFactory
from .item_usefulness import ItemUsefulnessFactory
from .item_coirault import ItemCoiraultFactory
from .item_laforte import ItemLaforteFactory


from ..fake_data.fake_sound import create_tmp_sound
from django.conf import settings


def format_code_number(n):
    numbers = '{0:0>11}'.format(n)
    return 'TEST_TST_' + '_'.join([numbers[i:i+4] for i in range(0, 11, 4)])


class ItemFactory(factory.django.DjangoModelFactory):
    """
    Item factory
    """

    class Meta:
        model = Item

    # General -----------
    code = factory.Sequence(lambda n: format_code_number(n))
    collection = factory.SubFactory('francoralite.apps.francoralite_api.tests.factories.collection.CollectionFactory')
    title = factory.Faker('word')
    alt_title = factory.Faker('word')
    trans_title = factory.Faker('word')
    description = factory.Faker('paragraph', nb_sentences=5)
    code_partner = factory.Faker('uuid4')
    auto_period_access = factory.Faker('boolean')
    remarks = factory.Faker('paragraph', nb_sentences=5)
    date_edit = factory.LazyFunction(datetime.datetime.now)
    media_type = factory.SubFactory(MediaTypeFactory)
    approx_duration = datetime.timedelta(minutes = 1)
    file = ''
    url_file = factory.Faker('url')

    # Description -----------------------
    timbre = factory.Faker('word')
    timbre_ref = factory.Faker('word')
    melody = factory.Faker('paragraph', nb_sentences=15)

    # Description / deposit  ---------
    # DOMAINS = ('T', 'C', 'A', 'I', 'R')
    domain = factory.fuzzy.FuzzyChoice(['T', 'C', 'A', 'I', 'R'])
    deposit_digest = factory.Faker('paragraph', nb_sentences=5)
    deposit_names = factory.Faker('word')
    deposit_places = factory.Faker('word')
    deposit_periods = factory.Faker('word')

    # Text ------------------------------
    text_bool = factory.Faker('boolean')
    text = factory.Faker('paragraph', nb_sentences=5)
    incipit = factory.Faker('paragraph', nb_sentences=5)
    refrain = factory.Faker('paragraph', nb_sentences=5)
    jingle = factory.Faker('paragraph', nb_sentences=5)
    coupe = factory.SubFactory(CoupeFactory)


class ItemCollectionFactory(ItemFactory):
    @factory.post_generation
    def duration_void( obj, create, extracted, **kwargs):
        """
        ALL items of a collection have their approx_duration to None
        """
        if obj.collection.id == 1 :
            obj.approx_duration = None


class ItemCompleteFactory(ItemFactory):
    """
    Fond factory with missions
    """

    @factory.post_generation
    def performances( self, create, extracted, **kwargs):
        if not create: return
        nb_perfomances = kwargs.get('nb_perfomances',1)

        for n in range(nb_perfomances):
           performance = PerformanceCollectionFactory(collection = self.collection)
           musician = PerformanceCollectionMusicianFactory(performance_collection = performance)

    @factory.post_generation
    def complete( self, create, extracted, **kwargs):
        if not create: return

        ItemCollectorFactory.create_batch(2, item = self)
        ItemInformerFactory.create_batch(3, item = self)
        ItemAuthorFactory.create_batch(1, item = self)
        ItemCompositorFactory.create_batch(1, item = self)
        ItemDanceFactory.create_batch(2, item = self)
        ItemDomainMusicFactory.create_batch(2, item = self)
        ItemDomainSongFactory.create_batch(2, item = self)
        ItemDomainTaleFactory.create_batch(2, item = self)
        ItemDomainVocalFactory.create_batch(2, item = self)
        ItemMusicalGroupFactory.create_batch(2, item = self)
        ItemMusicalOrganizationFactory.create_batch(2, item = self)
        ItemThematicFactory.create_batch(2, item = self)
        ItemUsefulnessFactory.create_batch(2, item = self)
        ItemCoiraultFactory.create_batch(2, item = self)
        ItemLaforteFactory.create_batch(2, item = self)




