# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import gettext_lazy as _


class CoiraultForm(forms.Form):
    name = forms.CharField(
        label=_(u'Chanson-type'),
        max_length=255, required=True)
    number = forms.CharField(
        label=_(u'Numéro'),
        max_length=255, required=True)
    uri = forms.CharField(
        label=_(u'URI'),
        max_length=512, required=True)
    abstract = forms.CharField(
        label=_(u'Résumé'),
        widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(CoiraultForm, self).__init__(*args, **kwargs)
