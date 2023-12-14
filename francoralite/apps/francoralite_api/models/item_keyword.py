# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

# Add nested/related tables
from .item import Item
from .keyword import Keyword


class ItemKeyword(models.Model):
    # Description of the table
    "Relation between an item and its keywords"

    # List of the fields
    keyword = models.ForeignKey(Keyword, verbose_name=_(
        'Keyword'), on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name=_('Item'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_item_keyword'
        verbose_name_plural = _('item_keywords')
        ordering = []
        unique_together = (('item', 'keyword'), )
