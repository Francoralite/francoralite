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
    personne, personne_add, personne_detail, personne_edit, personne_delete,
    location, location_add, location_detail, location_edit, location_delete
)


urlpatterns = [
    url(r'^$', home_integration.HomePageView.as_view(), name="home"),

    # Institutions
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

    # Authority  (Personnes)
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
    url(r'^authority/delete/(?P<id>[0-9]+)$',
        personne_delete.PersonneDelete.as_view(),
        name='personne-delete'),

    # Location ( Lieux)
    url(r'^location/$', location.LocationView.as_view(),
        name="location"),
    url(r'^location/add/$',
        location_add.LocationAdd.as_view(),
        name='location-add'),
    url(r'^location/(?P<id>[0-9]+)/$',
        location_detail.LocationDetail.as_view(),
        name='location-detail'),
    url(r'^location/edit/(?P<id>[0-9]+)$',
        location_edit.LocationEdit.as_view(),
        name='location-edit'),
    url(r'^location/delete/(?P<id>[0-9]+)$',
        location_delete.LocationDelete.as_view(),
        name='location-delete'),
]
