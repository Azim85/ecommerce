$(document).ready(function(){


    $('#createButton').click(function(){
        var serializedData = $('#createForm').serialize();
        $.ajax({
            url:$('#createForm').data('url'),
            data:serializedData,
            method:'post',
            success:function(response){
                $('#main').html('<div class="alert alert-success text-center w-100">'+response+'</div>')
            }
        })
    })
})