# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _
from .core import Core


class MissionForm(forms.Form):
    title = forms.CharField(label=_(u'Titre'), max_length=255, required=True)
    code = forms.CharField(label=_(u'Cote de la mission'),
                           widget=forms.TextInput(
                               attrs={
                                    'data-mask': '9999',
                                    'style': 'text-transform:uppercase;'
                                }
                           ),
                           max_length=16, required=True)
    code_partner = forms.CharField(
        label=_('Cote dans l\'institution partenaire'), required=False)
    descriptions = forms.CharField(label=_(u'Description'),
                                   widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(MissionForm, self).__init__(*args, **kwargs)

        PUBLIC_ACCESS_CHOICES = (
            ('none', _(u'Aucun')),
            ('metadata', _(u'Meta-données')),
            ('partial', _(u'Partiel')),
            ('full', _(u'Complet'))
            )

        self.fields['public_access'] = forms.ChoiceField(
            label=_(u'Type d\'accès'),
            choices=PUBLIC_ACCESS_CHOICES,
            initial="metadata",
            required=True)

        self.fields['fonds'] = forms.ChoiceField(
            label=_(u'Fonds'),
            choices=Core.get_choices(
                entity="fond", label_field="title"),
            required=True)
        self.fields['fonds'].readonly = True
