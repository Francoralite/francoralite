# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _
from bootstrap_datepicker.widgets import DatePicker
from .core import Core


class CollectionForm(forms.Form):
    title = forms.CharField(label=_(u'Titre'), max_length=255, required=True)
    alt_title = forms.CharField(
        label=_(u'Titre original'), max_length=255, required=True)
    code = forms.CharField(label=_(u'Cote de l\'enquête'),
                           widget=forms.TextInput(
                               attrs={
                                    'data-mask': '9999',
                                    'style': 'text-transform:uppercase;'
                                }
                           ),
                           max_length=16, required=True)
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
    comment = forms.CharField(
        label=_(u'Commentaires'),
        widget=forms.Textarea, required=False)

    code_partner = forms.CharField(
        label=_('Cote dans l\'institution partenaire'), required=False)
    descriptions = forms.CharField(label=_(u'Description'),
                                   widget=forms.Textarea, required=True)

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

        self.fields['mission'] = forms.ChoiceField(
            label=_(u'Mission'),
            choices=Core.get_choices(
                entity="mission", label_field="title"),
            required=True)
