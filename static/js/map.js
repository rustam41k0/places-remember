// Coordinates of center of EKB
const DEFAULT_LON = 60.614522838336555;
const DEFAULT_LAT = 56.83597279595725;

const dots = [];

document.addEventListener("DOMContentLoaded", initMap);

function initMap() {
    // Map settings
    const map_view_settings = new ol.View({
        center: ol.proj.fromLonLat([DEFAULT_LON, DEFAULT_LAT]),
        maxZoom: 18,
        zoom: 12,
    })

    const map_layer_settings = new ol.layer.Tile({
        source: new ol.source.OSM({
            url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
            attributions: [ol.source.OSM.ATTRIBUTION, 'Tiles courtesy of <a href="https://geo6.be/">GEO-6</a>'],
        })
    })

    // Attribution settings
    const attribution = new ol.control.Attribution({
        collapsible: true // Hide attribution if size of screen will get too small
    });
    const map_controls_settings = ol.control.defaults({
        attribution: false // Hide attribution by default
    }).extend([attribution]);

    // Map initialization
    const map = new ol.Map({
        controls: map_controls_settings,
        layers: [map_layer_settings],
        target: 'map',
        view: map_view_settings,
    });

    coordinates.forEach(generate_markers)

    const layer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: dots
        })
    });
    map.addLayer(layer);
}

// Generate marker points for OpenLayers map using coordinates
function generate_markers(currentValue) {
    dots.push(
        new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.fromLonLat([currentValue[0], currentValue[1]]))
        }))
}