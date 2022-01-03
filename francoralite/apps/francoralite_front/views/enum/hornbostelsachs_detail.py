# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.hornbostelsachs import HornbostelsachsForm
from ... import tools as tools



class HornbostelsachsDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/hornbostelsachs-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'hornbostelsachs:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(HornbostelsachsDetail, self).get_context_data(
                **kwargs)
            context['hornbostelsachs'] = tools.request_api(
                '/api/hornbostelsachs/' + context['id'])
            context['form'] = HornbostelsachsForm()
        except Http404:
            raise Http404(_('Cette référence n’existe pas.'))
        except Exception as err:
            context['hornbostelsachs'] = {}
            context['error'] = err
            context['form'] = HornbostelsachsForm()
        return context
