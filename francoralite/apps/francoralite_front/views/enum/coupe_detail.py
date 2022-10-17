# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.coupe import CoupeForm
from ... import tools as tools


class CoupeDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/coupe-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'coupe:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(CoupeDetail, self).get_context_data(**kwargs)
            context['coupe'] = tools.request_api(
                '/api/coupe/' + context['id'])
            context['form'] = CoupeForm()
        except Http404:
            raise Http404(_('Cette coupe n’existe pas.'))
        except Exception as err:
            context['coupe'] = {}
            context['error'] = err
            context['form'] = CoupeForm()
        return context
