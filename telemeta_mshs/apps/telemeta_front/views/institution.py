# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from rest_framework import status
import requests
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL
from telemeta_front.forms.institution import InstitutionForm
from django.shortcuts import render


class InstitutionView(TemplateView):
    template_name = "../templates/institution.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(InstitutionView, self).get_context_data(**kwargs)
        context['institutions'] = requests.get(
            FRONT_HOST_URL+'/api/institution/').json
        return context


class InstitutionDetail(TemplateView):
    template_name = "../templates/institution-detail.html"

    def get_context_data(self, **kwargs):
        context = super(InstitutionDetail, self).get_context_data(**kwargs)

        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL+'/api/institution/'+context['pk'])
        if response.status_code == status.HTTP_200_OK:
            context['institution'] = response.json
        return context


class InstitutionAdd(FormView):
    template_name = "../templates/institution-add.html"
    form_class = InstitutionForm
    success_url = '/institution/'

    def post(self, request, *args, **kwargs):

        form = InstitutionForm(request.POST)

        if form.is_valid():

            try:
                requests.post(
                    FRONT_HOST_URL + '/api/institution/',
                    data=form.cleaned_data
                )
                return HttpResponseRedirect('/institution/')

            except RequestException:
                return HttpResponseRedirect('/institution/add')

        return HttpResponseRedirect('/institution/add')


class InstitutionDelete(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            # raise Exception(id)
            requests.delete(
                FRONT_HOST_URL + '/api/institution/' + str(id)
                )
            return HttpResponseRedirect('/institution/')

        except RequestException:
            return HttpResponseRedirect('/institution/')


class InstitutionEdit(FormView):
    template_name = "../templates/institution-add.html"
    form_class = InstitutionForm
    success_url = '/institution/'

    def get_context_data(self, **kwargs):
        context = super(InstitutionEdit, self).get_context_data(**kwargs)

        id = kwargs.get('id')
        # Obtain values of the record
        response = requests.get(
            FRONT_HOST_URL + '/api/institution/' + str(id))
        if response.status_code == status.HTTP_200_OK:
            context['institution'] = response.json
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        institution = requests.get(
            FRONT_HOST_URL + '/api/institution/' + str(id))
        form = InstitutionForm(initial=institution.json())

        return render(request,
                      '../templates/institution-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):

        form = InstitutionForm(request.POST)
        id = kwargs.get('id')

        if form.is_valid():
            try:
                response = requests.patch(
                    FRONT_HOST_URL + '/api/institution/' + str(id) + '/',
                    data=form.cleaned_data
                )
                if(response.status_code != status.HTTP_200_OK):
                    return HttpResponseRedirect('/institution/edit')
                return HttpResponseRedirect('/institution/')

            except RequestException:
                return HttpResponseRedirect('/institution/edit')

        return HttpResponseRedirect('/institution/edit')
