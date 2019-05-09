$(function() {

    var def_curr;

    var selected_currency = []
    var selected_currency_display = []
    var options;
    options += '<option value="">--select--</option>';
    $('input[name="currency"]:checked').each(function() {
        var sel = $(this).val();
        var display = $(this).parent().text()
        selected_currency.push(sel)
        selected_currency_display.push(display)
    });
    $.each(selected_currency, function(index, item) {
        options += '<option value="' + item + '">' + selected_currency_display[index] + '</option>';
    });
    $("#id_default_currency").html(options);
    var t = $("#id_currency > li > label > input");
    t.change(function() {
        var options;
        options += '<option value="">--select--</option>';
        var selected_currency = []
        var selected_currency_display = []
        $('input[name="currency"]:checked').each(function() {
            var sel = $(this).val();
            var display = $(this).parent().text()
            selected_currency.push(sel)
            selected_currency_display.push(display)
        });
        $.each(selected_currency, function(index, item) {
            options += '<option value="' + item + '">' + selected_currency_display[index] + '</option>';
        });
        $("#id_default_currency").html(options);
        if (def_curr!=null) {
                        $('#id_default_currency option[value=' + def_curr + ']').attr('selected', true);
                    }
    });

    $.get('/phones/ajax-currency/', {slug:$("#id_slug").val()}, function(data) {

                def_curr = data


                    if (def_curr!=null) {
                        $('#id_default_currency option[value=' + def_curr + ']').attr('selected', true);
                    }

      });
});