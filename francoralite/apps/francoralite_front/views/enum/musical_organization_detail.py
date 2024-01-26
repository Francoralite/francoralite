# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.musical_organization import MusicalOrganizationForm
from ... import tools


class MusicalOrganizationDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/musical_organization-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'musical_organization:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(MusicalOrganizationDetail, self).get_context_data(
                **kwargs)
            # Obtain values of the record
            context['musical_organization'] = tools.request_api(
                '/api/musical_organization/' + context['id'])
            context['form'] = MusicalOrganizationForm()
        except Http404:
            raise tools.UserMessageHttp404(_('Cette organisation musicale n’existe pas.'))
        except Exception as err:
            context['musical_organization'] = {}
            context['form'] = MusicalOrganizationForm()
            context['error'] = err
        return context
