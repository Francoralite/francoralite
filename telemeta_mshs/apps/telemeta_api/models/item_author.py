# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

from .item import Item
from .authority import Authority


class ItemAuthor(models.Model):
    # Description of the table
    "Authors of an item"

    # List of the fields
    item = models.ForeignKey(Item, verbose_name=_('item'),
            on_delete=models.CASCADE)
    author = models.ForeignKey(Authority, verbose_name=_('author'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_author'
        verbose_name_plural = _('item_authors')
        ordering = []
