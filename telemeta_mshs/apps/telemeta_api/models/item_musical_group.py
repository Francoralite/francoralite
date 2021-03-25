# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

# Add nested/related tables
from .item import Item
from .musical_group import MusicalGroup


class ItemMusicalGroup(models.Model):
    # Description of the table
    "Relation between an item and its musical group"

    # List of the fields
    musical_group = models.ForeignKey(MusicalGroup,
                                      verbose_name=_('Fonction'),
                                      on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name=_('Item'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_musical_group'
        verbose_name_plural = _('item_musical_groups')
        ordering = []
