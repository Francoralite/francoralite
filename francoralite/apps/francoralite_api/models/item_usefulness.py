# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

# Add nested/related tables
from .item import Item
from .usefulness import Usefulness


class ItemUsefulness(models.Model):
    # Description of the table
    "Relation between Item an Usefulness (function of an item)"

    # List of the fields
    usefulness = models.ForeignKey(Usefulness, verbose_name=_(
        'Fonction'), on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name=_('Item'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_item_usefulness'
        verbose_name_plural = _('item_usefulnesses')
        ordering = []
        unique_together = (('item', 'usefulness'), )
