# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.dance import DanceForm
from ... import tools


class DanceDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/dance-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'dance:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(DanceDetail, self).get_context_data(**kwargs)
            context['dance'] = tools.request_api(
                '/api/dance/' + context['id'])
            context['form'] = DanceForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cette danse n’existe pas.'))
        except Exception as err:
            context['dance'] = {}
            context['error'] = err
            context['form'] = DanceForm()
        return context
