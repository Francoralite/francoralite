# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.civility import CivilityForm
from ... import tools


class CivilityDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/civility-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'civility:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(CivilityDetail, self).get_context_data(**kwargs)
            context['civility'] = tools.request_api(
                '/api/civility/' + context['id'])
            context['form'] = CivilityForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cette civilité n’existe pas.'))
        except Exception as err:
            context['civility'] = {}
            context['error'] = err
            context['form'] = CivilityForm()
        return context
