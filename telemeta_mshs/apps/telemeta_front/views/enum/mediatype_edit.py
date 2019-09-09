# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from rest_framework import status
import requests
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.mediatype import MediaTypeForm
from django.shortcuts import render


class MediaTypeEdit(FormView):
    template_name = "../templates/enum/mediatype-add.html"
    form_class = MediaTypeForm
    success_url = '/mediatype/'

    def get_context_data(self, **kwargs):
        context = super(MediaTypeEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/mediatype/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['mediatype'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        mediatype = requests.get(
            FRONT_HOST_URL + '/api/mediatype/' + str(id))
        form = MediaTypeForm(initial=mediatype.json())

        return render(request,
                      '../templates/enum/mediatype-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = MediaTypeForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/mediatype/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/mediatype/edit/' +
                                                str(id))
                return HttpResponseRedirect('/mediatype/')

            except RequestException:
                return HttpResponseRedirect('/mediatype/edit')

        return HttpResponseRedirect('/mediatype/edit')
