# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from bootstrap_datepicker.widgets import DatePicker
from django.utils.translation import ugettext_lazy as _


class PersonneForm(forms.Form):
    last_name = forms.CharField(label=_(u'Nom'), max_length=255, required=True)
    first_name = forms.CharField(label=_(u'Prénom'),
                                 max_length=255, required=False)
    civility = forms.CharField(
        label=_(u'Civilité'), max_length=16, required=False)
    alias = forms.CharField(label=_(u'Alias'), max_length=16, required=False)
    is_collector = forms.BooleanField(label=_(u'Enquêteur'), required=False)
    is_informer = forms.BooleanField(label=_(u'Informateur'), required=False)
    is_author = forms.BooleanField(label=_(u'Auteur'), required=False)
    is_composer = forms.BooleanField(label=_(u'Compositeur'), required=False)
    is_editor = forms.BooleanField(label=_(u'Editeur'), required=False)
    birth_date = forms.DateField(label=_(u'Date de naissance'),
                                 required=False,
                                 widget=DatePicker(
                                      options={
                                            "format": "yyyy-mm-dd",
                                            "language": "fr",
                                            "autoclose": True
                                        }
                                    ))
    birth_location_name = forms.CharField(
        label=_(u'Lieu de naissance'),
        widget=forms.TextInput(
            attrs={
                 'class': 'typeahead',
                 'placeholder': _(u'Saisir le nom d\'un lieu'),
             }
        ),
        required=False)
    birth_location = forms.CharField(
        label=_(u'Lieu de naissance'),
        widget=forms.HiddenInput(),
        required=False)
    death_date = forms.DateField(label=_(u'Date de Décès'), required=False,
                                 widget=DatePicker(
                                    options={
                                        "format": "yyyy-mm-dd",
                                        "language": "fr",
                                        "autoclose": True
                                    }
                                 ))
    death_location_name = forms.CharField(
        label=_(u'Lieu de décès'),
        widget=forms.TextInput(
            attrs={
                 'class': 'typeahead',
                 'placeholder': _(u'Saisir le nom d\'un lieu'),
             }
        ),
        required=False)
    death_location = forms.CharField(
            label=_(u'Lieu de décès'),
            widget=forms.HiddenInput(),
            required=False)
    biography = forms.CharField(
        label=u'Biographie',
        widget=forms.Textarea, required=False)
    uri = forms.CharField(label='URI', required=False)
