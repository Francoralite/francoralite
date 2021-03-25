# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _
from .performance_collection import PerformanceCollection
from .authority import Authority


class PerformanceCollectionMusician(models.Model):
    # Description of the table
    "The musicians who produce a performance"

    # List of the fields
    performance_collection = models.ForeignKey(
        PerformanceCollection, verbose_name=_('performance'),
        on_delete=models.CASCADE)
    musician = models.ForeignKey(Authority, verbose_name=_('musician'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'performance_collection_musician'
        verbose_name_plural = _('musicians')
        ordering = []
