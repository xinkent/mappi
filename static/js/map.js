function initMap() {
    const myLatLng = { lat: -25.363, lng: 131.044 }
    var Options = {
        zoom: 15, //地図の縮尺値を指定
        center: myLatLng, //地図の中心座標
        mapTypeId: 'roadmap' //地図の種類を指定
    };
    var map = new google.maps.Map(document.getElementById('map-test01'), Options); //埋め込むMAPのidを指定

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map
    })
}
