(function() {
    function handleContactFormSubmit(event) {
        event.preventDefault();
        var $form = $(event.target);

        if (!validate($form))
            return;

        displaySendingSpinner($form);

        $.ajax({
            url: $form.attr('action'),
            type: 'POST',
            data: getValues($form),
            cache: false,
            success: function() {
                displaySendingSuccessMessage($form);
                $form.trigger('reset');
            },
            error: function() {
                displaySendingErrorMessage($form);
                $form.trigger('reset');
            },
        });
    }

    function validate($form) {
        hideAllFieldErrors();
        var required = ['[name="name"]', '[name="email"]', '[name="message"]', '[name="g-recaptcha-response"]'];
        var ok = true;

        $.each(required, function(i, input) {
            var $input = $form.find(input);
            if ($input.val().trim() === '') {
                displayRequiredError($input);
                ok = false;
            }
        });

        return ok;
    }

    function displayRequiredError($input) {
        $input.closest('#input_and_info').find('#field_error').show();
    }

    function hideAllFieldErrors() {
        $('p#field_error').hide();
    }

    function getValues($form) {
        var values = {};
        $.each($form.serializeArray(), function(i, field) {
            values[field.name] = field.value;
        });
        return values;
    }

    function displaySendingErrorMessage($form) {
        $form.find('#statuses > div').hide();
        $form.find('#message_send_error').show();
    }

    function displaySendingSuccessMessage($form) {
        $form.find('#statuses > div').hide();
        $form.find('#message_send_success').show();
    }

    function displaySendingSpinner($form) {
        $form.find('#statuses > div').hide();
        $form.find('#message_sending').show();
    }

    $(function() {
        $('#contactForm').submit(handleContactFormSubmit);
    });
})();
