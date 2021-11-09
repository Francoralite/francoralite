# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from rest_framework import status
import requests
from django.conf import settings
from francoralite.apps.francoralite_front.forms.mission import MissionForm
from django.shortcuts import render
import francoralite.apps.francoralite_front.tools as tools

from ..forms.mission import MissionForm
from ..francoralite_template_view import FrancoraliteFormView


class MissionEdit(FrancoraliteFormView):
    api_url_prefix = '/api/mission/'
    entity_name = 'mission'
    template_name = "../templates/mission-add.html"
    form_class = MissionForm
    success_url = '/mission/'
    
    keycloak_scopes = {
        'DEFAULT': 'authority:update',
    }
