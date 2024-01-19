# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

"""
ItemLaforte factory to execute tests
"""

import factory
from ...models.item_laforte import ItemLaforte

# import nested/related factories
from .ref_laforte import RefLaforteFactory


class ItemLaforteFactory(factory.django.DjangoModelFactory):
    """
    ItemLaforte factory
    """

    item = factory.SubFactory(
        "francoralite.apps.francoralite_api.tests.factories.item.ItemFactory"
    )
    laforte = factory.SubFactory(RefLaforteFactory)

    class Meta:
        model = ItemLaforte
        django_get_or_create = (
            "item",
            "laforte",
        )
