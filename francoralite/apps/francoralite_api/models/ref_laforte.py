# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.db import models
from django.utils.translation import gettext_lazy as _


class RefLaforte(models.Model):
    number = models.CharField(_("numérotation"), max_length=40, unique=True)
    name = models.CharField(_("nom"), max_length=500)

    class Meta:
        app_label = "francoralite_api"
        db_table = "api_ref_laforte"
        verbose_name = _("Laforte")
        verbose_name_plural = _("Laforte")
        ordering = ['number']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
