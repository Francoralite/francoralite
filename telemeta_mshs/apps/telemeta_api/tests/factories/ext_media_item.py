# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ExtMediaItem factory to execute tests
"""

import factory
import uuid
from django.db.models import signals
from ...models.ext_media_item import ExtMediaItem
from .media_item import MediaItemFactory
from .coupe import CoupeFactory


# mute signal, because there's
#  a OneToOneField between MediaItemn and ExtMediaItem
@factory.django.mute_signals(signals.post_save)
class ExtMediaItemFactory(factory.django.DjangoModelFactory):
    """
    ExtMediItem factory
    """

    class Meta:
        model = ExtMediaItem
        django_get_or_create = (
            'media_item', 'code',)

    media_item = factory.SubFactory(MediaItemFactory)
    mshs_alt_title = factory.Faker('word')
    description = factory.Faker('paragraph', nb_sentences=1)
    mshs_timbre = factory.Faker('word')
    mshs_timbre_ref = factory.Faker('word')
    mshs_timbre_code = factory.Faker('word')
    mshs_melody = factory.Faker('paragraph', nb_sentences=3)
    mshs_domain = factory.Faker('word')
    mshs_domain_song = factory.Faker('word')
    mshs_domain_vocal = factory.Faker('word')
    mshs_domain_music = factory.Faker('word')
    mshs_domain_tale = factory.Faker('word')
    mshs_details = factory.Faker('paragraph', nb_sentences=1)
    mshs_function = factory.Faker('word')
    mshs_dance = factory.Faker('word')
    mshs_dance_details = factory.Faker('paragraph', nb_sentences=1)
    mshs_deposit_digest = factory.Faker('paragraph', nb_sentences=2)
    mshs_deposit_thematic = factory.Faker('word')
    mshs_deposit_names = factory.Faker('name')
    mshs_deposit_places = factory.Faker('city')
    mshs_deposit_periods = factory.Faker('word')
    mshs_text_bool = factory.Faker('boolean')
    mshs_text = factory.Faker('paragraph', nb_sentences=2)
    mshs_incipit = factory.Faker('word')
    mshs_refrain = factory.Faker('word')
    mshs_jingle = factory.Faker('word')
    mshs_ch_coupe = factory.SubFactory(CoupeFactory)
    mshs_title_ref_coirault = factory.Faker('word')
    mshs_code_coirault = factory.Faker('word')
    mshs_title_ref_laforte = factory.Faker('word')
    mshs_code_laforte = factory.Faker('word')
    mshs_title_ref_Dela = factory.Faker('word')
    mshs_code_Dela = factory.Faker('word')
    mshs_title_ref_Aare = factory.Faker('word')
    mshs_code_Aare = factory.Faker('word')
    mshs_musical_organization = factory.Faker('word')
    mshs_group = factory.Faker('word')
    code = str(uuid.uuid1())  # factory.Sequence(lambda n: 'code%05d' % n)
