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
from telemeta_front.forms.domain_music import DomainMusicForm
from django.shortcuts import render


class DomainMusicEdit(FormView):
    template_name = "../templates/enum/domain_music-add.html"
    form_class = DomainMusicForm
    success_url = '/domain_music/'

    def get_context_data(self, **kwargs):
        context = super(DomainMusicEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/domain_music/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['domain_music'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        domain_music = requests.get(
            FRONT_HOST_URL + '/api/domain_music/' + str(id))
        form = DomainMusicForm(initial=domain_music.json())

        return render(request,
                      '../templates/enum/domain_music-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = DomainMusicForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/domain_music/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/domain_music/edit' + str(id)
                                                + '/')
                return HttpResponseRedirect('/domain_music/')

            except RequestException:
                return HttpResponseRedirect('/domain_music/edit')

        return HttpResponseRedirect('/domain_music/edit')
