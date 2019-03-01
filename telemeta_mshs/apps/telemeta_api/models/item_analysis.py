# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import ugettext_lazy as _


class ItemAnalysis(models.Model):
    # Description of the table
    """
    Store the metadata of an item's sound
    """

    # List of the fields
    element_type = models.CharField(_('type element'),
                                    default='analysis', max_length=255)
    item = models.ForeignKey('Item',
                             related_name="analysis", verbose_name=_('item'))
    analyzer_id = models.CharField(_('id'),
                                   default="", blank=True, max_length=255)
    name = models.CharField(_('nom'), default="", blank=True, max_length=255)
    value = models.CharField(_('valeur'),
                             default="", blank=True, max_length=255)
    unit = models.CharField(_(u'unité'),
                            default="", blank=True, max_length=255)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_analysis'
        verbose_name_plural = _('item_analysises')
        ordering = []

    def __unicode__(self):
        return self.name
