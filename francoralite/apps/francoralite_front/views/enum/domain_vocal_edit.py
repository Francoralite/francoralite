# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from francoralite.apps.francoralite_front.forms.domain_vocal import DomainVocalForm
from django.shortcuts import render
import francoralite.apps.francoralite_front.tools as tools


class DomainVocalEdit(FormView):
    template_name = "../templates/enum/domain_vocal-add.html"
    form_class = DomainVocalForm
    success_url = '/domain_vocal/'

    def get_context_data(self, **kwargs):
        context = super(DomainVocalEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/domain_vocal/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['domain_vocal'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        domain_vocal = requests.get(
            settings.FRONT_HOST_URL + '/api/domain_vocal/' + str(id))
        form = DomainVocalForm(initial=domain_vocal.json())

        return render(request,
                      '../templates/enum/domain_vocal-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'domain_vocal', DomainVocalForm, request, *args, **kwargs)