# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.utils.translation import gettext_lazy as _
from django.db import models
from .document import Document
from .collection import Collection


class DocumentCollection(Document):
    "Collection related document"

    collection = models.ForeignKey(
        Collection,
        related_name="related_document",
        verbose_name=_('collection'),
        on_delete=models.CASCADE
        )

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_document_collection'
        verbose_name_plural = _('document')
        ordering = ['collection', 'title']
