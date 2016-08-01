$(function() {

    $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors) {
            // additional error messages or events
        },
        submitSuccess: function($form, event) {
            event.preventDefault(); // prevent default submit behaviour
            $('#message_send_success').hide();
            $('#message_send_error').hide();
            $('#message_sending').show();
            // get values from FORM
            var name = $("input#name").val();
            var email = $("input#email").val();
            var phone = $("input#phone").val();
            var csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
            var message = $("textarea#message").val();
            var formAction = $form.attr('action');
            var firstName = name; // For Success/Failure Message
            // Check for white space in name for Success/Fail message
            if (firstName.indexOf(' ') >= 0) {
                firstName = name.split(' ').slice(0, -1).join(' ');
            }
            $.ajax({
                url: formAction,
                type: "POST",
                data: {
                    name: name,
                    phone: phone,
                    email: email,
                    message: message,
                    csrfmiddlewaretoken: csrfmiddlewaretoken
                },
                cache: false,
                success: function() {
                    $('#message_sending').hide();
                    $('#message_send_success').show();

                    $('#contactForm').trigger("reset");
                },
                error: function() {
                    $('#message_sending').hide();
                    $('#message_send_error').show();

                    $('#contactForm').trigger("reset");
                },
            })
        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });
});


/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
    $('#success').html('');
});
