$('.button-collapse').sideNav({
        menuWidth: 300,
        edge: 'left',
        closeOnClick: true,
        draggable: true,
        time: 500
    }
);


$('.carousel.carousel-slider').carousel({fullWidth: true});


$(document).ready(function(){
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
    }
);


$('input.autocomplete').autocomplete({
    data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
    },
    limit: 20, // The max amount of results that can be shown at once. Default: Infinity.
    onAutocomplete: function(val) {
        // Callback function when value is autcompleted.
    },
    minLength: 1, // The minimum length of the input for the autocomplete to start. Default: 1.
});