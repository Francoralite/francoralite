# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
import requests
from django.conf import settings
from francoralite.apps.francoralite_front.forms.institution import InstitutionForm
from django.shortcuts import render
import francoralite.apps.francoralite_front.tools as tools


class InstitutionEdit(FormView):
    template_name = "../templates/institution-add.html"
    form_class = InstitutionForm
    success_url = '/institution/'

    def get_context_data(self, **kwargs):
        try:
            context = super(InstitutionEdit, self).get_context_data(**kwargs)
            id = kwargs.get('id')
            # Obtain values of the record
            context['institution'] = tools.request_api(
                '/api/institution/' + str(id))
        except Exception as err:
            context['institution'] = {}
            context['error'] = err.message
        return context

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        # Obtain values of the record
        institution = requests.get(
            settings.FRONT_HOST_URL + '/api/institution/' + str(id))
        form = InstitutionForm(initial=institution.json())

        return render(request,
                      '../templates/institution-add.html',
                      {'form': form, 'id': id})

    def post(self, request, *args, **kwargs):
        return tools.patch(
            'institution', InstitutionForm, request, *args, **kwargs)
