"use strict";
/* jslint node: true */
/* jshint esversion: 6 */
/* globals customElements */

// Settings
const API_REQUEST_URL = "/api/locationgiscollection/";
const DEFAULT_BOUNDS = [ [50, -85], [30, 0] ];
const DEFAULT_LAT = 46.56920;
const DEFAULT_LNG = 0.38523;
const DEFAULT_ZOOM = 19;

// CSS
const LEAFLET_CSS_URL= "/static/francoralite_front/css/leaflet/leaflet.css";
const MARKER_CLUSTER_CSS_URL = "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.css";
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
  font-size: 14px;
}
`;

// francoralite-map

class FrancoraliteMap extends HTMLElement {

  static get observedAttribtues() {
    return ["lat", "lng", "zoom", "bounds"];
  }

  get lat() {
    return this.getAttribute("lat");
  }

  get lng() {
    return this.getAttribute("lng");
  }

  get zoom() {
    return this.getAttribute("zoom");
  }

  get bounds() {
    return JSON.parse(this.getAttribute("bounds") || "null");
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
        this.map && this.map.fitBounds(this.bounds);
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
        position: "topleft",
      })
      .addTo(this.map);

    // Tile layer and OSM Contributors
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
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
    if (this.zoom === -1) {
      this.map.fitWorld({animate: false});
    } else if (this.lat && this.lng || this.zoom) {
      this.map.setView([this.lat || DEFAULT_LAT, this.lng || DEFAULT_LNG], this.zoom || DEFAULT_ZOOM);
    } else {
      this.map.fitBounds(this.bounds || DEFAULT_BOUNDS);
    }
  }

  request_location(markers) {
    // Request the locations of the collections

    let xhr = new XMLHttpRequest();
    xhr.addEventListener('load', (event) => {
      const data = JSON.parse(event.target.response);
      this.collection_marker(data.results !== undefined ? data.results : data, markers);
    });
    xhr.open('GET', API_REQUEST_URL, true);
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