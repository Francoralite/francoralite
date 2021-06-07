# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import gettext_lazy as _


class SkosCollection(models.Model):
    # Description of the table
    "Collections found in an DRF file."

    # List ofe the fields
    name = models.CharField(_('nom'), max_length=500)
    uri = models.CharField(_('uri'), max_length=500)
    number = models.CharField(_(u'numérotation'), max_length=40)
    collection = models.ForeignKey(
            'francoralite_api.SkosCollection',
            related_name='skos_collection',
            verbose_name=_('Collection parente'),
            null=True, blank=True, default=None,
            on_delete=models.SET_NULL)
    type = models.CharField(_('type'), max_length=40)

    class Meta:
        app_label = 'francoralite_api'
        db_table = 'skos_collection'
        verbose_name_plural = _('skos_collections')
        ordering = []

    def __unicode__(self):
        return self.name
