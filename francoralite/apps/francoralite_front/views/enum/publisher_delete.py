# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.views.generic.base import View
from ... import tools as tools


class PublisherDelete(View):
    keycloak_scopes = {
        'DEFAULT': 'publisher:delete',
    }
    def get(self, request, *args, **kwargs):
        return tools.delete('publisher', request, *args, **kwargs)
