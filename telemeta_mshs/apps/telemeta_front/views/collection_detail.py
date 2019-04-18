# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from telemeta_front.francoralite_template_view import FrancoraliteTemplateView
from rest_framework import status
import requests

from settings import FRONT_HOST_URL
from telemeta_front.forms.collection import CollectionForm


class CollectionDetail(FrancoraliteTemplateView):
    template_name = "../templates/collection-detail.html"

    def get_context_data(self, **kwargs):
        context = super(CollectionDetail, self).get_context_data(**kwargs)

        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL+'/api/collection/'+context['id']+'/complete/')
        if response.status_code == status.HTTP_200_OK:
            # Values of the collection
            context['collection'] = response.json
            context['form'] = CollectionForm()

        return context
