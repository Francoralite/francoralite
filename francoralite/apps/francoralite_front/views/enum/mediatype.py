# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from francoralite.apps.francoralite_front.francoralite_template_view import FrancoraliteTemplateView
import francoralite.apps.francoralite_front.tools as tools


class MediaTypeView(FrancoraliteTemplateView):
    template_name = "../templates/enum/mediatype.html"

    keycloak_scopes = {'GET': 'mediatype:view'}

    def get_context_data(self, **kwargs):
        try:
            context = super(MediaTypeView, self).get_context_data(**kwargs)
            context['mediatypes'] = tools.request_api('/api/mediatype')
        except Exception as err:
            context['mediatypes'] = []
            context['error'] = err

        return context
