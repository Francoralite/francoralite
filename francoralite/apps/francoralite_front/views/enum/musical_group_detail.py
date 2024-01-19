# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.musical_group import MusicalGroupForm
from ... import tools as tools


class MusicalGroupDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/musical_group-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'musical_group:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(MusicalGroupDetail, self).get_context_data(**kwargs)
            context['musical_group'] = tools.request_api(
                '/api/musical_group/' + context['id'])
            context['form'] = MusicalGroupForm
        except Http404:
            raise Http404(_('Cette formation n’existe pas.'))
        except Exception as err:
            context['musical_group'] = {}
            context['error'] = err
            context['form'] = MusicalGroupForm
        return context
