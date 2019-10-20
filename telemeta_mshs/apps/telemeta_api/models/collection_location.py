# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db import models
from telemeta.models.core import ModelCore, ForeignKey, MetaCore
from django.utils.translation import ugettext_lazy as _
from .collection import Collection
from .location import Location


class CollectionLocation(ModelCore):
    # Description of the table
    "The locations related to a media_collection"

    # List of the fields
    collection = ForeignKey(Collection, verbose_name=_('collection'))
    location = ForeignKey(
        Location, verbose_name=_('location'),
        on_delete=models.PROTECT)

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'collection_location'
        verbose_name_plural = _('collection_locations')
        ordering = []
