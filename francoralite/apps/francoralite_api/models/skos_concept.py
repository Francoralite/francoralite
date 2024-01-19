# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _


class SkosConcept(models.Model):
    # Description of the table
    "Concepts found in an DRF file."
    ""

    # List ofe the fields
    number = models.CharField(_('numérotation'), max_length=40)
    name = models.CharField(_('nom'), max_length=500)
    uri = models.CharField(_('uri'), max_length=500)
    collection = models.ForeignKey(
            'francoralite_api.SkosCollection',
            related_name='skos_concept',
            verbose_name=_('Collection parente'),
            default=None,
            on_delete=models.CASCADE)
    abstract = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'skos_concept'
        verbose_name_plural = _('skos_concepts')
        ordering = ['number']

    def __unicode__(self):
        return self.name
