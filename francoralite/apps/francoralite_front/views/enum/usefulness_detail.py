# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.usefulness import UsefulnessForm
from ... import tools


class UsefulnessDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/usefulness-detail.html"

    keycloak_scopes = {
        'DEFAULT': 'usefulness:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(UsefulnessDetail, self).get_context_data(**kwargs)
            context['usefulness'] = tools.request_api(
                '/api/usefulness/' + context['id'])
            context['form'] = UsefulnessForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cette fonction n’existe pas.'))
        except Exception as err:
            context['usefulness'] = {}
            context['error'] = err
            context['form'] = UsefulnessForm()
        return context
