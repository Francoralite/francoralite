# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.block import BlockForm
from ... import tools as tools


class BlockDetail(FrancoraliteTemplateView):
    template_name = '../templates/enum/block-detail.html'
    keycloak_scopes = {
        'DEFAULT': 'block:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(BlockDetail, self).get_context_data(**kwargs)
            context['custom_block'] = tools.request_api(
                '/api/block/' + context['id'])
            context['custom_block']['type_label'] = dict(
                BlockForm.TYPE_CHOICES).get(context['custom_block']['type'])
            context['form'] = BlockForm()
        except Http404:
            raise Http404(_('Ce bloc n’existe pas.'))
        except Exception as err:
            context['custom_block'] = {}
            context['error'] = err
            context['form'] = BlockForm()
        return context
