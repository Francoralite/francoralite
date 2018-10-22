# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.http import HttpResponseRedirect
from django.views.generic.base import View

import requests
from requests.exceptions import RequestException
from settings import FRONT_HOST_URL


class PersonneDelete(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            # raise Exception(id)
            requests.delete(
                FRONT_HOST_URL + '/api/authority/' + str(id)
                )
            return HttpResponseRedirect('/authority/')

        except RequestException:
            return HttpResponseRedirect('/authority/')
