# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.thematic import ThematicForm
from ... import tools


class ThematicDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/thematic-detail.html"

    keycloak_scopes = {
        'DEFAULT': 'thematic:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(ThematicDetail, self).get_context_data(**kwargs)
            context['thematic'] = tools.request_api(
                '/api/thematic/' + context['id'])
            context['form'] = ThematicForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cette thématique n’existe pas.'))
        except Exception as err:
            context['thematic'] = {}
            context['error'] = err
            context['form'] = ThematicForm()
        return context
