console.log('[System] Forms works!')
$(document).ready(function() 
{
    $('form').on('submit', function(event)
    {
        $.ajax
        (
            {
                data : 
                {
                    
                    //username : $('#username').val(),
                    //username : ('hello')
                    username : $('input[name="username"').val(),
                    password : $('input[name="password"').val(),
                    case : $('input[name="case"').val()
                    
                },
                
                type : 'POST',
                url: 'http:127.0.0.1:5050/bego',
            }
        );
        console.log('Send succesfully')

        event.preventDefault();

    });
});