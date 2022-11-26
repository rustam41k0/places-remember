const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url);
const map = L.map("map", {layers: [osm]});
map.locate()
    .on("locationfound", (e) => map.setView(e.latlng, 11))
    .on("locationerror", () => map.setView([0, 0], 5))
    .on('click', (e) => {
        L.popup(latlng, {content: '<p>Hello world!<br />This is a nice popup.</p>'}).openOn(map);
        // L.marker(e.latlng).addTo(map);
        // map.setView(e.latlng, 16)
    })