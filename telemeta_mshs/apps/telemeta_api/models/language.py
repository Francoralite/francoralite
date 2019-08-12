# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>
from django.db import models
from django.utils.translation import ugettext_lazy as _

SCOPE_CHOICES = (('I', 'Individual'), ('M', 'Macrolanguage'), ('S', 'Special'))

TYPE_CHOICES = (('A', 'Ancient'), ('C', 'Constructed'), ('E', 'Extinct'),
                ('H', 'Historical'), ('L', 'Living'), ('S', 'Special'))


class Language(models.Model):
    # Description of the table
    "ISO 639-3 normalized languages"

    identifier = models.CharField(_('identifier'), max_length=3)
    part2B = models.CharField(
        _('equivalent ISO 639-2 identifier (bibliographic)'), max_length=3)
    part2T = models.CharField(
        _('equivalent ISO 639-2 identifier (terminologic)'), max_length=3)
    part1 = models.CharField(
        _('equivalent ISO 639-1 identifier'), max_length=1)
    scope = models.CharField(_('scope'), choices=SCOPE_CHOICES, max_length=1)
    type = models.CharField(_('type'), choices=TYPE_CHOICES, max_length=1)
    name = models.CharField(_('name'), max_length=255)
    comment = models.TextField(_('comment'))

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_language'
        verbose_name_plural = _('languages')
        ordering = ['name']

    def __unicode__(self):
        return self.name
