# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import gettext_lazy as _


class CulturalAreaForm(forms.Form):
    name = forms.CharField(
        label=_(u'Nom'),
        max_length=255, required=True)
    geojson = forms.JSONField(
        label=_(u'GeoJSON'),
        widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(CulturalAreaForm, self).__init__(*args, **kwargs)
