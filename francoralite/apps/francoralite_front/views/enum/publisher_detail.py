# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.publisher import PublisherForm
from ... import tools as tools


class PublisherDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/publisher-detail.html"
    
    keycloak_scopes = {
        'DEFAULT': 'publisher:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(PublisherDetail, self).get_context_data(**kwargs)
            context['publisher'] = tools.request_api(
                '/api/publisher/' + context['id'])
            context['form'] = PublisherForm()
        except Http404:
            raise Http404(_('Cet éditeur n’existe pas.'))
        except Exception as err:
            context['publisher'] = {}
            context['error'] = err
            context['form'] = PublisherForm()
        return context
