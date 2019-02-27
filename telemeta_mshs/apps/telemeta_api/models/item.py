# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    # Description of the table
    "Media Item. Item belongs to a collection."

    # List of the fields

    # General -----------
    collection = models.ForeignKey(
            'telemeta_api.Collection',
            related_name='collection',
            verbose_name=_('Collection'))
    title = models.CharField(_('titre'), max_length=255)
    alt_title = models.CharField(
        _('autre titre'), default="", blank=True, max_length=255)
    trans_title = models.CharField(
        _('traduction titre'), default="", blank=True, max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    code = models.CharField(
        _('cote'), validators=[
            RegexValidator(
                regex=r'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}_[0-9]{3}$',
                message='Code must conform to XXXX_XXX_000X_0000_000',
                code='invalid_code',
            )
        ],  max_length=255)
    code_partner = models.CharField(
        _(u'cote de l\'item dans l\'institution partenaire'),
        null=True, blank=True, max_length=255)
    auto_period_access = models.BooleanField(
        _(u'accès automatique après la date glissante'), default=True)
    remarks = models.TextField(
        _(u'remarques concernant les données d\'archivage'),
        null=True, blank=True)
    date_edit = models.DateTimeField(_('date'), auto_now=True)
    media_type = models.ForeignKey(
        'MediaType',
        related_name="items",
        verbose_name=_(u'type de media'),
        blank=True, null=True, on_delete=models.SET_NULL)
    approx_duration = models.DurationField(
        _(u'durée estimée'),  null=True, blank=True)
    file = models.FileField(_('fichier son'), upload_to='items/%Y/%m/%d',
                            db_column="filename", max_length=1024)

    # Description -----------------------

    timbre = models.TextField(
        _(u"Timbre de l'air"), null=True, blank=True)
    timbre_ref = models.TextField(
        _(u"Timbre référencé"), null=True, blank=True)
    melody = models.TextField(
        _(u"Mélodie (transcription alphabétique)"),
        null=True, blank=True,
        help_text=_(u'Vous pouvez utiliser la notation ABC'))
    DOMAINS = (
        ('T', 'Témoignage'),
        ('C', 'Chanson'),
        ('A', 'Autre expression vocale'),
        ('I', 'Expression instrumentale'),
        ('R', 'Conte ou récit légendaire')
    )
    domain = models.CharField(
        _('Domaine'), blank=True, choices=DOMAINS, max_length=5)

    # Description / deposit  ---------
    deposit_digest = models.TextField(
        _(u"Résumé"), null=True, blank=True)
    deposit_names = models.TextField(
        _(u"Nom(s) propre(s) cité(s) "),
        null=True, blank=True,
        help_text=_('First name, Last name ; First name, Last name'))
    deposit_places = models.TextField(
        _(u"Lieu(x) cité(s)"),
        null=True, blank=True,
        help_text=_('Place named; place named; ...'))
    deposit_periods = models.TextField(
        _(u"Période(s) citée(s)"),
        null=True, blank=True,
        help_text=_('Period recounted; period recounted; ...'))

    # Text ------------------------------
    text_bool = models.BooleanField(_('Text ?'), default=False)
    text = models.TextField(_('Text'), null=True, blank=True)
    incipit = models.TextField(_('incipit'), null=True, blank=True)
    refrain = models.TextField(_('refrain'), null=True, blank=True)
    jingle = models.TextField(_('jingle'), null=True, blank=True)
    coupe = models.ForeignKey(
        'Coupe',
        related_name="items",
        verbose_name=_(u'coupe'),
        blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'item'
        verbose_name_plural = _('items')
        ordering = ['code', 'title']

    def __unicode__(self):
        # FIXIT------------------
        return self.title
