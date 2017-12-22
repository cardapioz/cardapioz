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

$('#post').click(function () {
    var comment = $('input[name=comment_text]').val();
    if(comment !== ''){
        var user_name = $('#user-name').text();
        var user_photo = $('#user-photo').attr('src');
        var date = 'Agora';
        $.ajax({
            type: 'POST',
            url: '/comment/',
            data:{
                comment_text: comment,
                product: $('input[name=product]').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            }, success:function (data) {

                $('.collection').prepend('<li class="collection-item avatar green lighten-5"><img alt="" class="circle"' +
                    'src="'+ user_photo +'">'+
                    '<span class="title">'+ user_name +'</span><p class="">'+ comment +'</p>'+
                    '<span class="secondary-content grey-text text-lighten-1">'+
                    date +'</span>'+
                    '</li>');

                $('input[name=comment_text]').val('');
                Materialize.toast(data, 3000, 'rounded')
            },error:function (data) {
                Materialize.toast('Ops, ocorreu um erro ao tentar cadastrar comentario', 3000, 'rounded')
            }
        })
    }else{
        $('#modal1').modal('open');
    }
});
