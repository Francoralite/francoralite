# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from instrument import Instrument
from emit_vox import EmitVox
from django.utils.translation import ugettext_lazy as _


class Performance(models.Model):
    # Description of the table
    "Performance made by some musicians"

    number = models.IntegerField(_("Nombre"))
    instrument = models.ForeignKey(Instrument,
                                   blank=True, null=True,
                                   verbose_name=_('instrument'),
                                   on_delete=models.SET_NULL)
    emit = models.ForeignKey(EmitVox,
                             blank=True, null=True,
                             verbose_name=_(u'Nature de l\'émission vocale'),
                             on_delete=models.SET_NULL)

    class Meta:
        abstract = True
