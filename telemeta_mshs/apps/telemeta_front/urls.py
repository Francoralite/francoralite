# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.conf.urls import url, include

from .views import (
    home as telemeta_front_home
)


urlpatterns = [
    url(r'^$', telemeta_front_home.HomePageView.as_view(), name="telemeta-home-new"),
]
