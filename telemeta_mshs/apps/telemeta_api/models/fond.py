# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Fond(models.Model):
    # Description of the table
    "Fonds, they belongs to an institution and they own some missions"

    # List of the fields
    institution = models.ForeignKey(
        'telemeta_api.Institution',
        related_name='fonds',
        verbose_name=_('Institution'))
    title = models.CharField(_('titre'), max_length=255)
    alt_title = models.CharField(
        _(u'Titre original'), blank=True, max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    code = models.CharField(
        _('cote'), validators=[
            RegexValidator(
                regex=r'^[A-Z]{4}_[A-Z]{3}$',
                message='Code must conform to XXXX_XXX',
                code='invalid_code',
            )
        ],  max_length=255)
    code_partner = models.CharField(
        _('Cote dans l\'institution partenaire'),
        null=True, blank=True, max_length=255)
    acquisition_mode = models.ForeignKey(
        'telemeta_api.AcquisitionMode',
        related_name='fonds',
        verbose_name=_('Mode d\'acquisition'),
        blank=True,
        null=True, on_delete=models.SET_NULL)
    conservation_site = models.CharField(
        _('lieu de conservation original'),
        null=True, blank=True, max_length=255)
    comment = models.TextField(_('commentaires'), null=True, blank=True)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'fond'
        verbose_name_plural = _('fonds')
        ordering = ['code', 'title']

    def __unicode__(self):
        return self.title
