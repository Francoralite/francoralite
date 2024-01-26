# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.instrument import InstrumentForm
from ... import tools


class InstrumentDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/instrument-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'instrument:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(InstrumentDetail, self).get_context_data(**kwargs)
            context['instrument'] = tools.request_api(
                '/api/instrument/' + context['id'])
            context['form'] = InstrumentForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cet instrument n’existe pas.'))
        except Exception as err:
            context['instrument'] = {}
            context['error'] = err
            context['form'] = InstrumentForm()
        return context
