# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db import models
from django.utils.translation import gettext_lazy as _
from .collection import Collection
from .publisher import Publisher


class CollectionPublisher(models.Model):
    # Description of the table
    "The publishers who produce a media_collection"

    # List of the fields
    collection = models.ForeignKey(Collection, verbose_name=_('collection'),
            on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, verbose_name=_('publisher'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'collection_publisher'
        verbose_name_plural = _('collection_publishers')
        ordering = []
