# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from .hornbostelsachs import HornbostelSachs
from django.utils.translation import gettext_lazy as _


class Instrument(models.Model):
    name = models.CharField(_('Nom'), unique=True, max_length=255)
    notes = models.TextField(_('Notes'), null=True, blank=True)
    typology = models.ForeignKey(HornbostelSachs,
                                 blank=True, null=True,
                                 verbose_name=_('HornbostelSachs'),
                                 on_delete=models.SET_NULL)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'instrument'
        verbose_name_plural = _('instruments')
        ordering = []
