# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

from .item import Item
from .ref_laforte import RefLaforte

class ItemLaforte(models.Model):
    # Description of the table
    "Table of relation bertween Item and RefLaforte"

    # List of the fields
    item = models.ForeignKey(Item, verbose_name=_('item'),
            on_delete=models.CASCADE)
    laforte = models.ForeignKey(RefLaforte, verbose_name=_('Laforte'),
            on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_item_laforte'
        verbose_name_plural = _('item_lafortes')
        ordering = []
        unique_together = (('item', 'laforte'), )