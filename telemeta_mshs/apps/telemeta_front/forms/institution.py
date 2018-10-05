# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
# import django_bootstrap3_form as form3


class InstitutionForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=255)
    notes = forms.CharField(
        label='Notes',
        widget=forms.Textarea, required=False)
