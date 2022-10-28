# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ..forms.fond import FondForm
from ..francoralite_template_view import FrancoraliteTemplateView
from ..widgets import DomainsBarLoader
from .. import tools as tools


class FondDetail(FrancoraliteTemplateView):
    template_name = "../templates/fond-detail.html"

    keycloak_scopes = {
        'DEFAULT': 'fond:view',
    }
    api_url_prefix = '/api/fond/'

    def get_context_data(self, **kwargs):
        try:
            context = super(FondDetail, self).get_context_data(**kwargs)
            # Obtain values of the record fond
            context['form'] = FondForm()
            context['fond'] = tools.request_api(self.api_url_prefix + context['id'])
            # Obtain values of related missions
            context['missions'] = tools.request_api(
                '/api/mission?fonds=' + context['id'])
            # Obtain values of items domains for each related mission
            domains_bar_loader = DomainsBarLoader('/api/mission/{id}/items_domains')
            for mission in context['missions']:
                domains_bar_loader.complete_record(mission)
            domains_bar_loader.complete_context(context)
            # Obtain values of related informers
            context['informers'] = tools.request_api(
                self.api_url_prefix + context['id'] + '/informers')
            # Obtain values of related collectors
            context['collectors'] = tools.request_api(
                self.api_url_prefix + context['id'] + '/collectors')
            # Obtain values of related documents
            context['documents'] = tools.request_api(
                self.api_url_prefix + context['id'] + '/document')
            # Obtain values of the start and en dates of related collections
            context['dates'] = tools.request_api(
                self.api_url_prefix + context['id'] + '/dates')
            # Obtain value of the items total duration
            context['duration'] = tools.request_api(
                self.api_url_prefix + context['id'] + '/duration')
        except Http404:
            raise Http404(_('Ce fonds n’existe pas.'))
        except Exception as err:
            context['fond'] = {}
            context['missions'] = []
            context['informers'] = []
            context['collectors'] = []
            context['documents'] = []
            context['dates'] = ['', '']
            context['duration'] = ''
            context['error'] = err
        return context
