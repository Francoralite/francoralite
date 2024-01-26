# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.cultural_area import CulturalAreaForm
from ... import tools


class CulturalAreaDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/cultural_area-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'cultural_area:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(CulturalAreaDetail, self).get_context_data(**kwargs)
            context['cultural_area'] = tools.request_api(
                '/api/cultural_area/' + context['id'])
            context['form'] = CulturalAreaForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cette aire culturelle n’existe pas.'))
        except Exception as err:
            context['cultural_area'] = {}
            context['error'] = err
            context['form'] = CulturalAreaForm()
        return context
