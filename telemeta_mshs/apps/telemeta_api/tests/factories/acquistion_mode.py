# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

"""
acquistion_mode factory to execute tests
"""

import factory
from ...models.acquisition_mode import AcquisitionMode


class AcquisitionModeFactory(factory.django.DjangoModelFactory):
    """
    acquistion_mode factory
    """

    class Meta:
        model = AcquisitionMode

    name = factory.Faker('sentence', nb_words=3)
    notes = factory.Faker('paragraph', nb_sentences=1)
