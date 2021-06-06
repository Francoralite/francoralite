# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

PUBLIC_ACCESS_CHOICES = (('none', _('none')), ('metadata', _('metadata')),
                         ('mixed', _('mixed')), ('full', _('full')))


class Mission(models.Model):
    # Description of the table-
    "Mission belongs to a Fonds"

    # List of the fields
    fonds = models.ForeignKey(
            'francoralite_api.Fond',
            related_name='mission',
            verbose_name=_('Fonds'),
            on_delete=models.CASCADE)
    title = models.CharField(_('titre'), max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    public_access = models.CharField(
        _('access type'),
        choices=PUBLIC_ACCESS_CHOICES,
        max_length=16, default="metadata")
    code = models.CharField(
        _('cote'), validators=[
            RegexValidator(
                regex=r'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}$',
                message='Code must conform to XXXX_XXX_000X',
                code='invalid_code',
            )
        ],  max_length=255)
    code_partner = models.CharField(
        _('Cote de la mission dans l\'institution partenaire'),
        null=True, blank=True, max_length=255)

    class Meta():
        app_label = 'francoralite_api'
        db_table = 'mission'
        verbose_name_plural = _('missions')
        ordering = ['code', 'title']

    def __unicode__(self):
        return self.title
