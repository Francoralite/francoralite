# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

# Add nested/related tables
from .item import Item
from .domain_tale import DomainTale


class ItemDomainTale(models.Model):
    # Description of the table
    "Relation betwwen Item an DomainTale"

    # List of the fields
    domain_tale = models.ForeignKey(DomainTale, verbose_name=_(
        'Genre du conte'), on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name=_('Item'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_domain_tale'
        verbose_name_plural = _('item_domain_tales')
        ordering = []
