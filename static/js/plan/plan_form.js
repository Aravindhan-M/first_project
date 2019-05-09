$(function() {
    var t = $("#id_country");
    t.change(function(){
    console.log("sdfs")
        if (t.val() != '') {
            $("#id_operator_id").prop('disabled',false);

            var selected = [];
            $("#id_operator_id :selected").each(function(i, sel){
                selected.push($(sel).val());
            });

            $.get('/mobileplans/ajax-plan-admin/', {id:t.val()}, function(data) {
                data = $.parseJSON(data);
                console.log(data)
                if (data.length == 0){
                $("#id_operator_id").prop('disabled',true);
                }
                var options;
                $.each(data, function(index,item) {
                    options += '<option value="' + item.pk + '">' + item.fields.operator + '</option>';
                });
                $("#id_operator_id").html(options);

                $("#id_operator_id option").each(function(i, sel) {
                    if ($.inArray(sel.value, selected) !== -1) {
                        $('#id_operator_id option[value=' + sel.value + ']').attr('selected', true);
                    }
                });

            });
        } else {
            $("#id_operator_id").prop('disabled',true);
        }
    });
    $("#id_country").trigger('change');
});