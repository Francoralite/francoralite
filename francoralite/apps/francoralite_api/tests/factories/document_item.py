# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
document_collection factory to execute tests
"""

import factory
from ...models.document_item import DocumentItem
# Import nested/related factories
from .document import DocumentFactory


class DocumentItemFactory(DocumentFactory):
    """
    DocumentItem factory
    """

    class Meta:
        model = DocumentItem
        django_get_or_create = (
            'item',)

    # Nested/related factories
    item = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.item.ItemFactory")
