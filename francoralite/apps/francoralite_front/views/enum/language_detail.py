# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.language import LanguageForm
from ... import tools as tools


class LanguageDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/language-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'language:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(LanguageDetail, self).get_context_data(**kwargs)
            context['language'] = tools.request_api(
                '/api/language/' + context['id'])
            context['form'] = LanguageForm()
        except Http404:
            raise Http404(_('Cette langue n’existe pas.'))
        except Exception as err:
            context['language'] = {}
            context['error'] = err
            context['form'] = LanguageForm()
        return context
