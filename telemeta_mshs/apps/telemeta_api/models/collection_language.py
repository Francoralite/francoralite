# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db import models
from django.utils.translation import gettext_lazy as _
from .collection import Collection
from .language import Language


class CollectionLanguage(models.Model):
    # Description of the table
    "List of Language_ISO used by a MediaCollection"

    # List of the fields
    collection = models.ForeignKey(Collection, verbose_name=_('collection'),
            on_delete=models.CASCADE)
    language = models.ForeignKey(Language,
                                 verbose_name=_('language'),
                                 on_delete=models.PROTECT)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_collection_language'
        verbose_name_plural = _('collection_languages')
        ordering = []
