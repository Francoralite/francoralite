# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from telemeta.models.core import *
from telemeta.models.location import *
from django.utils.translation import ugettext_lazy as _

class Authority(ModelCore):
    # Description of the table
    "People who produced something."


    # List of the fields
    last_name = CharField(_('last name'), required=True)
    first_name = CharField(_('first name') )
    civilite =  CharField(_('civilite') )
    alias =  CharField( _('alias') )
    ROLES = (
        ('ENQ','Enquêteur'),
        ('INF','Informateur'),
        ('AUT','Auteur'),
        ('CMP','Compositeur'),
        ('EDT','Editeur')
    )
    roles = CharField(_('Roles'),choices=ROLES)
    birth_date = DateField(null=True)
    birth_location = ForeignKey('telemeta.Location', related_name='birth_location', verbose_name=_('birth location'), blank=True, null=True, on_delete=models.SET_NULL)
    death_date = DateField( null=True )
    death_location = ForeignKey('telemeta.Location',related_name='death_location', verbose_name=_('death location'), blank=True, null=True, on_delete=models.SET_NULL)
    biography = TextField( _('biography'), null=True, blank=True )
    uri = URLField(_('URI'), null=True, blank=True)


    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'authority'
        verbose_name_plural = _('authorities')
        ordering = []

    def __unicode__(self):
        if self.civilite :
            return '%s %s %s' % (self.civilite,  self.first_name, self.last_name)
        return '%s %s' % (self.first_name, self.last_name)
