# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from telemeta.models.core import ModelCore, ForeignKey, MetaCore
from django.utils.translation import ugettext_lazy as _
from .collection import Collection
from .authority import Authority


class CollectionCollectors(ModelCore):
    # Description of the table
    "The collectors who collect a media_collection"

    collection = ForeignKey(Collection, verbose_name=_('collection'))
    collector = ForeignKey(Authority, verbose_name=_('collector'))

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'collection_collector'
        verbose_name_plural = _('collection_collectors')
        ordering = []
