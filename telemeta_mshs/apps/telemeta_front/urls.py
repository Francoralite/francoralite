# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.conf.urls import url

from .views import (
    home as home_integration,
    institution as institution_integration
)


urlpatterns = [
    url(r'^$', home_integration.HomePageView.as_view(), name="home"),
    url(r'^institution/$', institution_integration.InstitutionView.as_view(),
        name="institution"),
    url(r'^institution/(?P<id>[0-9]+)/$',
        institution_integration.InstitutionDetail.as_view(),
        name='institution-detail'),
    url(r'^institution/add/$',
        institution_integration.InstitutionAdd.as_view(),
        name='institution-add'),
    url(r'^institution/edit/(?P<id>[0-9]+)$',
        institution_integration.InstitutionEdit.as_view(),
        name='institution-edit'),
    url(r'^institution/delete/(?P<id>[0-9]+)$',
        institution_integration.InstitutionDelete.as_view(),
        name='institution-delete'),
]
