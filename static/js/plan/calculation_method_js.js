$(".times button").click(function(event) {
event.preventDefault();
console.log("clicked")
var val = $("#times").val()
var ids = "id"+ val * Math.floor(Math.random() * 100);
var template = "<div class='btn' style='display: inline-block;'><button class='btnexpress'> "+val+"<a id='"+ids+"' ><img src="+delete_pic+"></img></a></button></div>"
console.log(template)
    $('#result').before(template);
	console.log('#'+ids)

	 $("#"+ids+"").click('click', function() {

  $(this).parent().parent().remove();
});
});


$(".operator button").click(function(event) {
event.preventDefault();
var val = $("input[name='operator']:checked").val()
if(val){
var ids = "op"+  Math.floor(Math.random() * 100);
var template = "<div class='btn' style='display: inline-block;'><button class='btnexpress'> "+val+"<a id='"+ids+"' ><img src="+delete_pic+"></img></a></button></div>"
     $('#result').before(template);

	$("#"+ids+"").bind('click', function() {
  $(this).parent().parent().remove();
});
}
else{
alert("please select operator ")
}
});


$(".field button").click(function(event) {
event.preventDefault();
    var val = $("input[name='field']:checked").val()
if(val){
var ids = "op"+  Math.floor(Math.random() * 100);
var template = "<div class='btn' style='display: inline-block;'><button class='btnexpress'> "+val+"<a id='"+ids+"' ><img src="+delete_pic+"></img></a></button></div>"
     $('#result').before(template);

	$("#"+ids+"").bind('click', function() {
  $(this).parent().parent().remove();
});
}
else{
alert("please select field ")
}
});


$("#create_exp").click(function(event){
event.preventDefault();
var exp_string="";

var expressions = $(".btnexpress")
if (expressions.length == 0){
alert("Empty expression cannot be evaluated")
}
else{
expressions.each(function( index ) {
    exp_string +=$( this ).text()
});

try{
var result = nerdamer(exp_string).evaluate();




$("#id_expression").val(exp_string)


}
catch(err){
alert("Expression is invalid , please correct the expression")
}





}





})






