"use strict";
/* jslint node: true */
/* jshint esversion: 6 */
/* globals customElements */

// CSS
const LEAFLET_CSS_URL= "/static/francoralite_front/css/leaflet/leaflet.css";
const MARKER_CLUSTER_CSS_URL = "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.css"
const MARKER_CLUSTER_DEFAULT_CSS_URL = "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.Default.css";
const CONTROL_GEOCODER_CSS_URL = "https://cdnjs.cloudflare.com/ajax/libs/perliedman-leaflet-control-geocoder/2.4.0/Control.Geocoder.min.css";

// import JS
import "/static/francoralite_front/js/leaflet.js";
import "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/leaflet.markercluster.js";
import "https://cdnjs.cloudflare.com/ajax/libs/perliedman-leaflet-control-geocoder/2.4.0/Control.Geocoder.min.js";


const STYLESHEET = `
#map {
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.leaflet-top .leaflet-control {
  margin-top: 2em;
}
.leaflet-left .leaflet-control {
  margin-left: 2em;
}
.leaflet-bottom .leaflet-control {
  margin-bottom: 2em;
}
.leaflet-right .leaflet-control {
  margin-right: 2em;
}
.leaflet-control.leaflet-control-attribution {
  margin: 0;
  margin-top: -1.5em; /* make this "transparent" to other controls margins  */
}
.leaflet-control-zoom,
.leaflet-touch .leaflet-control-zoom {
  box-shadow: none;
  border: none;
}
.leaflet-control-zoom > a.leaflet-control-zoom-in,
.leaflet-control-zoom > a.leaflet-control-zoom-out,
.leaflet-touch .leaflet-control-zoom > a.leaflet-control-zoom-in,
.leaflet-touch .leaflet-control-zoom > a.leaflet-control-zoom-out {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1.5em;
  height: 1.5em;
  font-size: 26px;
  font-weight: normal;
  color: #E16246;
  border-radius: 50%;
  box-shadow: 0 1px 5px rgb(0 0 0 / 10%);
}
.leaflet-control-zoom > a:first-child {
  margin-bottom: .25em;
}
`;

// francoralite-map

class FrancoraliteMap extends HTMLElement {

  static get observedAttribtues() {
    return ["lat", "lng", "zoom"];
  }

  get lat() {
    return this.getAttribute("lat") || 51;
  }
  get lng() {
    return this.getAttribute("lng") || 0;
  }
  get zoom() {
    return this.getAttribute("zoom") || -1;
  }

  get bounds() {
    return this.getAttribute("bounds") || L.bounds(
      L.point( 50, -85 ),
      L.point( 30, 0 )
  );
  }

  attributeChangedCallback(name, oldValue, newValue) {
    super.attributeChangedCallback(name, oldValue, newValue);

    switch (name) {
      case "lat":
      case "lng":
        this.map && this.map.setView([this.lat, this.lng]);
        break;

      case "zoom":
        this.map && this.map.setZoom(this.zoom);
        break;

      case "bounds":
        this.map && this.map.fitBounds([ [50, -85], [30, 0] ]);
        break;
    }
  }

  constructor() {
    super();

    this.render();

    // ensure we've rendered before initializing

    setTimeout(() => {
      this.initMap();
      this.initView();
      this.initChildren();
    });
  }

  render() {
    this.attachShadow({ mode: "open" });

    const styleEl = document.createElement("style");
    styleEl.textContent = STYLESHEET;
    const leafletStyleEl = document.createElement("link");
    leafletStyleEl.setAttribute("rel", "stylesheet");
    leafletStyleEl.setAttribute("href", LEAFLET_CSS_URL );
    const controlGeocoderStyleEL = document.createElement("link");
    controlGeocoderStyleEL.setAttribute("rel", "stylesheet");
    controlGeocoderStyleEL.setAttribute("href", CONTROL_GEOCODER_CSS_URL);
    const markerClusterStyleEL = document.createElement("link");
    markerClusterStyleEL.setAttribute("rel","stylesheet");
    markerClusterStyleEL.setAttribute("href",MARKER_CLUSTER_CSS_URL);
    const markerClusterDefaultStyleEL = document.createElement("link");
    markerClusterDefaultStyleEL.setAttribute("rel","stylesheet");
    markerClusterDefaultStyleEL.setAttribute("href",MARKER_CLUSTER_DEFAULT_CSS_URL);

    this.mapEl = document.createElement("div");
    this.mapEl.setAttribute("id", "map");

    this.shadowRoot.append(styleEl, leafletStyleEl, controlGeocoderStyleEL, markerClusterStyleEL, markerClusterDefaultStyleEL);
    this.shadowRoot.append(this.mapEl);
  }

  initMap() {

    // Directory of leaflet's icons
    L.Icon.Default.imagePath='/static/francoralite_front/css/leaflet/images/';

    if (this.map) this.map.remove();

    this.map = L.map(this.mapEl, {
      zoomControl: false,
    });

    // Control for the zoom
    L.control
      .zoom({
        position: "bottomright",
      })
      .addTo(this.map);

    // Tile layer and OSM Contributors
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery &copy; <a href="http://mapbox.com">Mapbox</a>',
      maxZoom: 18,
    }).addTo(this.map);

    // Scale Bar
    L.control.scale(
      {
        metric: true,
        imperial: false
      }
    ).addTo(this.map);


    // Add a search control on the map
    // Type of geocoder to use

    let geocoder = L.Control.Geocoder.nominatim({
      geocodingQueryParams:{limit:10,},
    });
    // Create a search control
    L.Control.geocoder({
        collapsed:false,
        placeholder:"Rechercher une localité ...",
        showResultIcons:true,
        geocoder: geocoder,
    })
    .addTo(this.map);


    // Locations of collections
    let markers = L.markerClusterGroup( {
      showCoverageOnHover: true,
      zoomToBoundsOnClick: true,
      removeOutsideVisibleBounds: true
    } );

    this.request_location(markers);
  }

  initView() {
    this.map.setView([this.lat, this.lng], this.zoom);
    if (this.zoom == -1) {
      this.map.fitWorld({ animate: false });
    }
    if(this.bounds) {
      this.map.fitBounds([ [50, -85], [30, 0] ]);
    }
  }

  initChildren() {
    for (let child of this.children) {
      child.container = this.map;
    }

    this.mutationObserver = new MutationObserver((mutations) =>
      mutations.forEach((mutation) => {
        for (let child of mutation.addedNodes) {
          child.container = this.map;
        }

        for (let child of mutation.removedNodes) {
          child.container = null;
        }
      })
    );
    this.mutationObserver.observe(this, { childList: true });
  }

  request_location(markers) {
    // Request the locations of the collections

    let xhr = new XMLHttpRequest();
    xhr.addEventListener('load', (event) => {
      const data = JSON.parse(event.target.response);
      this.collection_marker(data.results !== undefined ? data.results : data, markers);
    });
    xhr.open('GET', '/api/locationgiscollection/', true);
    xhr.send(null);
  }

  collection_marker(locations, markers) {
    // Create the markers and the popup

    for( let loc of locations ) {
      let marker = L.marker([loc.location.latitude,loc.location.longitude]).bindPopup(
        '<h3><a href="/collection/'+loc.collection.id+'">'+
        loc.collection.code+' - '+loc.collection.title+'</a></h3>'+
        '<p>'+loc.collection.descriptions+'</p>'+
        '<hr />'+
        'Lieu : <a href="/location_gis/'+
        loc.location.id+'"><b>'+loc.location.code+
        '</b></a><p>'+loc.location.name+'</p><hr/><i>'+
        loc.location.notes+'</i>' );
        markers.addLayer(marker);
    }
    this.map.addLayer(markers);
  }

}

window.customElements.define("francoralite-map", FrancoraliteMap);