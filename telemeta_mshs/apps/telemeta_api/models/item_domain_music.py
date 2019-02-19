# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import ugettext_lazy as _
from telemeta.models.collection import MediaCollection
# Add nested/related tables
from .item import Item
from .domain_music import DomainMusic

class ItemDomainMusic(models.Model):
    # Description of the table
    "Relation betwwen Item an DomainMusic"

    # List of the fields
    item = models.ForeignKey(Item, verbose_name=_('Item'))
    domain_music = models.ForeignKey(
        DomainMusic, verbose_name=_('Genre de l\'expression instrumentale'))

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_domain_music'
        verbose_name_plural = _('item_domain_musics')
        ordering = []
