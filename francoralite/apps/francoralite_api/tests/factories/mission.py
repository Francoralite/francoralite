# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Mission factory to execute tests
"""

import factory
from ...models.mission import Mission
from .collection import CollectionItemsFactory


class MissionFactory(factory.django.DjangoModelFactory):
    """
    Mission factory
    """

    class Meta:
        model = Mission

    title = factory.Faker('word')
    description = factory.Faker('word')
    code = factory.Faker('uuid4')
    fonds = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.fond.FondFactory")
    code_partner = factory.Faker('word')
    public_access = factory.Iterator(['metadata', 'full'])


class MissionCollectionFactory(MissionFactory):
    """
    Mission with collections
    """

    @factory.post_generation
    def collections( self, create, extracted, **kwargs):
        if not create: return
        nb_collections = kwargs.get('nb_collections',1)

        for n in range(nb_collections):
            CollectionItemsFactory(mission = self)