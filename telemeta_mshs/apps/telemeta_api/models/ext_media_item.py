# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db.models import (
    CASCADE, ForeignKey, OneToOneField,
    CharField, TextField, BooleanField)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from telemeta.models.item import MediaItem
from telemeta.models.core import ModelCore, MetaCore
from markdownx.utils import markdownify
from .coupe import Coupe


class ExtMediaItem(ModelCore):
    """
    Telemeta MediaItem model extend
    """
    media_item = OneToOneField(MediaItem, on_delete=CASCADE)
    mshs_alt_title = CharField(
        blank=True, verbose_name=_('alternate title'), max_length=255)
    description = TextField(
        blank=True, verbose_name=_('description'),
        help_text=_('Describe the item'))
    # mshs_author = CharField(_('Auteur(s)'))
    # mshs_composer = CharField(_('Compositeur(s)'))
    mshs_timbre = CharField(
        _("Timbre de l'air"), blank=True, max_length=255)
    mshs_timbre_ref = CharField(
        _(u"Timbre(s) référencé(s)"), blank=True, max_length=1024)
    mshs_timbre_code = CharField(
        _('Cote du timbre'), blank=True, max_length=255)
    mshs_melody = TextField(
        _(u"Mélodie (transcription alphabétique)"),
        blank=True,
        help_text=_('You can use ABC notation'))
    DOMAINS = (
        ('T', 'Témoignage'),
        ('C', 'Chanson'),
        ('A', 'Autre expression vocale'),
        ('I', 'Expression instrumentale'),
        ('R', 'Conte ou récit légendaire')
    )
    mshs_domain = CharField(
        _('Domain'), blank=True, choices=DOMAINS, max_length=5)
    mshs_domain_song = CharField(
        _('kind of song'), blank=True, max_length=255)
    mshs_domain_vocal = CharField(
        _("Autre expression vocale"), blank=True, max_length=255)
    mshs_domain_music = CharField(
        _("Expression instrumentale"), blank=True, max_length=255)
    mshs_domain_tale = CharField(_("Conte"), blank=True, max_length=255)
    mshs_details = TextField(_(u"Précisions sur l'item"), blank=True)
    mshs_function = CharField(_('Fonction(s)'), blank=True, max_length=255)
    mshs_dance = CharField(_('Danse(s)'), blank=True, max_length=255)
    mshs_dance_details = TextField(
        _(u"Précisions sur la danse"), blank=True)
    mshs_deposit_digest = TextField(_(u"Résumé"), blank=True)
    mshs_deposit_thematic = TextField(_(u"Thématiques"), blank=True)
    mshs_deposit_names = TextField(
        _(u"Nom(s) propre(s) cité(s) "),
        blank=True,
        help_text=_('First name, Last name ; First name, Last name'))
    mshs_deposit_places = TextField(
        _(u"Lieu(x) cité(s)"),
        blank=True,
        help_text=_('Place named; place named; ...'))
    mshs_deposit_periods = TextField(
        _(u"Période(s) citée(s)"),
        blank=True,
        help_text=_('Period recounted; period recounted; ...'))
    mshs_text_bool = BooleanField(_('Text ?'), default=False)
    mshs_text = TextField(_('Text'), blank=True)
    mshs_incipit = TextField(_('incipit'), blank=True)
    mshs_refrain = TextField(_('refrain'), blank=True)
    mshs_jingle = TextField(_('jingle'), blank=True)
    mshs_ch_coupe = ForeignKey(
        Coupe, blank=True, null=True, verbose_name=_('coupe'))
    mshs_title_ref_coirault = CharField(
        _('Title ref. Coirault'), blank=True, max_length=255)
    mshs_code_coirault = CharField(
        _('code Coirault'), blank=True, max_length=255)
    mshs_title_ref_laforte = CharField(
        _('Title ref. Laforte'), blank=True, max_length=255)
    mshs_code_laforte = CharField(
        _('code Laforte'), blank=True, max_length=255)
    mshs_title_ref_Dela = CharField(
        _('Title ref. Delarue-Teneze'), blank=True, max_length=255)
    mshs_code_Dela = CharField(
        _('code Delarue-Teneze'), blank=True, max_length=255)
    mshs_title_ref_Aare = CharField(
        _('Title ref. Aare-Thomson'), blank=True, max_length=255)
    mshs_code_Aare = CharField(
        _('code Aare-Thomson'), blank=True, max_length=255)
    mshs_musical_organization = CharField(
        _(u"Organisation musicale"), blank=True, max_length=255)
    mshs_group = CharField(_('Formation'), blank=True, max_length=255)
    code = CharField(
        _('code'), unique=True, blank=True,
        help_text=_('CollectionCode_ItemCode'),
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{4}_[A-Z]{3}_[A-Z0-9]{4}_[0-9]{4}_[0-9]{3}$',
                message='Code must conform to XXXX_XXX_000X_0000_000',
                code='invalid_code',
            )
        ], max_length=255)

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'ext_media_item'

    @property
    def description_markdown(self):
        return markdownify(self.description)

    @property
    def dance_details_markdown(self):
        return markdownify(self.dance_details)

    @property
    def mshs_deposit_digest_markdown(self):
        return markdownify(self.mshs_deposit_digest)

    @property
    def mshs_text_markdown(self):
        return markdownify(self.mshs_text)

    @property
    def mshs_dance_details_markdown(self):
        return markdownify(self.mshs_dance_details)


@receiver(post_save, sender=MediaItem)
def create_media_item_extended(sender, instance, created, **kwargs):
    if created:
        ExtMediaItem.objects.create(media_item=instance)


@receiver(post_save, sender=MediaItem)
def save_media_item_extended(sender, instance, **kwargs):
    instance.extmediaitem.save()
