# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import forms
from django.utils.translation import gettext_lazy as _

from francoralite.apps.francoralite_front import tools
from django.core.exceptions import ValidationError


class BlockForm(forms.Form):

    TYPE_CUSTOM_TEXT = None
    TYPE_MAP = 'M'
    TYPE_PARTNERS = 'P'
    TYPE_CHOICES = (
        (TYPE_CUSTOM_TEXT, _('Texte personnalisé')),
        (TYPE_MAP, _('Carte')),
        (TYPE_PARTNERS, _('Partenaires')),
    )

    type = forms.ChoiceField(label=_(u'Type'),
        choices=TYPE_CHOICES, required=False)
    title = forms.CharField(label=_(u'Titre'),
        max_length=255, required=True)
    content = forms.CharField(label=_(u'Contenu'),
        widget=forms.Textarea, required=False)
    order = forms.IntegerField(label=_(u'Ordre d’affichage'),
        widget=forms.NumberInput, min_value=1, required=True)
    show = forms.BooleanField(label=_(u'Afficher'),
        required=False)

    def __init__(self, *args, **kwargs):
        super(BlockForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        for block in tools.request_api('/api/block'):
            if block.get('id') == getattr(self, 'current_id', None):
                continue

            block_title = cleaned_data.get('title')
            if block_title and block.get('title') == block_title:
                self.add_error('title', ValidationError(
                    _('Un bloc avec ce titre existe déjà.')))
                raise ValidationError(_('Un bloc avec ce titre existe déjà.'))

            block_type = cleaned_data.get('type')
            if block_type and block.get('type') == block_type:
                self.add_error('type', ValidationError(
                    _('Un bloc de ce type existe déjà.')))

            block_order = cleaned_data.get('order')
            if block_order and block.get('order') == block_order:
                self.add_error('order', ValidationError(
                    _('Un bloc avec cet ordre d’affichage existe déjà.')))

        return cleaned_data
