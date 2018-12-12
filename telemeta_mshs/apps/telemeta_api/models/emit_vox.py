# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from django.utils.translation import ugettext_lazy as _


class EmitVox(models.Model):
    name = models.CharField(_(u"Nature de l'émission vocale"),
                            unique=True, max_length=255)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'emit_vox'
        verbose_name_plural = _(u'nature des émissions vocales')
        ordering = []
