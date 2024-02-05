# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.domain_vocal import DomainVocalForm
from ... import tools



class DomainVocalDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_vocal-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'domain_vocal:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainVocalDetail, self).get_context_data(**kwargs)
            context['domain_vocal'] = tools.request_api(
                '/api/domain_vocal/' + context['id'])
            context['form'] = DomainVocalForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Ce genre vocal n’existe pas.'))
        except Exception as err:
            context['domain_vocal'] = {}
            context['error'] = err
            context['form'] = DomainVocalForm()
        return context
