# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
Language factory to execute tests
"""

import factory
import factory.fuzzy

from telemeta.models.language import Language


class LanguageFactory(factory.django.DjangoModelFactory):
    """
    Language factory
    """

    class Meta:
        model = Language

    identifier = factory.fuzzy.FuzzyText(length=3)
    part2B = factory.fuzzy.FuzzyText(length=3)
    part2T = factory.fuzzy.FuzzyText(length=3)
    part1 = factory.fuzzy.FuzzyText(length=1)
    scope = factory.fuzzy.FuzzyChoice(['I', 'M', 'S'])
    type = factory.fuzzy.FuzzyChoice(
        ['A', 'C', 'E', 'H', 'M', 'S'])
    name = factory.Faker('word')
    comment = factory.Faker('paragraph', nb_sentences=1)
