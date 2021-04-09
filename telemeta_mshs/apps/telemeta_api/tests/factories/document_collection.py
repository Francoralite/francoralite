# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
document_collection factory to execute tests
"""

import factory
from ...models.document_collection import DocumentCollection
# FIXIT : import nested/related factories
from .item import ItemFactory
from .document import DocumentFactory


class DocumentCollectionFactory(DocumentFactory):
    """
    DocumentCollection factory
    """

    class Meta:
        model = DocumentCollection
        django_get_or_create = (
            'collection',)

    # Nested/related factories
    collection = factory.SubFactory("telemeta_mshs.apps.telemeta_api.tests.factories.collection.CollectionFactory")
