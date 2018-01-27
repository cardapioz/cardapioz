function order_this() {
    $('#modal-wait').modal('open');

    $('.modal').modal({
         dismissible: false, // Modal can be dismissed by clicking outside of the modal
         opacity: .5, // Opacity of modal background
         inDuration: 300, // Transition in duration
         outDuration: 200, // Transition out duration
         startingTop: '4%', // Starting top style attribute
         endingTop: '20%', // Ending top style attribute
       }
    );

    var formdata = $(".form-pedido").serializeArray();
    var data = {};

    $(formdata).each(function(index, obj){
        data[obj.name] = obj.value;
    });
    data = JSON.stringify(data);

    fetch('/pedir/', {
        method: 'POST',
        headers:{'content-type': 'application/json'},
        body: data,
    }).then(function (data) {
        if (data.status === 201){
            console.log(data.status)
            $('#modal-wait').modal('close');
             document.querySelector('.btn-main').innerHTML = `
                 <a onclick="" class="btn green darken-3 waves-effect btn-acompanhar">acompanhar pedido</a>
            `;

            return updateModal('pedido-ok');


        }else{
            $('#modal-wait').modal('close');
            $('#modal-failure').modal('open');

             document.querySelector('.btn-main').innerHTML = `
                 <a onclick="updateModal('confirmacao')" class="btn red darken-3 waves-effect btn-retry">tentar novamente</a>
            `;
        }
    });
}
