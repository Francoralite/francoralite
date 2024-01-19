# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import gettext_lazy as _


class RefLaforteForm(forms.Form):
    number = forms.CharField(label=_("Numérotation"), max_length=40, required=True)
    name = forms.CharField(label=_("Nom"), max_length=500, required=True)

    def __init__(self, *args, **kwargs):
        super(RefLaforteForm, self).__init__(*args, **kwargs)
