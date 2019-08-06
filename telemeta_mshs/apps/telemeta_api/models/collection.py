# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from telemeta.models.core import MetaCore
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Collection(models.Model):
    # Description of the table
    "Collections, they belongs to a mission"

    # List of the fields

    mission = models.ForeignKey(
            'telemeta_api.Mission',
            related_name='collection',
            verbose_name=_('Mission'), blank=True, default="")
    title = models.CharField(_('titre'), max_length=255)
    alt_title = models.CharField(
        _(u'Titre original'), blank=True, max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    recording_context = models.CharField(
        _(u'Contexte d\'enregistrement'), blank=True, max_length=255)
    recorded_from_year = models.DateField(blank=True, null=True)
    recorded_to_year = models.DateField(blank=True, null=True)
    year_published = models.IntegerField(blank=True, null=True)
    location_details = models.TextField(
        _(u'Précisions sur le lieu'),
        default="",
        blank=True)
    cultural_area = models.CharField(
        _(u'Aire culturelle'),
        help_text=_('Aire culturelle ; Aire culturelle'),
        default="", blank=True,  max_length=255)
    language = models.CharField(
        'langage',
        help_text=_('Langage ; langage'),
        default="", blank=True,  max_length=255)
    publisher_collection = models.CharField(
        _(u'Collection éditeur'),
        help_text=('collection ; collection'),
        default="", blank=True,  max_length=255)
    booklet_author = models.CharField(
        _(u'Auteur de la note éditée'),
        help_text=_(u'Nom de l\'auteur'),
        default="", blank=True,  max_length=255)
    metadata_author = models.CharField(
        _(u'Rédacteur(s) fiches ou registre'),
        help_text=_(u'Rédacteur ; rédacteur'),
        default="", blank=True,  max_length=255)
    code = models.CharField(
        _('cote'), validators=[
            RegexValidator(
                regex=r'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}$',
                message='Code must conform to XXXX_XXX_000X_0000',
                code='invalid_code',
            )
        ],  max_length=255)
    code_partner = models.CharField(
        _('Cote dans l\'institution partenaire'),
        null=True, blank=True, max_length=255)
    booklet_description = models.TextField(
        _(u'Documentation associée'), null=True, blank=True)
    comment = models.TextField(
        _('commentaires'), null=True, blank=True)
    media_type = models.ForeignKey(
        'telemeta_api.MediaType',
        related_name='collection',
        verbose_name=_(u'Type de média'),
        blank=True,
        null=True, on_delete=models.SET_NULL)
    physical_items_num = models.IntegerField(
        _(u'Nombre de composants (support / pièce)'), blank=True, null=True)
    auto_period_access = models.BooleanField(
        _(u'Accès automatique après la date glissante'), default=True)
    legal_rights = models.ForeignKey(
        'telemeta_api.LegalRights',
        related_name='collection',
        verbose_name=_(u'Droits d\'utilisation'),
        blank=True,
        null=True, on_delete=models.SET_NULL)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'int_collection'
        verbose_name_plural = _('collections')
        ordering = ['code', 'title']
