# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from telemeta.models.core import MetaCore
from telemeta.models.resource import MediaBaseResource
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Collection(MediaBaseResource):
    # Description of the table
    "Collections, they belongs to a mission"

    # List of the fields

    mission = models.ForeignKey(
            'telemeta_api.Mission',
            related_name='collection',
            verbose_name=_('Mission'), blank=True, default="")
    alt_title = models.CharField(
        _(u'Titre original'), max_length=255)
    recording_context = models.CharField(
        _(u'Contexte d\'enregistrement'),  max_length=255)
    recorded_from_year = models.DateField(null=True)
    recorded_to_year = models.DateField(null=True)
    year_published = models.IntegerField(null=True)
    location = models.ForeignKey(
        'telemeta_api.Location',
        related_name='location',
        verbose_name=_('lieu'),
        blank=True,
        null=True, on_delete=models.SET_NULL)
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
    publisher = models.CharField(
        _(u'Editeur'),
        help_text=_(u'éditeur ; éditeur'),
        default="", blank=True, max_length=255)
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
        _(u'Nombre de composants (support / pièce)'), null=True)
    auto_period_access = models.BooleanField(
        _(u'Accès automatique après la date glissante'), default=True)

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'int_collection'
