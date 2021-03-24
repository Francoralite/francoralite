# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_mshs.apps.telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_mshs.apps.telemeta_front.tools as tools
from telemeta_mshs.apps.telemeta_front.forms.musical_organization import MusicalOrganizationForm


class MusicalOrganizationDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/musical_organization-detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super(MusicalOrganizationDetail, self).get_context_data(
                **kwargs)
            # Obtain values of the record
            context['musical_organization'] = tools.request_api(
                '/api/musical_organization/' + context['id'])
            context['form'] = MusicalOrganizationForm()
        except Exception as err:
            context['musical_organization'] = {}
            context['form'] = MusicalOrganizationForm()
            context['error'] = err.message
        return context
