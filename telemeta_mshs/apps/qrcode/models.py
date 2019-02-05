# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class QrCode(models.Model):
    pass

    class Meta:
        app_label = 'qrcode'
        db_table = 'qrcode'
        verbose_name_plural = _('qrcodes')
        ordering = []
