# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
import requests
from settings import FRONT_HOST_URL
from telemeta_front.forms.collection import CollectionForm
from django.shortcuts import render
import telemeta_front.tools as tools


class CollectionEdit(FormView):
    template_name = "../templates/collection-add.html"
    form_class = CollectionForm
    success_url = '/collection/'
    keycloak_scopes = {
            'GET': 'collection:view',
            'POST': 'collection:add',
            'PATCH': 'collection:update',
            'PUT': 'collection:update'}

    def get_context_data(self, **kwargs):
        try:
            context = super(CollectionEdit, self).get_context_data(**kwargs)
            id = kwargs.get('id')
            # Obtain values of the record
            context['collection'] = tools.request_api(
                '/api/collection/' + str(id) + '/complete')
        except Exception as err:
            context['collection'] = {}
            context['error'] = err.message
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        data = tools.request_api(
          '/api/collection/'+str(id)+'/complete')
        data['mission'] = data['mission']['id']
        if data['media_type']:
            data['media_type'] = data['media_type']['id']
        if data['legal_rights']:
            data['legal_rights'] = data['legal_rights']['id']

        form = CollectionForm(initial=data)

        return render(request,
                      '../templates/collection-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'collection', CollectionForm, request, *args, **kwargs)
