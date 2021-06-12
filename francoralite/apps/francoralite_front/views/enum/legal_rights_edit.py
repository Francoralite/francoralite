# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from francoralite.apps.francoralite_front.forms.legal_rights import LegalRightsForm
from django.shortcuts import render
import francoralite.apps.francoralite_front.tools as tools


class LegalRightsEdit(FormView):
    template_name = "../templates/enum/legal_rights-add.html"
    form_class = LegalRightsForm
    success_url = '/legal_rights/'

    def get_context_data(self, **kwargs):
        context = super(LegalRightsEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/legalrights/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['legal_rights'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        legal_rights = requests.get(
            settings.FRONT_HOST_URL + '/api/legalrights/' + str(id))
        form = LegalRightsForm(initial=legal_rights.json())

        return render(request,
                      '../templates/enum/legal_rights-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'legal_rights', LegalRightsForm, request, *args, **kwargs)
