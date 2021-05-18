# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from telemeta_mshs.apps.telemeta_front.forms.domain_tale import DomainTaleForm
from django.shortcuts import render
import telemeta_mshs.apps.telemeta_front.tools as tools


class DomainTaleEdit(FormView):
    template_name = "../templates/enum/domain_tale-add.html"
    form_class = DomainTaleForm
    success_url = '/domain_tale/'

    def get_context_data(self, **kwargs):
        context = super(DomainTaleEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/domain_tale/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['domain_tale'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        domain_tale = requests.get(
            settings.FRONT_HOST_URL + '/api/domain_tale/' + str(id))
        form = DomainTaleForm(initial=domain_tale.json())

        return render(request,
                      '../templates/enum/domain_tale-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'domain_tale', DomainTaleForm, request, *args, **kwargs)
