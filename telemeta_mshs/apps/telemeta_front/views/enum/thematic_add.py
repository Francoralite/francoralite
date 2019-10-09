# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.views.generic.edit import FormView
from telemeta_front.forms.thematic import ThematicForm
import telemeta_front.tools as tools


class ThematicAdd(FormView):
    template_name = "../templates/enum/thematic-add.html"
    form_class = ThematicForm
    success_url = '/thematic/'

    def post(self, request, *args, **kwargs):
        return tools.post('thematic', ThematicForm, request, *args, **kwargs)
