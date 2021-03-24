# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from telemeta_mshs.apps.telemeta_front.forms.mediatype import MediaTypeForm
from django.shortcuts import render
import telemeta_mshs.apps.telemeta_front.tools as tools


class MediaTypeEdit(FormView):
    template_name = "../templates/enum/mediatype-add.html"
    form_class = MediaTypeForm
    success_url = '/mediatype/'

    def get_context_data(self, **kwargs):
        context = super(MediaTypeEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            settings.FRONT_HOST_URL + '/api/mediatype/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['mediatype'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        mediatype = requests.get(
            settings.FRONT_HOST_URL + '/api/mediatype/' + str(id))
        form = MediaTypeForm(initial=mediatype.json())

        return render(request,
                      '../templates/enum/mediatype-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'mediatype', MediaTypeForm, request, *args, **kwargs)
