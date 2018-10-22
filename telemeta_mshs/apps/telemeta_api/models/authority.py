# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from telemeta.models.core import ModelCore, MetaCore, models
from telemeta.models.core import (
    CharField, TextField, DateField, URLField, BooleanField)
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Authority(ModelCore):
    # Description of the table
    "People who produced something."

    # List of the fields
    last_name = CharField(_('last name'), required=True)
    first_name = CharField(_('first name'))
    civility = CharField(_('civility'))
    alias = CharField(_('alias'))
    is_collector = BooleanField(_('collector'), default=False)
    is_informer = BooleanField(_('informer'), default=False)
    is_author = BooleanField(_('author'), default=False)
    is_composer = BooleanField(_('composer'), default=False)
    is_editor = BooleanField(_('editor'), default=False)
    birth_date = DateField(null=True)
    birth_location = models.ForeignKey(
        'telemeta_api.Location',
        related_name='birth_location',
        verbose_name=_('birth location'),
        blank=True,
        null=True, on_delete=models.SET_NULL)
    death_date = DateField(null=True)
    death_location = models.ForeignKey(
        'telemeta_api.Location',
        related_name='death_location',
        verbose_name=_('death location'),
        blank=True,
        null=True, on_delete=models.SET_NULL)
    biography = TextField(_('biography'), null=True, blank=True)
    uri = URLField(_('URI'), null=True, blank=True)

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'authority'
        verbose_name_plural = _('authorities')
        ordering = []

    def __unicode__(self):
        if self.civilite:
            return '%s %s %s' % (
                self.civilite,  self.first_name, self.last_name)
        return '%s %s' % (self.first_name, self.last_name)
