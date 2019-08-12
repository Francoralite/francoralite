# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db import models
from telemeta.models.core import ModelCore, ForeignKey, MetaCore
from django.utils.translation import ugettext_lazy as _
from .collection import Collection
from .language import Language


class CollectionLanguage(ModelCore):
    # Description of the table
    "List of Language_ISO used by a MediaCollection"

    # List of the fields
    collection = ForeignKey(Collection, verbose_name=_('collection'))
    language = ForeignKey(Language,
                          verbose_name=_('language'),
                          on_delete=models.PROTECT)

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'collection_language'
        verbose_name_plural = _('collection_languages')
        ordering = []
