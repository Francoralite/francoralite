# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from .performance_collection import PerformanceCollection
from .item import Item
from django.utils.translation import ugettext_lazy as _


class ItemPerformanceCollection(models.Model):
    # Description of the table
    "Performance made by some musicians for a collection, used by an item"
    item = models.ForeignKey(Item, verbose_name=_('item'))
    performance_collection = models.ForeignKey(
        PerformanceCollection, verbose_name=_('performance'))

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'item_performance_collection'
        verbose_name_plural = _('interpretes')
        ordering = []
