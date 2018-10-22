# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from telemeta.models.core import ModelCore, MetaCore
from telemeta.models.core import CharField, TextField, FloatField
from django.utils.translation import ugettext_lazy as _


class Location(ModelCore):
    # Description of the table
    "To locate some resources"

    # List of the fields
    code = CharField(_('code'), required=True)
    name = CharField(_('name'), required=True)
    notes = TextField(_('notes'), null=True, blank=True)
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)


class Meta(MetaCore):
    app_label = 'telemeta_api'
    db_table = 'location_api'
    verbose_name_plural = _('locations')
    ordering = []


def __unicode__(self):
    return '%s' % (self.code)
