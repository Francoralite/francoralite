# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _


class LanguageForm(forms.Form):
    identifier = forms.CharField(
        label=_(u'Identificateur'), max_length=3, required=True)
    part2B = forms.CharField(
        label=_(u'equivalent ISO 639-2 (bibliographie)'),
        max_length=3, required=True)
    part2T = forms.CharField(
        label=_(u'equivalent ISO 639-2 (terminologie)'),
        max_length=3, required=True)
    part1 = forms.CharField(
        label=_('equivalent ISO 639-1 '), max_length=1, required=True)
    name = forms.CharField(
        label=_(u'Nom'), max_length=255)
    comment = forms.CharField(
        label=_(u'Commentaires'),
        widget=forms.Textarea,
        required=False)

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(
            *args, **kwargs)

        SCOPE_CHOICES = (
            ('I', _(u'Individuel')),
            ('M', _(u'Macrolanguage')),
            ('S', _(u'Spécial'))
            )
        TYPE_CHOICES = (
            ('A', 'Ancient'),
            ('C', 'Constructed'),
            ('E', 'Extinct'),
            ('H', 'Historical'),
            ('L', 'Living'),
            ('S', 'Special')
            )

        self.fields['scope'] = forms.ChoiceField(
            label=_(u'Scope'),
            choices=SCOPE_CHOICES,
            initial="I",
            required=True)
        self.fields['type'] = forms.ChoiceField(
            label=_(u'Type'),
            choices=TYPE_CHOICES,
            initial="L",
            required=True)
