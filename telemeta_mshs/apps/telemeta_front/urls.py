# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.conf.urls import url

from .views import (
    home as home_integration,
    institution, institution_add, institution_delete, institution_detail,
    institution_edit,
    personne, personne_add, personne_detail, personne_edit
)


urlpatterns = [
    url(r'^$', home_integration.HomePageView.as_view(), name="home"),
    url(r'^institution/$', institution.InstitutionView.as_view(),
        name="institution"),
    url(r'^institution/(?P<id>[0-9]+)/$',
        institution_detail.InstitutionDetail.as_view(),
        name='institution-detail'),
    url(r'^institution/add/$',
        institution_add.InstitutionAdd.as_view(),
        name='institution-add'),
    url(r'^institution/edit/(?P<id>[0-9]+)$',
        institution_edit.InstitutionEdit.as_view(),
        name='institution-edit'),
    url(r'^institution/delete/(?P<id>[0-9]+)$',
        institution_delete.InstitutionDelete.as_view(),
        name='institution-delete'),
    url(r'^authority/$', personne.PersonneView.as_view(),
        name="personne"),
    url(r'^authority/add/$',
        personne_add.PersonneAdd.as_view(),
        name='personne-add'),
    url(r'^authority/(?P<id>[0-9]+)/$',
        personne_detail.PersonneDetail.as_view(),
        name='personne-detail'),
    url(r'^authority/edit/(?P<id>[0-9]+)$',
        personne_edit.PersonneEdit.as_view(),
        name='personne-edit'),
]
