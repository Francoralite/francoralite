# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.domain_tale import DomainTaleForm
from ... import tools


class DomainTaleDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_tale-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'domain_tale:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainTaleDetail, self).get_context_data(**kwargs)
            context['domain_tale'] = tools.request_api(
                '/api/domain_tale/' + context['id'])
            context['form'] = DomainTaleForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Ce genre de conte n’existe pas.'))
        except Exception as err:
            context['domain_tale'] = {}
            context['error'] = err
            context['form'] = DomainTaleForm()
        return context
