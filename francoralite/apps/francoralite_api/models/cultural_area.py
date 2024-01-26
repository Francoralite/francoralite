# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from django.utils.translation import gettext_lazy as _


class CulturalArea(models.Model):
    # Description of the table
    "Cultural area"

    # List of the fields
    name = models.CharField(_('Nom'), unique=True, max_length=255)
    geojson = models.JSONField(_('GeoJSON'), null=True, blank=True)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_cultural_area'
        verbose_name = _('aire culturelle')
        verbose_name_plural = _('aires culturelles')
        ordering = ['name']

    def __unicode__(self):
        return self.name
