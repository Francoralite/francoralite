# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):
    # Description of the table
    "To locate some resources"

    # List of the fields
    code = models.CharField(_('code'), max_length=255)
    name = models.CharField(_('name'), max_length=1024)
    notes = models.TextField(_('notes'), null=True, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)


class Meta:
    app_label = 'telemeta_api'
    db_table = 'location_api'
    verbose_name_plural = _('locations')
    ordering = []


def __unicode__(self):
    return '%s' % (self.code)
