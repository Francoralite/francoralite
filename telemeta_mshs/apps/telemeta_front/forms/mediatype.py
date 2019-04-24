# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _


class MediaTypeForm(forms.Form):
    value = forms.CharField(
        label=_(u'Nom'),
        max_length=255, required=True)
    notes = forms.CharField(
        label=_(u'Notes'),
        widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(MediaTypeForm, self).__init__(*args, **kwargs)
