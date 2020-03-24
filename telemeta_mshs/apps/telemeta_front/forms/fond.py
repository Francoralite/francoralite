# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _
from .core import Core
import telemeta_front.tools as tools
from django.core.exceptions import ValidationError


def validate_code(value):
    test_code = tools.request_api('/api/fond?code=' + value)
    if len(test_code) > 0:
        raise ValidationError(
            _(u"Il existe déja un fonds avec la même cote. %(value)s"),
            params={'code': str(value)},
            code='invalid')


class FondForm(forms.Form):
    title = forms.CharField(label=_(u'Titre'), max_length=255, required=True)
    code = forms.CharField(label=_(u'Cote du fonds'),
                           widget=forms.TextInput(
                               attrs={
                                    'data-mask': 'aaaa_aaa',
                                    'pattern': '^[A-Za-z]{4}_[A-Za-z]{3}$',
                                    'style': 'text-transform:uppercase;'
                                }
                           ),
                           validators=[validate_code],
                           max_length=16, required=True)
    code_partner = forms.CharField(
        label=_('Cote dans l\'institution partenaire'), required=False)
    description = forms.CharField(label=_(u'Description'),
                                  widget=forms.Textarea, required=True)
    conservation_site = forms.CharField(
        label=_(u'Lieu de conservation original'),
        max_length=255, required=False)
    comment = forms.CharField(label=_(u'Commentaires'),
                              widget=forms.Textarea,
                              required=False)

    def __init__(self, *args, **kwargs):
        super(FondForm, self).__init__(*args, **kwargs)

        self.fields['institution'] = forms.ChoiceField(
            label=_(u'Institution partenaire'),
            choices=Core.get_choices(
                entity="institution", label_field="name"),
            required=True)

        self.fields['acquisition_mode'] = forms.ChoiceField(
            label=_(u'Mode d\'acquisition'),
            choices=Core.get_choices(
                entity="acquisitionmode", label_field="name"),
            required=False)
