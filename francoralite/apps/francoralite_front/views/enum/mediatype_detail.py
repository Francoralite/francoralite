# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.http import Http404
from django.utils.translation import gettext as _
from ...francoralite_template_view import FrancoraliteTemplateView
from ...forms.mediatype import MediaTypeForm
from ... import tools as tools


class MediaTypeDetail(FrancoraliteTemplateView):
    template_name = "../templates/enum/mediatype-detail.html"
    keycloak_scopes = {
        'DEFAULT': 'mediatype:view',
    }

    def get_context_data(self, **kwargs):
        try:
            context = super(MediaTypeDetail, self).get_context_data(**kwargs)
            context['mediatype'] = tools.request_api(
                '/api/mediatype/' + context['id'])
            context['form'] = MediaTypeForm()
        except Http404:
            raise Http404(_('Ce type de média n’existe pas.'))
        except Exception as err:
            context['mediatype'] = {}
            context['error'] = err
            context['form'] = MediaTypeForm()
        return context
