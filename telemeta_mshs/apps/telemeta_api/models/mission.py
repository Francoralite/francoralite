# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from telemeta.models.core import MetaCore
from telemeta.models.resource import MediaBaseResource
from django.utils.translation import ugettext_lazy as _
from django.db.models import CharField
from django.db import models


class Mission(MediaBaseResource):
    # Description of the table-
    "Mission belongs to a Fonds"

    # List of the fields
    fonds = models.ForeignKey(
            'telemeta_api.Fond',
            related_name='mission',
            verbose_name=_('Fonds'))
    code_partner = CharField(
        _('Cote de la mission dans l\'institution partenaire'),
        null=True, blank=True, max_length=255)

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'mission'
        verbose_name_plural = _('missions')
        ordering = []

    def __unicode__(self):
        return self.title
