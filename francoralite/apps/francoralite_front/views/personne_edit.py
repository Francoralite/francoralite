# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
import requests
from django.conf import settings
from francoralite.apps.francoralite_front.forms.personne import PersonneForm
from django.shortcuts import render
import francoralite.apps.francoralite_front.tools as tools


class PersonneEdit(FormView):
    template_name = "../templates/personne-add.html"
    form_class = PersonneForm
    success_url = '/authority/'

    keycloak_scopes = {
            'GET': 'authority:view',
            'POST': 'authority:add',
            'PATCH': 'authority:update',
            'PUT': 'authority:update'}

    def get_context_data(self, **kwargs):
        try:
            context = super(PersonneEdit, self).get_context_data(**kwargs)
            id = kwargs.get('id')
            # Obtain values of the record
            context['personne'] = tools.request_api(
                '/api/authority/' + str(id))
        except Exception as err:
            context['personne'] = {}
            context['error'] = err
        return context

    def get(self, request, *args, **kwargs):

        id_auth = kwargs.get('id')

        # Obtain values of the record
        personne = requests.get(
            settings.FRONT_HOST_URL + '/api/authority/' + str(id_auth))
        data = personne.json()
        form = PersonneForm(initial=data)
        authority = personne.json()

        return render(request,
                      '../templates/personne-add.html',
                      {'form': form, 'id': id_auth, 'personne': authority})

    def post(self, request, *args, **kwargs):
        return tools.patch('authority', PersonneForm, request, *args, **kwargs)
