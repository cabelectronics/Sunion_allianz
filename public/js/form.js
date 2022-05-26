console.log("Form works!")
$(document).ready(function() 
{
    $('form').on('submit', function(event)
    {
        $.ajax
        (
            {
                data : 
                {
                    
                    username : $('#username').val(),
                    password : $('#password').val(),
                
                    
                },
                
                type : 'POST',
                url: 'http:127.0.0.1:6280/bego',
            }
        );
        console.log('Send succesfully')

        event.preventDefault();

    });
});

//bego puerto del localhost donde se envian el usuario y contrasena