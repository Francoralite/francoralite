# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.base import View
import francoralite.apps.francoralite_front.tools as tools


class InstitutionDelete(View):
    def get(self, request, *args, **kwargs):
        return tools.delete('institution', request, *args, **kwargs)
