# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _
from .authority import Authority
from .civility import Civility


class AuthorityCivility(models.Model):
    # Description of the table
    "The civilities of an authority"

    # List of the fields

    authority = models.ForeignKey(Authority, verbose_name=_('authority'),
            on_delete=models.CASCADE)
    civility = models.ForeignKey(Civility, verbose_name=_('civility'),
            on_delete=models.CASCADE)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'authority_civility'
        verbose_name = _('civility of an authority')
        verbose_name_plural = _('civilities of authorities')
        ordering = []
        unique_together = (('authority', 'civility'), )
