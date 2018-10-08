# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms


class PersonneForm(forms.Form):
    last_name = forms.CharField(label='Nom', max_length=255)
    first_name = forms.CharField(label='Prénom', max_length=255)
    notes = forms.CharField(
        label='Biographie',
        widget=forms.Textarea, required=False)
