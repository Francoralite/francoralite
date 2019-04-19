# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
import telemeta_front.tools as tools


class MediaTypeView(FrancoraliteTemplateView):
    template_name = "../templates/enum/mediatype.html"

    keycloak_scopes = {'GET': 'mediatype:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(MediaTypeView, self).get_context_data(**kwargs)
            context['mediatype'] = tools.request_api('/api/mediatype/')
        except Exception as err:
            context['mediatype'] = []
            context['error'] = err.message

        return context
