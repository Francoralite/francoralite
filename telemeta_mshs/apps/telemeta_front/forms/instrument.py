# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _


class InstrumentForm(forms.Form):
    name = forms.CharField(
        label=_(u'Titre'),
        max_length=255, required=True)
    notes = forms.CharField(
        label=_(u'Notes'),
        widget=forms.Textarea, required=False)
    typology = forms.CharField(
        label=_(u'Classification Hornbostel-Sachs'),
        widget=forms.TextInput(
            attrs={
                 'class': 'typeahead',
                 'placeholder': _(u'Saisir le numéro d\'une entrée'),
             }
        ),
        required=False)
