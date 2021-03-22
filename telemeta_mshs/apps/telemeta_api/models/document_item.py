# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.utils.translation import ugettext_lazy as _
from django.db import models
from .document import Document
from .item import Item


class DocumentItem(Document):
    "Item related document"

    item = models.ForeignKey(
        Item,
        related_name="related_document",
        verbose_name=_('item'),
        on_delete=models.CASCADE
    )

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_document_item'
        verbose_name_plural = _('document')
        ordering = ['item', 'title']
