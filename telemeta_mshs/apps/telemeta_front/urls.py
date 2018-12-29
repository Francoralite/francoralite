# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.conf.urls import url, include

from .views import (
    home as home_integration,
    institution, institution_add, institution_delete, institution_detail,
    institution_edit,
    personne, personne_add, personne_detail, personne_edit, personne_delete,
    location, location_add, location_detail, location_edit, location_delete,
    location_gis, location_gis_add, location_gis_detail, location_gis_edit,
    location_gis_delete,
    fond, fond_add, fond_detail, fond_edit, fond_delete,
    mission, mission_add, mission_detail, mission_edit, mission_delete,
    collection, collection_add, collection_detail, collection_edit,
    collection_delete,
)

from .views.enum import (
    instrument, instrument_edit, instrument_delete, instrument_detail
)


urlpatterns = [
    url(r'^$', home_integration.HomePageView.as_view(), name="home"),
    url(r'^select2/', include('django_select2.urls')),

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

    # Location GIS ( Lieux)
    url(r'^location_gis/$', location_gis.LocationView.as_view(),
        name="location_gis"),
    url(r'^location_gis/add/$',
        location_gis_add.LocationAdd.as_view(),
        name='location_gis-add'),
    url(r'^location_gis/(?P<id>[0-9]+)/$',
        location_gis_detail.LocationDetail.as_view(),
        name='location_gis-detail'),
    url(r'^location_gis/edit/(?P<id>[0-9]+)$',
        location_gis_edit.LocationEdit.as_view(),
        name='location_gis-edit'),
    url(r'^location_gis/delete/(?P<id>[0-9]+)$',
        location_gis_delete.LocationDelete.as_view(),
        name='location_gis-delete'),

    # Fonds
    url(r'^fond/$', fond.FondView.as_view(),
        name="fond"),
    url(r'^fond/add/$',
        fond_add.FondAdd.as_view(),
        name='fond-add'),
    url(r'^fond/(?P<id>[0-9]+)/$',
        fond_detail.FondDetail.as_view(),
        name='fond-detail'),
    url(r'^fond/edit/(?P<id>[0-9]+)$',
        fond_edit.FondEdit.as_view(),
        name='fond-edit'),
    url(r'^fond/delete/(?P<id>[0-9]+)$',
        fond_delete.FondDelete.as_view(),
        name='fond-delete'),

    # Mission
    url(r'^mission/$', mission.MissionView.as_view(),
        name="mission"),
    url(r'^institution/(?P<id_institution>[0-9]+)/fond/(?P<id_fond>[0-9]+)/mission/add/$',  # noqa
        mission_add.MissionAdd.as_view(),
        name='mission-add'),
    url(r'^mission/(?P<id>[0-9]+)/$',
        mission_detail.MissionDetail.as_view(),
        name='mission-detail'),
    url(r'^mission/edit/(?P<id>[0-9]+)$',
        mission_edit.MissionEdit.as_view(),
        name='mission-edit'),
    url(r'^mission/delete/(?P<id>[0-9]+)$',
        mission_delete.MissionDelete.as_view(),
        name='mission-delete'),

    # Collection/Enquetes
    url(r'^collection/$', collection.CollectionView.as_view(),
        name="collection"),
    url(r'^institution/(?P<id_institution>[0-9]+)/fond/(?P<id_fond>[0-9]+)/mission/(?P<id_mission>[0-9]+)/collection/add/$',  # noqa
        collection_add.CollectionAdd.as_view(),
        name='collection-add'),
    url(r'^collection/(?P<id>[0-9]+)/$',
        collection_detail.CollectionDetail.as_view(),
        name='collection-detail'),
    url(r'^collection/edit/(?P<id>[0-9]+)$',
        collection_edit.CollectionEdit.as_view(),
        name='collection-edit'),
    url(r'^collection/delete/(?P<id>[0-9]+)$',
        collection_delete.CollectionDelete.as_view(),
        name='collection-delete'),

    # Instruments
    url(r'^instrument/$', instrument.InstrumentView.as_view(),
        name="instrument"),
    # url(r'^fond/add/$',
    #     fond_add.FondAdd.as_view(),
    #     name='fond-add'),
    url(r'^instrument/(?P<id>[0-9]+)/$',
     instrument_detail.InstrumentDetail.as_view(),
     name='instrument-detail'),
    url(r'^instrument/edit/(?P<id>[0-9]+)$',
         instrument_edit.InstrumentEdit.as_view(),
         name='instrument-edit'),
    url(r'^instrument/delete/(?P<id>[0-9]+)$',
        instrument_delete.InstrumentDelete.as_view(),
        name='instrument-delete'),
]
