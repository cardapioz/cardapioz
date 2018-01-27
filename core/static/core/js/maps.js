var placeSearch, autocomplete;

function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete((document.getElementById('autocomplete')),{types: ['address'], componentRestrictions: {country: 'br'}});
}

function geolocate() {
    //essa funcao usa o gps do navegador para usar os bounds, i.e, direcionar resultados para o local do usuario
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var geolocation = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            var circle = new google.maps.Circle({
                center: geolocation,
                radius: position.coords.accuracy
            });
            autocomplete.setBounds(circle.getBounds());
        });
    }
}

function updateAddress(){
    var place = autocomplete.getPlace();
    var data = {};

    for (var i = 0; i < place.address_components.length; i++) {
        data[place.address_components[i].types[0]] = place.address_components[i].short_name;
    }
    data['complement'] = 'teste';
    data['user'] = $('#user').val();
    data = JSON.stringify(data);
    console.log(data);

    fetch('/address/', {
        method: 'POST',
        headers:{'content-type': 'application/json'},
        body: data,
    }).then(function (data) {
        if (data.status === 201){
            console.log('Enviado com sucesso.');
        }else{
            console.log('Ocorreu um erro.');
        }
    }).catch(function (error) {
        console.log('ocorreu um erro.' + error)
    });
}
