function order_this() {

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
            $('#modal1').modal('open');
        }else{
            console.log('pedido não realizado')
        }
    });
}

 $('.modal').modal({
      dismissible: true, // Modal can be dismissed by clicking outside of the modal
      opacity: .5, // Opacity of modal background
      inDuration: 300, // Transition in duration
      outDuration: 200, // Transition out duration
      startingTop: '4%', // Starting top style attribute
      endingTop: '10%', // Ending top style attribute
      ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
        alert("Ready");
        console.log(modal, trigger);
      },
      complete: function() { alert('Closed'); } // Callback for Modal close
    }
  );