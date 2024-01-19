# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import Http404
from django.utils.translation import gettext as _

from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.domain_music import DomainMusicForm
from ... import tools as tools

class DomainMusicDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_music-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'domain_music:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainMusicDetail, self).get_context_data(**kwargs)
            context['domain_music'] = tools.request_api(
                '/api/domain_music/' + context['id'])
            context['form'] = DomainMusicForm()
        except Http404:
            raise Http404(_('Ce genre de musique n’existe pas.'))
        except Exception as err:
            context['domain_music'] = {}
            context['error'] = err
            context['form'] = DomainMusicForm()
        return context
