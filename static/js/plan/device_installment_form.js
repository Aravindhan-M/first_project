$(function() {

var options="";
options += '<option value="">--select--</option>';
var operator = $("#id_operator")
var plan = $("#id_plan")
if (operator.val() ==""){
$("#id_operator").html(options);
$("#id_line_type").prop('disabled',true);
}
if (operator.val() ==""){
$("#id_plan").html(options);
 
}




var t = $("#id_country");
t.change(function(){

if (t.val() != '') {
var option = ""
            $("#id_operator_id").prop('disabled',false);

            var selected = [];
            $("#id_operator_id :selected").each(function(i, sel){
                selected.push($(sel).val());
            });

            $.get('/mobileplans/ajax-plan-admin/', {id:t.val()}, function(data) {
            console.log(data)
                data = $.parseJSON(data);
                console.log(data)
                option += '<option value="">--select--</option>';

                $.each(data, function(index,item) {
                    option += '<option value="' + item.pk + '">' + item.fields.operator + '</option>';
                });
                console.log(option)
                $("#id_operator").html(option);
                $("#id_line_type").prop('disabled',false);

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


var l = $("#id_line_type");
l.change(function(){

if (l.val() != '') {
var option = ""
            $("#id_plan").prop('disabled',false);

            var selected = [];
            $("#id_plan :selected").each(function(i, sel){
                selected.push($(sel).val());
            });

            $.get('/mobileplans/ajax-device-installment-admin/', {country:t.val(),operator:$("#id_operator").val(),line:l.val()}, function(data) {
            console.log(data)
                data = $.parseJSON(data);
                console.log(data)
                option += '<option value="">--select--</option>';

                $.each(data, function(index,item) {
                    option += '<option value="' + item.pk + '">' + item.fields.name + '</option>';
                });
                console.log(option)
                $("#id_plan").html(option);


//                $("#id_plan option").each(function(i, sel) {
//                    if ($.inArray(sel.value, selected) !== -1) {
//                        $('#id_plan option[value=' + sel.value + ']').attr('selected', true);
//                    }
//                });

            });
        } else {
            $("#id_plan").prop('disabled',true);
        }
});


});




//$(function() {
//    var t = $("#id_country");$("#id_operator_id").prop('disabled',true);
//    t.change(function(){
//    console.log("sdfs")
//        if (t.val() != '') {
//            $("#id_plan").prop('disabled',false);
//
//            var selected = [];
//            $("#id_plan :selected").each(function(i, sel){
//                selected.push($(sel).val());
//            });
//
//            $.get('/mobileplans/ajax-plan-country-admin/', {id:t.val()}, function(data) {
//            console.log(data)
//                data = $.parseJSON(data);
//                console.log(data.length)
//                var options;
//                if (data.length == 0){
//                options += '<option value="">--select--</option>';
//                }
//                else{
//                options += '<option value="">--select--</option>';
//                $.each(data, function(index,item) {
//                    options += '<option value="' + item.pk + '">' + item.fields.name + '</option>';
//                });
//                }
//
//
//                $("#id_plan").html(options);
//                if (data.length != 0){
//
//                $("#id_plan option").each(function(i, sel) {
//                    if ($.inArray(sel.value, selected) !== -1) {
//                        $('#id_plan option[value=' + sel.value + ']').attr('selected', true);
//                    }
//                });
//                }
//
//            });
//        } else {
//            $("#id_plan").prop('disabled',true);
//        }
//        $("#id_plan").trigger('change');
//    });
//
// $("#id_country").trigger('change');
//
//
//
//    var tt = $("#id_plan");
//    tt.change(function(){
//    console.log("sdfssdfsfsdfsdfsdfsd")
//        if (tt.val() != '') {
//            $("#id_phone").prop('disabled',false);
//
//            var selected = [];
//            $("#id_phone :selected").each(function(i, sel){
//                selected.push($(sel).val());
//            });
//
//            $.get('/mobileplans/ajax-plan-country-phone-admin/', {id:t.val(),plan:tt.val()}, function(data) {
//            console.log(data)
//
//                console.log(data.length)
//                var options;
//                if (data.length == 0){
//                options += '<option value="">--select--</option>';
//                }
//                else{
//                options += '<option value="">--select--</option>';
//                $.each(data, function(index,item) {
//                console.log(item.id)
//                console.log(item.name)
//
//                    options += '<option value="' + item.id + '">' + item.name + '</option>';
//                });
//                }
//
//
//                $("#id_phone").html(options);
//                if (data.length != 0){
//
//                $("#id_phone option").each(function(i, sel) {
//                    if ($.inArray(sel.value, selected) !== -1) {
//                        $('#id_phone option[value=' + sel.value + ']').attr('selected', true);
//                    }
//                });
//                }
//
//            });
//        } else {
//            $("#id_phone").prop('disabled',true);
//        }
//    });
//
//
//
//
//
//
//});