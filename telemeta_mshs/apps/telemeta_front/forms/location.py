# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _


class LocationForm(forms.Form):
    name = forms.CharField(label=_(u'Nom'), max_length=255, required=True)
    latitude = forms.FloatField(label=_(u'Latitude'), required=True)
    longitude = forms.FloatField(label=_(u'Longitude'), required=True)
    type = forms.IntegerField(
        label=_('Type'), initial=0, widget=forms.HiddenInput())
    complete_type = forms.CharField(
        label=_('Type complet'), initial=1, widget=forms.HiddenInput())
    is_authoritative = forms.BooleanField(
        label=_('Officiel'), initial=True, widget=forms.HiddenInput())
