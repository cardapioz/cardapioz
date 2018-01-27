function order_this() {

    const formdata = $(".form-pedido").serializeArray();
    let data = {};

    $(formdata).each(function(index, obj){
        data[obj.name] = obj.value;
    });
    data = JSON.stringify(data);
   // data['csrftoken'] = $('input[name=csrfmiddlewaretoken]').val();

    console.log(data);

    fetch('/pedir/', {
        method: 'POST',
        headers:{'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val(), 'content-type': 'application/json'},
        body: data,
    }).then(function (data) {
        if (data.status === 201){
            $('#modal-order-this').modal('open');
        }else{
            console.log(data)
        }
    });
}
