# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.keyword import KeywordForm
from ... import tools


class KeywordDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/keyword-detail.html"

    keycloak_scopes = {
        'DEFAULT': 'keyword:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(KeywordDetail, self).get_context_data(**kwargs)
            context['keyword'] = tools.request_api(
                '/api/keyword/' + context['id'])
            context['form'] = KeywordForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Ce mot-clé n’existe pas.'))
        except Exception as err:
            context['keyword'] = {}
            context['error'] = err
            context['form'] = KeywordForm()
        return context
