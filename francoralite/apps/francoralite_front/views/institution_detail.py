# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ..forms.institution import InstitutionForm
from ..francoralite_template_view import FrancoraliteTemplateView
from .. import tools as tools


class InstitutionDetail(FrancoraliteTemplateView):
    template_name = "../templates/institution-detail.html"
    
    keycloak_scopes = {
        'DEFAULT': 'institution:view',
    }
    api_url_prefix = '/api/institution/'

    def get_context_data(self, **kwargs):
        try:
            context = super(InstitutionDetail, self).get_context_data(**kwargs)
            # Obtain values of the record institution
            context['form'] = InstitutionForm()
            context['institution'] = tools.request_api(
                self.api_url_prefix + context['id'])
            # Obtain values of related fonds
            context['fonds'] = tools.request_api(
                '/api/fond?institution=' + context['id'])
        except Http404:
            raise Http404(_('Cette institution n’existe pas.'))
        except Exception as err:
            context['institution'] = {}
            context['fonds'] = []
            context['error'] = err
        return context
