# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.utils.translation import ugettext_lazy as _
from django.db import models


class Authority(models.Model):
    # Description of the table
    "People who produced something."

    # List of the fields
    last_name = models.CharField(_('last name'), max_length=255)
    first_name = models.CharField(_('first name'), max_length=255)
    civility = models.CharField(_('civility'), blank=True, max_length=255)
    alias = models.CharField(_('alias'), blank=True, max_length=255)
    is_collector = models.BooleanField(_('collector'), default=False)
    is_informer = models.BooleanField(_('informer'), default=False)
    is_author = models.BooleanField(_('author'), default=False)
    is_composer = models.BooleanField(_('composer'), default=False)
    is_editor = models.BooleanField(_('editor'), default=False)
    birth_date = models.DateField(null=True)
    birth_location = models.ForeignKey(
        'telemeta_api.Location',
        related_name='birth_location',
        verbose_name=_('birth location'),
        blank=True,
        null=True, on_delete=models.SET_NULL)
    death_date = models.DateField(null=True)
    death_location = models.ForeignKey(
        'telemeta_api.Location',
        related_name='death_location',
        verbose_name=_('death location'),
        blank=True,
        null=True, on_delete=models.SET_NULL)
    biography = models.TextField(_('biography'), null=True, blank=True)
    uri = models.URLField(_('URI'), null=True, blank=True)

    class Meta():
        app_label = 'telemeta_api'
        db_table = 'authority'
        verbose_name_plural = _('authorities')
        ordering = ['last_name', 'first_name']

    def __unicode__(self):
        if self.civility:
            return '%s %s %s' % (
                self.civility,  self.first_name, self.last_name)
        return '%s %s' % (self.first_name, self.last_name)
