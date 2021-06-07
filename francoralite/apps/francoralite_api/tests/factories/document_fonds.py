# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
document_fond factory to execute tests
"""

import factory
from ...models.document_fond import DocumentFond
# Import nested/related factories
from .document import DocumentFactory


class DocumentFondsFactory(DocumentFactory):
    """
    DocumentFonds factory
    """

    class Meta:
        model = DocumentFond
        django_get_or_create = (
            'fond',)

    # Nested/related factories
    fond = factory.SubFactory("francoralite.apps.francoralite_api.tests.factories.fond.FondFactory")
