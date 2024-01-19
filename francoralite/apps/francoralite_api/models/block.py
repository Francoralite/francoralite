# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.utils.translation import gettext_lazy as _
from django.db import models


class Block(models.Model):
    # Description of the table
    "Markdown blocks to customize home page."

    # Enums of the table
    TYPE_CUSTOM_TEXT = None
    TYPE_MAP = 'M'
    TYPE_PARTNERS = 'P'
    TYPE_CHOICES = (
        (TYPE_CUSTOM_TEXT, _('Custom text')),
        (TYPE_MAP, _('Map')),
        (TYPE_PARTNERS, _('Partners')),
    )

    # List of the fields
    type = models.CharField(_('type'), choices=TYPE_CHOICES, max_length=1,
        null=True, blank=False, default=None, unique=True)
    title = models.CharField(_('title'), max_length=255,
        null=False, blank=False, unique=True)
    content = models.TextField(_('content'),
        null=True, blank=True, default=None)
    order = models.PositiveSmallIntegerField(_('order'),
        null=False, blank=False, unique=True)
    show = models.BooleanField(_('show'),
        null=False, blank=False, default=False)

    class Meta():
        app_label = 'francoralite_api'
        db_table = 'block'
        verbose_name_plural = _('blocks')
        ordering = ['order', 'title']

    def __unicode__(self):
        return self.title
