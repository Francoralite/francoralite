# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_mshs.apps.telemeta_front.tools as tools


class MusicalOrganizationView(FrancoraliteTemplateView):
    template_name = "../templates/enum/musical_organization.html"

    keycloak_scopes = {
        'GET': 'musical_organization:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(MusicalOrganizationView, self).get_context_data(
                **kwargs)
            context['musical_organizations'] = tools.request_api(
                '/api/musical_organization')
        except Exception as err:
            context['musical_organizations'] = []
            context['error'] = err.message

        return context
