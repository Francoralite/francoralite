# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _


class Institution(models.Model):
    "Institution who owns some resources"

    name = models.CharField(_('name'), max_length=255)
    notes = models.TextField(_('notes'), null=True, blank=True)


    class Meta:
        app_label = 'telemeta_api'
        db_table = 'institutions'
        verbose_name_plural = _('institutions')
        ordering = ['name']

    def __unicode__(self):
        return self.name
