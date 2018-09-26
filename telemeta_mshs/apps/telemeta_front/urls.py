# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.conf.urls import url, include

from views import (
    home as home2
)


urlpatterns = [
    url(r'^$', home2.home, name="telemeta-home"),
    # Telemeta orignal app
    url(r'', include('telemeta.urls')),

    ]
