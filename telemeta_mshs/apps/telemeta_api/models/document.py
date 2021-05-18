# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.utils.translation import gettext_lazy as _
from django.db import models


class Document(models.Model):
    # Description of the table
    "Related documents to an entity"

    # List of fields
    id_nakala = models.CharField(_('ID Nakala'), max_length=25)
    title = models.CharField(_('titre'), max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    credits = models.TextField(_(u'crédits'), null=True, blank=True)
    date = models.DateTimeField(_('date'), auto_now=True)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_document'
        verbose_name_plural = _('documents')
        ordering = ['title']

    def __unicode__(self):
        return self.title
