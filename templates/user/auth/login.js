
$(function () {
    var $user = $('#user');
    var $password = $('#password');
    var $csrfmiddlewaretoken = $(document.getElementsByName("csrfmiddlewaretoken"));
    $('#login-submit').on('click', function () {
        $('#login-submit').hide(300);
        var login_form = {
            user: $user.val(),
            password: $password.val(),
            csrfmiddlewaretoken: $csrfmiddlewaretoken.val(),
        }
        $.ajax({
            type: 'POST',
            url:'{% url 'login_api' %}',
            data : login_form,
            success : function(answer){
                if (answer.error == "Not"){
                    window.location.replace("{% url 'info_user'%}");
                };
                if (answer.error == "password"){
                    $password.removeClass('valid');
                    $password.addClass('invalid');
                };
                if (answer.error == "user_email"){
                    $user.removeClass('valid');
                    $user.addClass('invalid');
                };
            $('#login-submit').show(300);
            },
            error: function(){
                login_form.push(window.location);
                $.ajax({
                    type: 'POST',
                    url: '{%url 'error_api'%}' ,
                    data : login_form,
                });
            },
        });
    });
    $($user).on('input', revalidate);
    $($password).on('input', revalidate);
});

function revalidate(){
    this.classList.remove('invalid');
    
}