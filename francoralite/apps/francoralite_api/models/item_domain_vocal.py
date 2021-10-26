# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

# Add nested/related tables
from .item import Item
from .domain_vocal import DomainVocal


class ItemDomainVocal(models.Model):
    # Description of the table
    "Relation betwwen Item an DomainVocal"

    # List of the fields
    domain_vocal = models.ForeignKey(DomainVocal, verbose_name=_(
        'Genre de l\'autre expression vocale'), on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name=_('Item'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_item_domain_vocal'
        verbose_name_plural = _('item_domain_vocals')
        ordering = []
        unique_together = (('item', 'domain_vocal'), )
