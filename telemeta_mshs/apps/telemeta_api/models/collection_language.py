# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta.models.core import ModelCore, ForeignKey, MetaCore
from django.utils.translation import ugettext_lazy as _
from telemeta.models.collection import MediaCollection
# Add nested/related tables
from telemeta.models.language import Language


class CollectionLanguage(ModelCore):
    # Description of the table
    "List of Language_ISO used by a MediaCollection"

    # List of the fields
    collection = ForeignKey(MediaCollection, verbose_name=_('collection'))
    language = ForeignKey(Language, verbose_name=_('language'))

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'collection_language'
        verbose_name_plural = _('collection_languages')
        ordering = []
