$(function() {

    $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors) {
            // additional error messages or events
        },
        submitSuccess: function($form, event) {
            event.preventDefault(); // prevent default submit behaviour
            $form.find('#message_send_success').hide();
            $form.find('#message_send_error').hide();
            $form.find('#message_sending').show();
            // get values from FORM
            var name = $form.find("input#name").val();
            var email = $form.find("input#email").val();
            var phone = $form.find("input#phone").val();
            var csrfmiddlewaretoken = $form.find("input[name='csrfmiddlewaretoken']").val();
            var message = $form.find("textarea#message").val();
            var g_recaptcha_response = $form.find("textarea#g-recaptcha-response").val();
            var formAction = $form.attr('action');
            $.ajax({
                url: formAction,
                type: "POST",
                data: {
                    name: name,
                    phone: phone,
                    email: email,
                    message: message,
                    csrfmiddlewaretoken: csrfmiddlewaretoken,
                    'g-recaptcha-response': g_recaptcha_response

                },
                cache: false,
                success: function() {
                    $form.find('#message_sending').hide();
                    $form.find('#message_send_success').show();

                    $form.trigger("reset");
                },
                error: function() {
                    $form.find('#message_sending').hide();
                    $form.find('#message_send_error').show();

                    $form.trigger("reset");
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

