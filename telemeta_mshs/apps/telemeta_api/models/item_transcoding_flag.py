# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import ugettext_lazy as _


class ItemTranscodingFlag(models.Model):
    # Description of the table
    """
    Store a "flag" if a format has been encoded for an item
    """

    # List of the fields
    item = models.ForeignKey('Item',
                             related_name="trancoded", verbose_name=_('item'))
    mime_type = models.CharField(_('type MIME'), default="", max_length=255)
    date = models.DateTimeField(_('date'), auto_now=True)
    value = models.BooleanField(_(u'Transcodé'))

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_transcoding_flag'
        verbose_name_plural = _('item_transcoding_flags')
        ordering = []

    def __unicode__(self):
        return str(self.mime_type)
