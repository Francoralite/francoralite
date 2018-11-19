# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from bootstrap_datepicker.widgets import DatePicker
from .core import Core


class CollectionForm(forms.Form):
    title = forms.CharField(label=_(u'Titre'), max_length=255, required=True)
    alt_title = forms.CharField(
        label=_(u'Titre original'), max_length=255, required=False)
    record_from_year = forms.DateField(
        label=_(u'Date d\'enregistrement (depuis)'),
        required=False,
        widget=DatePicker(
              options={
                    "format": "yyyy-mm-dd",
                    "language": "fr",
                    "autoclose": True
                }
            )
    )
    record_to_year = forms.DateField(
        label=_(u'Date d\'enregistrement (jusqu\'à)'),
        required=False,
        widget=DatePicker(
              options={
                    "format": "yyyy-mm-dd",
                    "language": "fr",
                    "autoclose": True
                }
            )
    )
    year_published = forms.IntegerField(
        label=_(u'Année de parution'),
        widget=forms.TextInput(
            attrs={
                 'data-mask': '9999',
                 'style': 'text-transform:uppercase;'
             }
        ), required=False)
    location_details = forms.CharField(
        label=_(u'Précisions sur le lieu'),
        widget=forms.Textarea, required=False)
    cultural_area = forms.CharField(
        label=_(u'Aire culturelle'), required=False)
    language = forms.CharField(
        label=_(u'Langue(s)'), required=False)
    publisher_collection = forms.CharField(
        label=_(u'Collection éditeur'), required=False)
    booklet_author = forms.CharField(
        label=_(u'Auteur de la notice éditée'), required=False)
    metadata_author = forms.CharField(
        label=_(u'Rédacteur(s) fiche ou registre'), required=False)
    code_partner = forms.CharField(
        label=_('Cote dans l\'institution partenaire'), required=False)
    code = forms.CharField(
        label=_(u'Cote de l\'enquête'),
        widget=forms.TextInput(
            attrs={
                'style': 'text-transform:uppercase;'
                }
            ),
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z]{4}_[A-Za-z]{3}_[A-Za-z0-9]{4}_[0-9]{4}$',
                message=_(u'Ce code n\'est pas conforme.'),
                code='invalide_code'
                ),
        ],
        max_length=30, required=True)
    booklet_description = forms.CharField(
        label=_(u'Documentation associée'),
        widget=forms.Textarea, required=False)
    physical_items_num = forms.IntegerField(
        label=_(u'Nombre de composants (support/pièce)'), required=False)
    auto_period_access = forms.BooleanField(
        label=_(u'Accès automatique après la date glissante'), required=False)
    comment = forms.CharField(
        label=_(u'Commentaires'),
        widget=forms.Textarea, required=False)

    descriptions = forms.CharField(label=_(u'Descriptions'),
                                   widget=forms.Textarea, required=False)
    description = forms.CharField(label=_(u'Description'),
                                  widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)

        PUBLIC_ACCESS_CHOICES = (
            ('none', _(u'Aucun')),
            ('metadata', _(u'Meta-données')),
            ('partial', _(u'Partiel')),
            ('full', _(u'Complet'))
            )

        self.fields['public_access'] = forms.ChoiceField(
            label=_(u'Type d\'accès'),
            choices=PUBLIC_ACCESS_CHOICES,
            initial="metadata",
            required=True)

        self.fields['recording_context'] = forms.ChoiceField(
            label=_(u'Contexte d\'enregistrement'),
            choices=Core.get_choices(
                entity="recordingcontext", label_field="value"),
            required=True)

        self.fields['media_type'] = forms.ChoiceField(
            label=_(u'Type de média'),
            choices=Core.get_choices(
                entity="mediatype", label_field="value"),
            required=True)

        self.fields['mission'] = forms.ChoiceField(
            label=_(u'Mission'),
            choices=Core.get_choices(
                entity="mission", label_field="title"),
            required=True)

        self.fields['legal_rights'] = forms.ChoiceField(
            label=_(u'Droits d\'utilisation'),
            choices=Core.get_choices(
                entity="legalrights", label_field="value"),
            required=True)
