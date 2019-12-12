# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _
from .core import Core


class ItemForm(forms.Form):
    # General ----------------------------------------------------

    title = forms.CharField(label=_(u'Titre'), max_length=255, required=True)
    alt_title = forms.CharField(
        label=_(u'Autre(s) titre(s)'),
        max_length=255, required=False)
    trans_title = forms.CharField(
        label=_(u'Traduction(s) titre(s)'),
        max_length=255, required=False)
    description = forms.CharField(label=_(u'Description'),
                                  widget=forms.Textarea, required=False)
    #   Données d'archivage
    code = forms.CharField(
        label=_('Cote'),
        widget=forms.TextInput(
            attrs={
                 'style': 'text-transform:uppercase;',
                 'placeholder': 'format : aaaa_aaa_9999_9999_999',
                 'pattern': '^[A-Za-z]{4}_[A-Za-z]{3}_[A-Za-z0-9]{4}_[0-9]{4}_[0-9]{3}$',  # noqa
                 'title': _(u'Cote; format : aaaa_aaa_9999_9999_999'),  # noqa
             }
        ),
        max_length=255,
        required=True)
    code_partner = forms.CharField(
        label=_('Cote de l\'item dans l\'institution partenaire'),
        required=False)
    auto_period_access = forms.BooleanField(
        label=_(u'Accès automatique après la date glissante'),
        required=False)
    remarks = forms.CharField(
        label=_(u'Remarques concernant les données d\'archivage'),
        widget=forms.Textarea, required=False)
    file = forms.FileField(
        label=_(u'Fichier audio'),
        widget=forms.FileInput(),
        required=True
    )

    # Description -----------------------------------------------
    timbre = forms.CharField(
        label=_(u'Timbre de l\'air'), required=False)
    timbre_ref = forms.CharField(
        label=_(u'Timbre(s) référencé(s)'), required=False)
    melody = forms.CharField(
            label=_(u'Mélodie (transcription alphabétique)'),
            widget=forms.Textarea, required=False)
    # domain = forms.CharField(
    #     label=_(u'Domaine(s)'), required=False)
    DOMAINS = (
        ('T', 'Témoignage'),
        ('C', 'Chanson'),
        ('A', 'Autre expression vocale'),
        ('I', 'Expression instrumentale'),
        ('R', 'Conte ou récit légendaire')
    )
    domains = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=DOMAINS,
        label=_(u'Domaine(s)'),
        required=False)

    # Description / deposit
    deposit_digest = forms.CharField(label=_(u'Résumé'), required=False)
    deposit_names = forms.CharField(
        label=_(u'Nom(s) propre(s) cité(s)'), required=False)
    deposit_places = forms.CharField(
        label=_(u'Lieu(x) cité(s)'), required=False)
    deposit_periods = forms.CharField(
        label=_(u'Période(s) citée(s)'), required=False)

    # Text ------------------------------
    text_bool = forms.BooleanField(
        label=_(u'Présence de texte'),
        required=False)
    text = forms.CharField(label=_(u'Texte'), required=False)
    incipit = forms.CharField(label=_(u'Incipit'), required=False)
    refrain = forms.CharField(label=_(u'Refrain'), required=False)

    # refrain = forms.CharField(
    #    label=_(u'Refrain'),
    #    widget=forms.Textarea(attrs={"rows": 5, "cols": 20}, required=False))

    jingle = forms.CharField(label=_(u'Ritournelle du conte'), required=False)
    # Références

    # Voix-instruments -----------------------------

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        self.fields['media_type'] = forms.ChoiceField(
            label=_(u'Type de média'),
            choices=Core.get_choices(
                entity="mediatype", label_field="name"),
            required=True)

        self.fields['collection'] = forms.ChoiceField(
            label=_(u'Enquête'),
            choices=Core.get_choices(
                entity="collection", label_field="title"),
            required=True)

        self.fields['coupe'] = forms.ChoiceField(
            label=_(u'Coupe'),
            choices=Core.get_choices(
                entity="coupe", label_field="name"),
            required=False)
