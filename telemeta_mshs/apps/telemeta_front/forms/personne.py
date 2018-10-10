# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from bootstrap_datepicker.widgets import DatePicker
from django.utils.translation import ugettext_lazy as _


class PersonneForm(forms.Form):
    last_name = forms.CharField(label=_('Nom'), max_length=255, required=True)
    first_name = forms.CharField(label=_('Prénom'),
                                 max_length=255, required=False)
    civilite = forms.CharField(
        label=_('Civilité'), max_length=16, required=False)
    alias = forms.CharField(label=_('Alias'), max_length=16, required=False)
    roles = forms.CharField(label=_('Rôles'), max_length=16, required=False)
    birth_date = forms.DateField(label=_('Date de naissance'), required=False,
                                 widget=DatePicker(
                                        options={
                                            "format": "mm/dd/yyyy",
                                            "autoclose": True
                                        }
                                    ))
    birth_location = forms.CharField(
        label=_('Lieu de naissance'), required=False)
    death_date = forms.DateField(label=_('Date de Décès'), required=False,
                                 widget=DatePicker(
                                    options={
                                        "format": "mm/dd/yyyy",
                                        "autoclose": True
                                    }
                                 ))
    death_location = forms.CharField(label=_('Lieu de décès'), required=False)
    biography = forms.CharField(
        label='Biographie',
        widget=forms.Textarea, required=False)
    uri = forms.CharField(label='URI', required=False)
