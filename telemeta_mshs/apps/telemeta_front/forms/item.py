# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import ugettext_lazy as _
from .core import Core


class ItemForm(forms.Form):
    # FIXIT -----------
    title = forms.CharField(label=_(u'Titre'), max_length=255, required=True)

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(
            *args, **kwargs)

        # FIXIT -----------
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
