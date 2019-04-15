# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.base import TemplateView
import telemeta_front.tools as tools


class MusicalOrganizationView(TemplateView):
    template_name = "../templates/enum/musical_organization.html"

    keycloak_scopes = {
        'GET': 'musical_organization:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(MusicalOrganizationView, self).get_context_data(
                **kwargs)
            context['musical_organizations'] = tools.request_api(
                '/api/musical_organization/')
        except Exception as err:
            context['musical_organizations'] = []
            context['error'] = err.message

        return context
