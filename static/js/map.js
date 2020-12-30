function initMap(){
    var MyLatLng = new google.maps.LatLng(39.7161777, 141.1364266); //座標を指定
    var Options = {
    zoom: 15, //地図の縮尺値を指定
    center: MyLatLng, //地図の中心座標
    mapTypeId: 'roadmap' //地図の種類を指定
    };
    var map = new google.maps.Map(document.getElementById('map-test01'), Options); //埋め込むMAPのidを指定

    var latlng = new google.maps.LatLng(35.632,139.881);
    var marker = new google.maps.Marker({
        position: latlng,
        map:map
    })
}
