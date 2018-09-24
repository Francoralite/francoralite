# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
MediaItem factory to execute tests
"""

import factory
import uuid
from telemeta.models.item import (
    MediaItem as Mediaitem, ITEM_PUBLIC_ACCESS_CHOICES)

# Import nested/related factories
from .MediaCollection import MediacollectionFactory
from .location import LocationFactory
from .language import LanguageFactory
from .enumeration import (
    EthnicGroupFactory,
    VernacularStyleFactory,
    GenericStyleFactory,
    OrganizationFactory,
    RightsFactory,
    MediatypeFactory,
    TopicFactory
    )


class MediaItemFactory(factory.django.DjangoModelFactory):
    """
    MediaItem factory
    """

    class Meta:
        model = Mediaitem
        django_get_or_create = ('code',)

    title = factory.Faker('word')
    alt_title = factory.Faker('word')
    collector = factory.Faker('word')
    collection = factory.SubFactory(MediacollectionFactory)
    recorded_from_date = factory.Faker('date')
    recorded_to_date = factory.Faker('date')
    public_access = factory.fuzzy.FuzzyChoice(
        ITEM_PUBLIC_ACCESS_CHOICES)
    location = factory.SubFactory(LocationFactory)
    location_comment = factory.Faker('word')
    cultural_area = factory.Faker('word')
    language = factory.Faker('word')
    language_iso = factory.SubFactory(LanguageFactory)
    ethnic_group = factory.SubFactory(EthnicGroupFactory)
    context_comment = factory.Faker('word')
    moda_execut = factory.Faker('word')
    vernacular_style = factory.SubFactory(VernacularStyleFactory)
    generic_style = factory.SubFactory(GenericStyleFactory)
    author = factory.Faker('word')
    organization = factory.SubFactory(OrganizationFactory)
    rights = factory.SubFactory(RightsFactory)
    old_code = factory.Faker('word')
    track = factory.Faker('word')
    collector_selection = factory.Faker('word')
    collector_from_collection = factory.Faker('boolean')
    creator_reference = factory.Faker('word')
    external_references = factory.Faker('paragraph', nb_sentences=1)
    auto_period_access = factory.Faker('boolean')
    comment = factory.Faker('paragraph', nb_sentences=2)
    media_type = factory.SubFactory(MediatypeFactory)
    approx_duration = '00:20:00'
    mimetype = factory.Faker('word')
    file = factory.Faker('file_name')
    url = factory.Faker('url')
    recordist = factory.Faker('word')
    digitalist = factory.Faker('word')
    digitization_date = factory.Faker('date')
    publishing_date = factory.Faker('date')
    scientist = factory.Faker('word')
    topic = factory.SubFactory(TopicFactory)
    summary = factory.Faker('paragraph', nb_sentences=2)
    contributor = factory.Sequence(lambda n: 'code%s' % n)
    code = str(uuid.uuid1())
