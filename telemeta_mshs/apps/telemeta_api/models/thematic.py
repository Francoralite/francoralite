# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _


class Thematic(models.Model):
    # Description of the table
    "Thematic used by a deposit (for each item)"

    # List ofe the fields
    name = models.CharField(_('Nom'), unique=True, max_length=255)
    notes = models.TextField(_('Notes'), null=True, blank=True)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_thematic'
        verbose_name_plural = _('thematics')
        ordering = ['name']

    def __unicode__(self):
        return self.name
