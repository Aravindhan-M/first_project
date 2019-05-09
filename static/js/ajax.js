//<video name='demo' controls autoplay width='100%' height='100%'>
					//	<source src="" type="video/mp4"></source>
					//	</video>


$(document).ready(function(){
$("video").hide();
var e;
var page = window.location.pathname.split("/")[2];
var zones = ['zone1','zone2','zone3','zone4'];
if($(".zone1").length > 1){
console.log("display ads")
start(page,zones);
}

var promise = function(data){
console.log(data)


if (data != null){
a_class = "a."+ data.zone.name
img_class = "img." + data.zone.name
video_class = "video." + data.zone.name
vid = "v-"+data.zone.name
if(data.image_url){
$(img_class).attr("src",data.image_url);
$(video_class).hide();
$(img_class).show();
clearTimeout(e);
e = setInterval(ajaxcall,5000,page,zones);
}
if(data.video_url){
console.log(video_class)
$(video_class).show();
$(img_class).hide();
console.log($(video_class+" source"))
//$(video_class+" source").attr("src",data.video_url);
var html =
`
<video id ='${vid}' class = "${data.zone.name}" autoplay  width='100%' height='100%'>
					<source src="${data.video_url}" type="video/mp4"></source>
					</video>

`
$(video_class).replaceWith( html );
clearTimeout(e);
e = setInterval(ajaxcall,15000,page,zones);
du = document.getElementById("v-zone2");
console.log(du.duration);
}


$(a_class).attr("href",data.ad_url);
$(a_class).attr("title",data.title);

}
}
function ajaxcall(page,zones){
   console.log("ajax call inside")

for (index = 0; index < zones.length; index++) {
               $.ajax({
        url: '/ads/adreq/',
        data: {
          'page': page,
          'zone' : zones[index]
        },
        dataType: 'json',
        success: function (data) {
        console.log(data)
        promise(data)

        }
      });
      }


   }

function start(page,zones)
{
console.log("start inside")
console.log(page)
console.log(zones)


   console.log("sdfaf")


   e = setInterval(ajaxcall,5000,page,zones);




}



});

