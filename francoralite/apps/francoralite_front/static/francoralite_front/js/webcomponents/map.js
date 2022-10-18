"use strict";
/* jslint node: true */
/* jshint esversion: 6 */
/* globals customElements, L */


// Settings
const DEFAULT_BOUNDS = [[50, -85], [30, 0]];
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
import {MarkdownBlock, MarkdownSpan, MarkdownElement} from "/static/francoralite_front/js/md-block.js";



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

  static get observedAttributes() {
    return ["lat", "lng", "zoom", "bounds", "markers-url", "markers-list", "markers-drag"];
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

  get markersUrl() {
    return this.getAttribute("markers-url");
  }

  set markersUrl(url) {
    this.setAttribute("markers-url", url);
  }

  get markersList() {
    return JSON.parse(this.getAttribute("markers-list") || "null");
  }

  get markersDrag() {
    return this.getAttribute("markers-drag") === 'yes';
  }

  attributeChangedCallback(name, oldValue, newValue) {
    // super.attributeChangedCallback(name, oldValue, newValue);

    switch (name) {
      case "lat":
      case "lng":
        if (this.map) {
          this.map.setView([this.lat, this.lng]);
        }
        break;

      case "zoom":
        if (this.map) {
          this.map.setZoom(this.zoom);
        }
        break;

      case "bounds":
        if (this.map) {
          this.map.fitBounds(this.bounds);
        }
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
    markerClusterStyleEL.setAttribute("rel", "stylesheet");
    markerClusterStyleEL.setAttribute("href", MARKER_CLUSTER_CSS_URL);
    const markerClusterDefaultStyleEL = document.createElement("link");
    markerClusterDefaultStyleEL.setAttribute("rel", "stylesheet");
    markerClusterDefaultStyleEL.setAttribute("href", MARKER_CLUSTER_DEFAULT_CSS_URL);

    this.mapEl = document.createElement("div");
    this.mapEl.setAttribute("id", "map");

    this.shadowRoot.append(styleEl, leafletStyleEl, controlGeocoderStyleEL, markerClusterStyleEL, markerClusterDefaultStyleEL);
    this.shadowRoot.append(this.mapEl);
  }

  initMap() {

    // Directory of leaflet's icons
    L.Icon.Default.imagePath='/static/francoralite_front/css/leaflet/images/';

    if (this.map) {
      this.map.remove();
    }

    this.map = L.map(this.mapEl, {
      zoomControl: false,
    });

    // Control for the zoom
    L.control.zoom({
      position: "topleft",
    })
    .addTo(this.map);

    // Tile layer and OSM Contributors
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 18,
    }).addTo(this.map);

    // Scale Bar
    L.control.scale({
      metric: true,
      imperial: false,
    })
    .addTo(this.map);

    // Add a search control on the map
    // Type of geocoder to use
    let geocoder = L.Control.Geocoder.nominatim({
      geocodingQueryParams: {limit: 10,},
    });
    // Create a search control
    L.Control.geocoder({
      collapsed: false,
      placeholder: "Rechercher une localité ...",
      showResultIcons: true,
      geocoder: geocoder,
      defaultMarkGeocode: false,
    })
    .on('markgeocode', (e) => {
      // When a geocoding is performed
      //  a marker with the new geocoded data is updated
      this.setNodeValue("#id_latitude",  e.geocode.center.lat);
      this.setNodeValue("#id_longitude", e.geocode.center.lng);
      this.setNodeValue("#id_name", e.geocode.properties.display_name);

      // Create the marker with "dragend" listener
      this.map.fitBounds(e.geocode.bbox);
      if (this._previousGeocodeMarker) {
        this.map.removeLayer(this._previousGeocodeMarker);
      }
      this._previousGeocodeMarker = L.marker(
        e.geocode.center,
        {draggable: this.markersDrag}
      )
      .addTo(this.map)
      .bindPopup(e.geocode.html || e.geocode.name)
      .openPopup()
      .on("dragend", (e) => {
        let changedPos = e.target.getLatLng();
        this.setNodeValue("#id_latitude", changedPos.lat);
        this.setNodeValue("#id_longitude", changedPos.lng);
      });
    })
    .addTo(this.map);

    // Markers layer
    let markersLayer = L.markerClusterGroup({
      showCoverageOnHover: true,
      zoomToBoundsOnClick: true,
      removeOutsideVisibleBounds: true,
    });

    if (this.markersList) {
      // There's a markers list !
      this.addMarkers(this.markersList, markersLayer);
    } else if(!this.markersUrl) {
      this.markersUrl = '/api/locationgis';
      this.requestMarkers(markersLayer);
    } else {
      // ... using the API request
      this.requestMarkers(markersLayer, this.markersDrag);
    }
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

  requestMarkers(markersLayer, dragMarkers='') {
    // Request the locations of the collections
    if (this.markersUrl) {
      let xhr = new XMLHttpRequest();
      xhr.addEventListener('load', (event) => {
        const data = JSON.parse(event.target.response);
        this.addMarkers(data.results !== undefined ? data.results : data, markersLayer, dragMarkers);
      });
      xhr.open('GET', this.markersUrl, true);
      xhr.send(null);
    }
  }

  addMarkers(locations, markersLayer, dragMarkers) {
    // Create the markers and the popup

    // A function to create the markers
    let createMarker = (loc) => {
      if (loc.collection && loc.location) {
        // It's a Collection-Location
        markersLayer.addLayer(
          L.marker(
            [loc.location.latitude, loc.location.longitude],
            {draggable: dragMarkers}
          ).bindTooltip(
            "Code : " + loc.collection.code + "<br>" +
            "Titre : " + loc.collection.title + "<br>" +
            "Lieu : " + loc.location.code
          ).bindPopup(
            '<h4><a href="/collection/' + loc.collection.id + '">' +
            loc.collection.code + ' - ' + loc.collection.title + '</a></h4>' +
            '<p><md-block>' + loc.collection.description + '</md-block></p>' +
            '<hr />' +
            'Lieu : <a href="/location_gis/' +
            loc.location.id + '"><b>' + loc.location.code +
            '</b></a><p>' + loc.location.name + '</p><hr/><i>' +
            loc.location.notes + '</i>'
          ).on("dragend", (e) => {
            let changedPos = e.target.getLatLng();
            this.setNodeValue("#id_latitude", changedPos.lat);
            this.setNodeValue("#id_longitude", changedPos.lng);
          })
        );
      } else {
        // It's a Location, only
        markersLayer.addLayer(
          L.marker(
            [loc.latitude, loc.longitude],
            {draggable: dragMarkers}
          ).bindTooltip(
            "Code : " + loc.code + "<br>" +
            "Nom : " + loc.name + "<br>"
          ).bindPopup(
            'Lieu : <a href="/location_gis/' +
            loc.id + '"><b>' + loc.code +
            '</b></a><p>' + loc.name + '</p><hr/><i>' +
            loc.notes + '</i>'
          ).on("dragend", (e) => {
            let changedPos = e.target.getLatLng();
            this.setNodeValue("#id_latitude", changedPos.lat);
            this.setNodeValue("#id_longitude", changedPos.lng);
          })
        );
      }
    };

    // Test the type of the locations
    if (Array.isArray(locations)) {
      locations.forEach(loc => createMarker(loc));
    } else {
      createMarker(locations);
    }

    // Add on the map this new layer
    this.map.addLayer(markersLayer);
  }

  setNodeValue(nodeSelector, value) {
    const node = document.querySelector(nodeSelector);
    if (node instanceof HTMLInputElement) {
      node.value = value;
    } else if (node) {
      node.innerHTML = value;
    }
  }
}

customElements.define("francoralite-map", FrancoraliteMap);
