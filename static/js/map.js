function initMap() {
    console.log(stores);
    var Options = {
        zoom: 10, //地図の縮尺値を指定
        center: {lat:35.3, lng:139.3} , //地図の中心座標
        mapTypeId: 'roadmap' //地図の種類を指定
    };
    var map = new google.maps.Map(document.getElementById('map-test01'), Options); //埋め込むMAPのidを指定

    for (let i = 0; i < stores.length; i++) {
        var store = stores[i];
        var latlng = { lat: store.lat, lng: store.lng};
        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
        });
    }
}
