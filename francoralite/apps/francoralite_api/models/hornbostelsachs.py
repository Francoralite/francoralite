# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from django.utils.translation import gettext_lazy as _


class HornbostelSachs(models.Model):
    number = models.CharField(_(u'Numérotation'), unique=True, max_length=30)
    name = models.TextField(_('Nom'), null=True, blank=True)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'hornbostelsachs'
        ordering = []
