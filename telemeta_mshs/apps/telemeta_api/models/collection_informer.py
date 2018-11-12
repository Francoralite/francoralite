# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta.models.core import ModelCore, ForeignKey, MetaCore
from django.utils.translation import ugettext_lazy as _
from .collection import Collection
from .authority import Authority


class CollectionInformer(ModelCore):
    # Description of the table
    "The informers who produce a media_collection"

    # List of the fields

    collection = ForeignKey(Collection, verbose_name=_('collection'))
    informer = ForeignKey(Authority, verbose_name=_('informer'))

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'collection_informer'
        verbose_name_plural = _('collection_informers')
        ordering = []