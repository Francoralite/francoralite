# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.base import TemplateView
from rest_framework import status
import requests


class InstitutionView(TemplateView):
    template_name = "../templates/institution.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(InstitutionView, self).get_context_data(**kwargs)
        context['institutions'] = requests.get(
            'http://localhost:8000/api/institution/').json
        return context


class InstitutionDetail(TemplateView):
    template_name = "../templates/institution-detail.html"

    def get_context_data(self, **kwargs):
        context = super(InstitutionDetail, self).get_context_data(**kwargs)

        # Obtain values of the record
        response = requests.get(
            'http://localhost:8000/api/institution/'+context['pk'])
        if response.status_code == status.HTTP_200_OK:
            context['institution'] = response.json
        return context
