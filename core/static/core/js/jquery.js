$('.button-collapse').sideNav({
        menuWidth: 300, // Default is 300
        edge: 'left', // Choose the horizontal origin
        closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
        draggable: true // Choose whether you can drag to open on touch screens
    }
);


$('.carousel.carousel-slider').carousel({fullWidth: true});


$(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal').modal();
    $('select').material_select();

});


function logout() {
    $.ajax({
        type: 'POST',
        url: '/accounts/logout/',
        data:{
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },success:function () {
            window.location.href = '/';
        }
    })
}

$('#post').click(function () {
    $.ajax({
        type: 'POST',
        url: '/comment/',
        data:{
            comment_text: $('input[name=comment_text]').val(),
            product: $('input[name=product]').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        }, success:function (data) {
            Materialize.toast(data, 3000, 'rounded')
        },error:function (data) {
            Materialize.toast('Ops, ocorreu um erro ao tentar cadastrar comentario', 3000, 'rounded')

        }
    })
});
