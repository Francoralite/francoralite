# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from django.utils.translation import gettext_lazy as _
from .collection import Collection
from .authority import Authority


class CollectionCollectors(models.Model):
    # Description of the table
    "The collectors who collect a media_collection"

    collection = models.ForeignKey(Collection, verbose_name=_('collection'),
            on_delete=models.CASCADE)
    collector = models.ForeignKey(Authority, verbose_name=_('collector'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'collection_collector'
        verbose_name_plural = _('collection_collectors')
        ordering = []
