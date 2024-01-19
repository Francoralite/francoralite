# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.domain_song import DomainSongForm
from ... import tools as tools


class DomainSongDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/domain_song-detail.html"
    
    keycloak_scopes = {
        'DEFAULT': 'domain_song:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(DomainSongDetail, self).get_context_data(**kwargs)
            context['domain_song'] = tools.request_api(
                '/api/domain_song/' + context['id'])
            context['form'] = DomainSongForm()
        except Http404:
            raise Http404(_('Ce genre de chanson n’existe pas.'))
        except Exception as err:
            context['domain_song'] = {}
            context['error'] = err
            context['form'] = DomainSongForm()
        return context
