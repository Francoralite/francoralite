# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

# Add nested/related tables
from .authority import Authority
from .item import Item


class ItemInformer(models.Model):
    # Description of the table
    "Item's informers"

    # List of the fields
    item = models.ForeignKey(Item, verbose_name=_('XXXXXX'),
            on_delete=models.CASCADE)
    informer = models.ForeignKey(Authority, verbose_name=_('XXXXXX'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_item_informer'
        verbose_name_plural = _('item_informers')
        ordering = []
        unique_together = (('item', 'informer'), )
