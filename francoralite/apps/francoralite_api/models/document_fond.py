# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.utils.translation import gettext_lazy as _
from django.db import models
from .document import Document
from .fond import Fond


class DocumentFond(Document):
    "Fond related document"

    fond = models.ForeignKey(
        Fond,
        related_name="related_document",
        verbose_name=_('fond'),
        on_delete=models.CASCADE
        )

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_document_fond'
        verbose_name_plural = _('document')
        ordering = ['fond', 'title']
