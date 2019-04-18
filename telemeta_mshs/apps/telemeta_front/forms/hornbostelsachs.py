# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _


class HornbostelsachsForm(forms.Form):
    number = forms.CharField(
        label=_(u'Numéro'),
        max_length=255, required=True)
    name = forms.CharField(
        label=_(u'Nom'),
        widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(HornbostelsachsForm, self).__init__(*args, **kwargs)
