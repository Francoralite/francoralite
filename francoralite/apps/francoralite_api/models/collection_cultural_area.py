# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _
from .collection import Collection
from .cultural_area import CulturalArea


class CollectionCulturalArea(models.Model):
    # Description of the table
    "The cultural areas of a collection"

    # List of the fields

    collection = models.ForeignKey(Collection, verbose_name=_('collection'),
            on_delete=models.CASCADE)
    cultural_area = models.ForeignKey(CulturalArea, verbose_name=_('cultural area'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'collection_cultural_area'
        verbose_name = _('cultural area of a collection')
        verbose_name_plural = _('cultural areas of collections')
        ordering = []
        unique_together = (('collection', 'cultural_area'), )
