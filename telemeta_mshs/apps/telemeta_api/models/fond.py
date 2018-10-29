# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from telemeta.models.core import MetaCore
from telemeta.models.resource import MediaBaseResource
from telemeta.models.core import CharField, TextField
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Fond(MediaBaseResource):
    # Description of the table
    "Fonds, they belongs to an institution and they own some missions"

    # List of the fields
    institution = models.ForeignKey(
        'telemeta_api.Institution',
        related_name='fonds',
        verbose_name=_('Institution'))
    code_partner = CharField(
        _('Cote dans l\'institution partenaire'),
        null=True, blank=True)
    acquisition_mode = models.ForeignKey(
        'telemeta_api.AcquisitionMode',
        related_name='fonds',
        verbose_name=_('Mode d\'acquisition'),
        blank=True,
        null=True, on_delete=models.SET_NULL)
    conservation_site = CharField(_('lieu de conservation original'),
                                  null=True, blank=True)
    comment = TextField(_('commentaires'), null=True, blank=True)

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'fond'
        verbose_name_plural = _('fonds')
        ordering = []

    def __unicode__(self):
        return self.title
