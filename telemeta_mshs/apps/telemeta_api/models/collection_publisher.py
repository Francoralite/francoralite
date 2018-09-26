# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta.models.core import ModelCore, ForeignKey, MetaCore
from django.utils.translation import ugettext_lazy as _
from telemeta.models.collection import MediaCollection
# FIXIT : Add nested/related tables
from .authority import Authority


class CollectionPublisher(ModelCore):
    # Description of the table
    "The publishers who produce a media_collection"

    # List of the fields
    collection = ForeignKey(MediaCollection, verbose_name=_('collection'))
    publisher = ForeignKey(Authority, verbose_name=_('publisher'))

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'collection_publisher'
        verbose_name_plural = _('collection_publishers')
        ordering = []
