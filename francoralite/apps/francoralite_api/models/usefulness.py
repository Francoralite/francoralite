# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _


class Usefulness(models.Model):
    # Description of the table
    "Usefulness is used to specify the utility of an item. E.g.: labor's song"

    # List of the fields
    name = models.CharField(_('Nom'), unique=True, max_length=255)
    notes = models.TextField(_('Notes'), null=True, blank=True)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'api_usefulness'
        verbose_name_plural = _('usefulnesses')
        ordering = ['name']

    def __unicode__(self):
        return self.name
