// Coordinates of center of EKB
const DEFAULT_LON = 60.614522838336555;
const DEFAULT_LAT = 56.83597279595725;

const dots = [];

document.addEventListener("DOMContentLoaded", initMap);

/**
 * Initializing function, invokes on document "document ready" event.
 */
function initMap() {
    // Map settings
    // Docs: https://openlayers.org/en/latest/apidoc/module-ol_Map-Map.html
    const map_layer_settings = new ol.layer.Tile({
        source: new ol.source.OSM({
            // Map source
            url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
            // Map authors
            attributions: [ol.source.OSM.ATTRIBUTION, 'Tiles courtesy of <a href="https://geo6.be/">GEO-6</a>'],
        })
    })

    const map_view_settings = new ol.View({
        center: ol.proj.fromLonLat([DEFAULT_LON, DEFAULT_LAT]),
        maxZoom: 18,
        zoom: 12,
    })

    // Attribution settings
    // Docs: https://openlayers.org/en/latest/examples/attributions.html
    const attribution = new ol.control.Attribution({
        collapsible: true // Hide attribution if size of screen will get too small
    });
    // Docs: https://openlayers.org/en/latest/examples/overviewmap.html
    const map_controls_settings = ol.control.defaults({
        attribution: false // Hide attribution by default
    }).extend([attribution]);

    // Map initialization
    const map = new ol.Map({
        controls: map_controls_settings,
        layers: [
            map_layer_settings,
            new ol.layer.Vector({
                source: vectorSource
            })],
        target: 'map',
        view: map_view_settings,
    });

    var addedMarker = new ol.geom.Point([
        ol.proj.transform(coords, 'EPSG:4326', 'EPSG:3857')]);

    var featurething = new ol.Feature({
        name: "Marker 01",
        geometry: addedMarker
    });

    vectorSource.addFeature(featurething);

    const layer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.fromLonLat([4.35247, 50.84673]))
            })
        })
    });

    map.addLayer(layer);
}