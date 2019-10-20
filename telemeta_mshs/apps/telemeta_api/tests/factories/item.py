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
from .collection import CollectionFactory
from .mediatype import MediaTypeFactory
from .coupe import CoupeFactory
from ..fake_data.fake_sound import create_tmp_sound


class ItemFactory(factory.django.DjangoModelFactory):
    """
    Item factory
    """
    code = factory.Sequence(lambda n: 'code{0}'.format(n))

    class Meta:
        model = Item

    # FIXIT------------------
    # General -----------
    collection = factory.SubFactory(CollectionFactory)
    title = factory.Faker('word')
    alt_title = factory.Faker('word')
    trans_title = factory.Faker('word')
    description = factory.Faker('paragraph', nb_sentences=5)
    code_partner = factory.Faker('word')
    auto_period_access = factory.Faker('boolean')
    remarks = factory.Faker('paragraph', nb_sentences=5)
    date_edit = factory.LazyFunction(datetime.datetime.now)
    media_type = factory.SubFactory(MediaTypeFactory)
    approx_duration = factory.Faker('time_delta')
    file = create_tmp_sound()  # factory.Faker('file_name', extension="mp3")

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
