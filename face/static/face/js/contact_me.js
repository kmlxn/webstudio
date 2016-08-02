(function() {
    function handleContactFormSubmit(event) {
        event.preventDefault();
        var $form = $(event.target);
        var $allSendingStatuses = $form.find('#statuses > div');
        var $messageSendingError = $form.find('#message_send_error');
        var $messageSendingSuccess = $form.find('#message_send_success');
        var $messageSendingSpinner = $form.find('#message_sending');

        if (!validate($form))
            return;

        displaySendingSpinner();

        $.ajax({
            url: $form.attr('action'),
            type: 'POST',
            data: getValues($form),
            cache: false,
            success: function() {
                displaySendingSuccessMessage();
                $form.trigger('reset');
            },
            error: function() {
                displaySendingErrorMessage();
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

    function displaySendingErrorMessage() {
        $allSendingStatuses.hide();
        $messageSendingError.show();
    }

    function displaySendingSuccessMessage() {
        $allSendingStatuses.hide();
        $messageSendingSuccess.show();
    }

    function displaySendingSpinner() {
        $allSendingStatuses.hide();
        $messageSendingSpinner.show();
    }

    $(function() {
        $('#contactForm').submit(handleContactFormSubmit);
    });
})();
