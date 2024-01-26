# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.legal_rights import LegalRightsForm
from ... import tools

class LegalRightsDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/legal_rights-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'legal_rights:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(LegalRightsDetail, self).get_context_data(**kwargs)
            context['legal_rights'] = tools.request_api(
                '/api/legalrights/' + context['id'])
            context['form'] = LegalRightsForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Ces droits légaux n’existent pas.'))
        except Exception as err:
            context['legal_rights'] = {}
            context['error'] = err
            context['form'] = LegalRightsForm()
        return context
