# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _
# Add nested/related tables
from .item import Item
from .domain_song import DomainSong


class ItemDomainSong(models.Model):
    # Description of the table
    "Relation betwwen Item an DomainSong"

    # List of the fields
    item = models.ForeignKey(Item, verbose_name=_('Item'),
            on_delete=models.CASCADE)
    domain_song = models.ForeignKey(
        DomainSong, verbose_name=_('Genre de la chanson'),
        on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_item_domain_song'
        verbose_name_plural = _('item_domain_songs')
        ordering = []
        unique_together = (('item', 'domain_song'), )
