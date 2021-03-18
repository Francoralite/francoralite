# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from telemeta_front.forms.metadata_author import MetadataAuthorForm
from django.shortcuts import render
import telemeta_front.tools as tools


class MetadataAuthorEdit(FormView):
    template_name = "../templates/enum/metadata_author-add.html"
    form_class = MetadataAuthorForm
    success_url = '/metadata_author/'

    def get_context_data(self, **kwargs):
        context = super(MetadataAuthorEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/metadata_author/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['metadata_author'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        metadata_author = requests.get(
            settings.FRONT_HOST_URL + '/api/metadata_author/' + str(id))
        form = MetadataAuthorForm(initial=metadata_author.json())

        return render(request,
                      '../templates/enum/metadata_author-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'metadata_author', MetadataAuthorForm, request, *args, **kwargs)
