# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.conf.urls import url

from .views import overview

app_name = 'qrcode'
urlpatterns = [
    url(r'^$', overview, name='overview'),
]
