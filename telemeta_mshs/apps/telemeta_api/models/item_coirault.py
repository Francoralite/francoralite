# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _

from .item import Item
from .skos_concept import SkosConcept


class ItemCoirault(models.Model):
    # Description of the table
    "Table of relation between Item and Coirault"

    # List of the fields
    item = models.ForeignKey(Item, verbose_name=_('item'),
            on_delete=models.CASCADE)
    coirault = models.ForeignKey(SkosConcept, verbose_name=_('Coirault'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_coirault'
        verbose_name_plural = _('item_coiraults')
        ordering = []
