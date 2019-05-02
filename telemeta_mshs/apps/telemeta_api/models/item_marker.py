# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class ItemMarker(models.Model):
    # Description of the table-
    """
    Store the markers (timecode) of an item's sound
    """

    # List ofe the fields
    item = models.ForeignKey('Item',
                             related_name="marker", verbose_name=_('item'))
    time = models.FloatField()
    title = models.CharField(_('nom'), default="", blank=True, max_length=255)
    date = models.DateTimeField(_('date'), auto_now=True)
    description = models.TextField(_('description'), null=True, blank=True)
    author = models.ForeignKey(User, related_name="api_markers",
                               verbose_name=_('author'),
                               blank=True, null=True)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_marker'
        verbose_name_plural = _('item_markers')
        ordering = []

    def __unicode__(self):
        return self.title
