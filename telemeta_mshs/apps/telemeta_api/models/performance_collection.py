# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from .performance import Performance
from .collection import Collection
from django.utils.translation import gettext_lazy as _


class PerformanceCollection(Performance):
    # Description of the table
    "Performance made by some musicians for a collection"
    collection = models.ForeignKey(Collection, verbose_name=_('collection'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'performance_collection'
        verbose_name_plural = _('interpretes')
        ordering = []
