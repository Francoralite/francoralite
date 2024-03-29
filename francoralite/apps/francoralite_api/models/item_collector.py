# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

from .item import Item
from .authority import Authority


class ItemCollector(models.Model):
    # Description of the table
    "Table of the items"

    # List of the fields
    item = models.ForeignKey(Item, verbose_name=_('item'),
            on_delete=models.CASCADE)
    collector = models.ForeignKey(Authority, verbose_name=_('collector'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_item_collector'
        verbose_name_plural = _('item_collectors')
        ordering = []
        unique_together = (('item', 'collector'), )
