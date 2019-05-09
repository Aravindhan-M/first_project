
$(document).ready(function(){

  $(window).on('shown.bs.modal', function() {

    $('.carousel').slick({
    slidesToShow: 1,
      slidesToScroll: 1,
    // autoplay: true,
    // autoplaySpeed: 2000,
    nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
    prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>',
    responsive: [
     {
        breakpoint: 1024,
        settings: {
        slidesToShow: 3,
        slidesToScroll: 2,variableWidth: false,centerMode:true
      }
    },
      {
         breakpoint: 991,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2, variableWidth:false,centerMode:false
      }
    },
    {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,slidesToScroll: 1,variableWidth:false,centerMode:false
                    }
                  },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,variableWidth:false,centerMode:false
        }
      }

    ]
});

  $(".scrollPrdct_mdl").niceScroll({autohidemode:false,railalign:'right', cursorcolor:"#81b4ed",emulatetouch: false,});
//    $(".scrollPrdct_mdl").niceScroll({
//      touchbehavior: true,
//      autohidemode:false,
//       cursorcolor:"#81b4ed",
//      railalign:'right',
//      enablekeyboard: false,
//    enablemousewheel:true,
//    background:'rgba(173, 173, 173, 0.68)',
//    horizrailenabled:false,cursoropacitymin:0.4
//
//    });

  });
  // Resize the slick slider according device
    $(window).resize(function () {
        $('.top_products_slides1,.top_products_slides2').not('.slick-initialized').slick('resize');
    });
    $(window).on('orientationchange', function () {
        $('.top_products_slides1,.top_products_slides2').not('.slick-initialized').slick('resize');
    });
  // Make the range slider draggable on mobile
    $('.ui-slider-handle').draggable();
  // Initializinf Functions
    initializeLocalization();
    initializeSlider();
    initializeRangeSlider();
    initializePriceRangeSlider();
    initializeNiceScroll();
		$('#demo').flagStrap({
        countries: {
            "DZ": "Algeria",
            "BH": "Bahrain",
            "EG": "Egypt",
            "IQ": "Iraq",
            "JO": "Jordan",
            "KW": "Kuwait",
            "LB": "Lebanon",
            "LY": "Libya",
            "MA": "Morocco",
            "OM": "Oman",
            "PS": "Palestine",
            "QA": "Qatar",
            "SA": "SA",
            "SD": "Sudan",
            "SY": "Syria",
            "TN": "Tunisia",
            "AE": "UAE",
            "YE": "Yemen"
        },
        buttonSize: "btn-sm",
        buttonType: "btn-info",
        labelMargin: "10px",
        scrollable: false,
        scrollableHeight: "350px"
    });

//$("#dropdownMenuButton").click(function(){
//
//    console.log("calleedd")
//			console.log($("#dropdownMenuButton").text())
//})

$("#resultsBox").find("li").click(function(){
  alert("You clicked on li " + $(this).text());
});
		// to denote the value of dropdown in text to button
			$(".dropdown-menu li a").click(function(){


			  $(this).parents(".dropdown").find('.btn').html($(this).text() + '<span class="caret"></span>');
			  $(this).parents(".dropdown").find('.btn').val($(this).data('value'));

			});

    
// custom select script
    var x, i, j, selElmnt, a, b, c;
    /*look for any elements with the class "custom-select":*/
    x = document.getElementsByClassName("custom-select");
    for (i = 0; i < x.length; i++) {
    selElmnt = x[i].getElementsByTagName("select")[0];
    /*for each element, create a new DIV that will act as the selected item:*/
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
    x[i].appendChild(a);
    /*for each element, create a new DIV that will contain the option list:*/
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");
    // b.setAttribute("data-simplebar", "init");
    for (j = 1; j < selElmnt.length; j++) {
      /*for each option in the original select element,
      create a new DIV that will act as an option item:*/
      c = document.createElement("DIV");
      c.innerHTML = selElmnt.options[j].innerHTML;
      c.addEventListener("click", function(e) {
          /*when an item is clicked, update the original select box,
          and the selected item:*/
          var y, i, k, s, h;
          s = this.parentNode.parentNode.getElementsByTagName("select")[0];
          h = this.parentNode.previousSibling;
          for (i = 0; i < s.length; i++) {
            if (s.options[i].innerHTML == this.innerHTML) {
              s.selectedIndex = i;
              h.innerHTML = this.innerHTML;
              y = this.parentNode.getElementsByClassName("same-as-selected");
              for (k = 0; k < y.length; k++) {
                y[k].removeAttribute("class");
              }
              this.setAttribute("class", "same-as-selected");
              break;
            }
          }
          h.click();
      });
      b.appendChild(c);
    }
    x[i].appendChild(b);
    a.addEventListener("click", function(e) {
        /*when the select box is clicked, close any other select boxes,
        and open/close the current select box:*/
        e.stopPropagation();
        closeAllSelect(this);
        this.nextSibling.classList.toggle("select-hide");
        this.classList.toggle("select-arrow-active");
      });
  }
  function closeAllSelect(elmnt) {
    /*a function that will close all select boxes in the document,
    except the current select box:*/
    var x, y, i, arrNo = [];
    x = document.getElementsByClassName("select-items");
    y = document.getElementsByClassName("select-selected");
    for (i = 0; i < y.length; i++) {
      if (elmnt == y[i]) {
        arrNo.push(i)
      } else {
        y[i].classList.remove("select-arrow-active");
      }
    }
    for (i = 0; i < x.length; i++) {
      if (arrNo.indexOf(i)) {
        x[i].classList.add("select-hide");
      }
    }
  }
/*if the user clicks anywhere outside the select box,
then close all select boxes:*/
document.addEventListener("click", closeAllSelect);
// custom select script end
});

function initializeLocalization() {
  $('#selectLanguageDropdown').localizationTool({
'defaultLanguage' : 'en_GB',
/* do not throw error if a selector doesn't match */
'ignoreUnmatchedSelectors': false,
/* show the flag on the widget */
'showFlag' : false,
/* show the language on the widget */
'showLanguage': true,
/* show the country on the widget */
'showCountry': false,
/* format of the language/country label */
'labelTemplate': '{{language}}',
'languages' : {
  'arabic' : {
      // 'country': 'Italy',
      'language' : 'Arabic',
      // 'countryTranslated': 'Italia',
      // 'languageTranslated': 'Italiano',
      'flag' : {
          'url' : 'http://upload.wikimedia.org/wikipedia/commons/f/fb/Farm-Fresh_italy.png', /* url of flag image */
          'class' : 'italian-flag' /* (optional) class to assign to the flag (e.g., for css styling) */
      }
  },
    
},

 // * Strings are provided by the user of the plugin. Each entry
 // * in the dictionary has the form:
 // *
 // * [STRING_IDENTIFIER] : {
 // *      [LANGUAGE] : [TRANSLATION]
 // * }
 // *
 // * STRING_IDENTIFIER:
 // *     id:<html-id-name>           OR
 // *     class:<html-class-name>     OR
 // *     element:<html-element-name> OR
 // *     <string>
 // *
 // * LANGUAGE: one of the languages defined above (e.g., it_IT)
 // *
 // * TRANSLATION: <string>
 // *
 
'strings' : {
  'Additional Services' : {
      'arabic' : 'الخدمات والمزايا',
  },
  'Mobile' : {
      'arabic' : 'التليفون المحمول',
  },
  'mobile plans' : {
      'arabic' : ' باقات الهواتف المحمولة',
  },
  'mobile plans only' :{
    'arabic':'الهواتف المحمولة',
  },
  'Mobile Internet' :{
   'arabic' :'باقات الانترنت',
  },
   'Fixed Internet' :{
   'arabic' :'باقاتا انترنت الفايبر و ال دى اس ال',
  },
   'Login' :{
   'arabic' :' الدخول',
  },
  'Register' :{
   'arabic' :'التسجيل',
  },
  'Choose the best plan in, Saudi Arabia' :{
   'arabic' :'اختر أفضل الباقات في المملكة العربية السعودية',
  },
  'Providers' :{
   'arabic' :'مقدمي الخدمات',
  },
  'Best':{
    'arabic':'افضل',
  },
  'Best Mobile plans':{
    'arabic':'افضل باقات الهواتف المحمولة',
  },
  'Best unlimited internet':{
    'arabic':'افضل باقات الانترنت اللامحدود',
  },
  'Copyright © 2019 PlanBaker Inc.':{
    'arabic':'حقوق الطبع والنشر © 2019 PlanBaker Inc.',
  },
  'Select Mobile Phone':{
    'arabic':'اختر الهاتف المحمول',
  },
  'Select Intenet Device':{
    'arabic':'اخترجهاز الإنترنت',
  },
  'class:needsimcardonly_trans':{
    'arabic':'تحتاج شريحة المحمول فقط',
  },
  'Monthly Usage':{
    'arabic':'الاستهلاك الشهرى',
  },
  'class:data_trans':{
    'arabic':'البيانات :',
  },
  'class:minute_trans':{
    'arabic':'الدقائق :',
  },
  'class:msg_trans':{
    'arabic':'الرسائل :',
  },
  'network':{
    'arabic':'الشبكة',
  },
  'class:plan_availabe_trnslte':{
    'arabic':'الباقات المتاحة',
  },
  'search all operators':{
    'arabic':'البحث فى جميع مقدمي الخدمات',
  },
  'Top Smartphones':{
    'arabic':'احدث الهواتف الذكية',
  },
  'See specifications':{
    'arabic':'انظر المواصفات',
  },
  'class:available_in_12_plans':{
    'arabic':'متوفر فى 12 باقة',
  },
  // 'class:buymobilephoneonly':{
  //   'arabic':'شراء الهاتف المحمول فقط',
  // },
  'Choose the best plans for Mobile phone':{
    'arabic':'اختر أفضل باقة للهاتف المحمول في المملكة العربية السعودية',
  },
  'Choose the best plans for':{
    'arabic':'اختيار أفضل الخطط ل',
  },
  'Choose the best plans for Mobile internet':{
    'arabic':'اختر أفضل باقة انترنت في المملكة العربية السعودية',
  },
  'Go to the nearest branch':{
    'arabic':'اذهب إلى أقرب فرع',
  },
  'Buy Online':{
    'arabic':'شراء عن طريق الانترنت',
  },
  'Mobile Phones':{
    'arabic':'الهواتف المحمولة',
  },
  'class:choose_best_plans_for':{
    'arabic':'اختيار أفضل الخطط ل',
  },
   'class:mobilephonr_trans':{
    'arabic':'الهواتف المحمولة',
  },
  'class:plan_desc':{
    'arabic':'أبجد هوز هو مجرد',
  },
  'Lorem Ipsum':{
    'arabic':'أبجد هوز هو مجرد',
  }

},
/*
 * A callback called whenever the user selects the language
 * from the dropdown menu. If false is returned, the
 * translation will not be performed (but just the language
 * will be selected from the widget).
 *
 * The countryLanguageCode is a string representing the
 * selected language identifier like 'en_GB'
 */
'onLanguageSelected' : function (lang) {
  change(lang);
  return true;
  }
  });
}


function change (lang) {


          if (lang == "arabic") {


            $("html").attr("dir", "rtl");
            $("#styleLink").attr('href', '/static/css/rtl_style.css');

//            $('.top_products_slides1').slick('unslick');
//            $('.top_products_slides2').slick('unslick');
//            $('.planVndr_products_list_slider').slick('unslick');
//             $('.provider_slider').slick('unslick');
            initializertlSlider();
            initializertlRangeSlider();
            initializertlPriceRangeSlider();
            initializertlNiceScroll();
          }
          if (lang == "en_GB") {

            $("html").attr("dir", "");
            $("#styleLink").attr('href', '/static/css/style.css');

            $('.top_products_slides1').slick('unslick');
            $('.top_products_slides2').slick('unslick');
            $('.planVndr_products_list_slider').slick('unslick');
            // $('.provider_slider').slick('unslick');
            initializeSlider();
            initializeRangeSlider();
             initializePriceRangeSlider();
             initializeNiceScroll();
          }
}
// function initializeSimpleBar(){
// new SimpleBar(document.getElementById('simple_bar'), {
//     autoHide: true,
//     direction: 'ltr',
//     timeout: 1000
// })
// new SimpleBar(document.getElementById('simple_bar1'), {
//     autoHide: true,
//     direction: 'ltr',
//     timeout: 1000
// })
// new SimpleBar(document.getElementById('simple_bar2'), {
//     autoHide: true,
//     direction: 'ltr',
//     timeout: 1000
// })
// }
// function initializertlSimpleBar(){
//   console.log('simple rtl')
//   new SimpleBar(document.getElementById('simple_bar'), {
//     autoHide: true,
//     direction: 'rtl',
//     timeout: 1000
// })
// new SimpleBar(document.getElementById('simple_bar1'), {
//     autoHide: true,
//     direction: 'rtl',
//     timeout: 1000
// })
// new SimpleBar(document.getElementById('simple_bar2'), {
//     autoHide: true,
//     direction: 'rtl',
//     timeout: 1000
// })
// }
function initializeNiceScroll(){

  $(function () {  
          $(".select-items").niceScroll({
            scrollspeed: 40,cursorcolor: "#3c94e6",horizrailenabled:false,cursoropacitymin:0.4,railalign: 'right'
          });
      });
  $(function () {  
          $(" .scrollPrdct").niceScroll({
            scrollspeed: 40,cursorcolor: "#3c94e6",horizrailenabled:false,cursoropacitymin:0.4,railalign: 'right',background: "rgba(183, 183, 183,0.3)"
          });
      });
 
}
function initializertlNiceScroll(){


$(function () {  
          $(".select-items").niceScroll({
            scrollspeed: 40,cursorcolor: "#3c94e6",horizrailenabled:false,cursoropacitymin:0.4,railalign: 'left'
          });
      });
$(function () {  
          $(".scrollPrdct").niceScroll({
            scrollspeed: 40,cursorcolor: "#3c94e6",horizrailenabled:false,cursoropacitymin:0.4,railalign: 'left'
          });
      });
}

function initializeRangeSlider(id) {


$(id).val(0)
         var val = ($(id).val() - $(id).attr('min')) / ($(id).attr('max') - $(id).attr('min'));
          $(id).css('background-image',
                '-webkit-gradient(linear, left top, right top, '
                + 'color-stop(' + val + ', #3c94e6), '
                + 'color-stop(' + val + ', #cfe1f1)'
                + ')'
                );

  $(id).on('change mousemove',function () {
          var val = ($(this).val() - $(this).attr('min')) / ($(this).attr('max') - $(this).attr('min'));
          $(this).css('background-image',
                '-webkit-gradient(linear, left top, right top, '
                + 'color-stop(' + val + ', #3c94e6), '
                + 'color-stop(' + val + ', #cfe1f1)'
                + ')'
                );
  });
  $(id).on('change touchmove',function () {
          var val = ($(this).val() - $(this).attr('min')) / ($(this).attr('max') - $(this).attr('min'));
          $(this).css('background-image',
                '-webkit-gradient(linear, left top, right top, '
                + 'color-stop(' + val + ', #3c94e6), '
                + 'color-stop(' + val + ', #cfe1f1)'
                + ')'
                );
  });
}

function initializertlRangeSlider() {
   var val = ($('input[type="range"]').val() - $('input[type="range"]').attr('min')) / ($('input[type="range"]').attr('max') - $('input[type="range"]').attr('min')); 
          $('input[type="range"]').css('background-image',
                '-webkit-gradient(linear, right top, left top,'
                + 'color-stop(' + val + ', #3c94e6), '
                + 'color-stop(' + val + ', #cfe1f1)'
                + ')'
                );
  $('input[type="range"]').on('change mousemove',function () {
          var val = ($(this).val() - $(this).attr('min')) / ($(this).attr('max') - $(this).attr('min')); 
          $(this).css('background-image',
                '-webkit-gradient(linear, right top, left top,'
                + 'color-stop(' + val + ', #3c94e6), '
                + 'color-stop(' + val + ', #cfe1f1)'
                + ')'
                );
  });
  $('input[type="range"]').on('change touchmove',function () {
          var val = ($(this).val() - $(this).attr('min')) / ($(this).attr('max') - $(this).attr('min')); 
          $(this).css('background-image',
                '-webkit-gradient(linear, right top, left top,'
                + 'color-stop(' + val + ', #3c94e6), '
                + 'color-stop(' + val + ', #cfe1f1)'
                + ')'
                );
  });
   
}

function initializertlSlider() {
    $('.top_products_slides1,.top_products_slides2').not('.slick-initialized').slick({ 
     slidesToShow: 4,
      slidesToScroll: 1,
      variableWidth: true,
      rtl:true,
      autoplay: true,
      autoplaySpeed: 2000,
      nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
      prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>', 
      responsive: [
               {
                   breakpoint: 1024,
                settings: {
                  slidesToShow: 3,
                  slidesToScroll: 2,variableWidth: true,centerMode:true
                }
              },
              {
                 breakpoint: 991,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2, variableWidth:false,centerMode:false
              }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,slidesToScroll: 2,variableWidth:false,centerMode:false
                  }
                },
            {
                breakpoint: 600,
                settings: {
                  slidesToShow: 1,
                  slidesToScroll: 1,variableWidth:false,centerMode:false
                }
              }
          ]
       });
    $('.planVndr_products_list_slider').not('.slick-initialized').slick({
     slidesToShow: 3,
      slidesToScroll: 1,
      rtl:true,
      autoplay: true,
      autoplaySpeed: 2000,
      nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
      prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>', 
      responsive: [
               {
                   breakpoint: 1024,
                settings: {
                  slidesToShow: 3,
                  slidesToScroll: 2,variableWidth: true,centerMode:true
                }
              },
              {
                 breakpoint: 991,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2, variableWidth:false,centerMode:false
              }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,slidesToScroll: 2,variableWidth:false,centerMode:false
                  }
                },
            {
                breakpoint: 600,
                settings: {
                  slidesToShow: 1,
                  slidesToScroll: 1,variableWidth:false,centerMode:false
                }
              }
          ]
       });

// $('.provider_slider').not('.slick-initialized').slick({ 
//     slidesToShow: 5,
//       slidesToScroll: 1,centerMode:true,rtl:true,
//     // autoplaySpeed: 2000,
//      nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
//     prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>',     
//   responsive: [
//     {
//       breakpoint: 991,
//       settings: {
//         slidesToShow: 2,
//         slidesToScroll: 2

//       }
//     },
//     {
//       breakpoint: 600,
//       settings: {
//         slidesToShow: 2,
//         slidesToScroll: 2
//       }
//     },
//     {
//       breakpoint: 480,
//       settings: {
//         slidesToShow: 1,
//         slidesToScroll: 1
//       }
//     }
//   ]
// });
}

function initializeSlider() {
    $('.top_products_slides1,.top_products_slides2').slick({ 
    slidesToShow: 4,
      slidesToScroll: 1,
      variableWidth:true,
    autoplay: true,
    autoplaySpeed: 2000,
         nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
    prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>', 
    responsive: [
     {
        breakpoint: 1024,
        settings: {
        slidesToShow: 3,
        slidesToScroll: 2,variableWidth: false,centerMode:true
      }
    },
      {
         breakpoint: 991,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2, variableWidth:false,centerMode:false
      }
    },
    {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,slidesToScroll: 1,variableWidth:false,centerMode:false
                    }
                  },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,variableWidth:false,centerMode:false
        }
      }
     
    ]
});
    $('.planVndr_products_list_slider').slick({
    slidesToShow: 3,
      slidesToScroll: 1,
    // autoplay: true,
    // autoplaySpeed: 2000,
    nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
    prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>', 
    responsive: [
     {
        breakpoint: 1024,
        settings: {
        slidesToShow: 3,
        slidesToScroll: 2,variableWidth: false,centerMode:true
      }
    },
      {
         breakpoint: 991,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2, variableWidth:false,centerMode:false
      }
    },
    {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,slidesToScroll: 1,variableWidth:false,centerMode:false
                    }
                  },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,variableWidth:false,centerMode:false
        }
      }
     
    ]
});
}

// $('.provider_slider').not('.slick-initialized').slick({ 
//     slidesToShow: 5,
//       slidesToScroll: 1,centerMode:true,
//     // autoplaySpeed: 2000,
//      nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
//     prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>',     
//   responsive: [
//     {
//       breakpoint: 991,
//       settings: {
//         slidesToShow: 2,
//         slidesToScroll: 2

//       }
//     },
//     {
//       breakpoint: 600,
//       settings: {
//         slidesToShow: 2,
//         slidesToScroll: 2
//       }
//     },
//     {
//       breakpoint: 480,
//       settings: {
//         slidesToShow: 1,
//         slidesToScroll: 1
//       }
//     }
//   ]
// });

/* === FILTER SHOW LESS TOGGLE === */
$(document).ready(function(){
  $('#store-show').click(function(){
     $( "#store-show-section" ).toggle("fast");
     $( "#store-show" ).toggleClass("flter-ico-change");
     if ($( "#store-show" ).hasClass("flter-ico-change")) {
            $( "#store-show" ).html("Show more <span class='plus-ico'><i class='flaticon-down-arrow'></i></span");
       } else {
              $( "#store-show" ).html("Show less <span class='plus-ico'><i class='flaticon-up-arrow'></i></span>");
       }
       
  });
  $('#color-show').click(function(){
     $( "#color-show-section" ).toggle("fast");
     $( "#color-show" ).toggleClass("flter-ico-change");
     if ($( "#color-show" ).hasClass("flter-ico-change")) {
            $( "#color-show" ).html("Show more <span class='plus-ico'><i class='flaticon-down-arrow'></i></span");
       } else {
              $( "#color-show" ).html("Show less <span class='plus-ico'><i class='flaticon-up-arrow'></i></span>");
       }
  });
  $('#memory-show').click(function(){
     $( "#memory-show-section" ).toggle("fast");
     $( "#memory-show" ).toggleClass("flter-ico-change");
     if ($( "#memory-show" ).hasClass("flter-ico-change")) {
            $( "#memory-show" ).html("Show more <span class='plus-ico'><i class='flaticon-down-arrow'></i></span");
       } else {
              $( "#memory-show" ).html("Show less <span class='plus-ico'><i class='flaticon-up-arrow'></i></span>");
       }
  });
  /* === FILTER COLLAPSE === */
$('#show-filter').click(function() {
    var $slider = $('#filterdiv');
    $slider.toggleClass('open_catfilter');
    // $slider.animate({
    //   left: parseInt($slider.css('left'),10) == -460 ?
    //    0 : -460
    // });
});
});
// price range slider scripts starts
     function initializePriceRangeSlider() {

    $( "#slider-range" ).slider({
      range: true,
      isRTL: false,
      min: 0,
      max: 500,
      values: [ 0, 500 ],
      slide: function( event, ui ) {
      console.log("sdfsdfsf")
      console.log(event)
      console.log(ui)
        $('#min-value').val(''+ ui.values[ 0 ]);
        $('#max-value').val('' + ui.values[ 1 ]);
        $( "#amount" ).val( "" + ui.values[ 0 ] + " to " + ui.values[ 1 ] );
      }
    });
    $('#min-value').val(''+ $( "#slider-range" ).slider( "values", 0 ));
    $('#max-value').val('' +$( "#slider-range" ).slider( "values", 1 ));
    $( "#amount" ).val( " " + $( "#slider-range" ).slider( "values", 0 ) +
      " to " + $( "#slider-range" ).slider( "values", 1 ) );
  }
 function initializertlPriceRangeSlider() {
    $( "#slider-range" ).slider({
      range: true,
      isRTL: true,
      min: 0,
      max: 500,
      values: [ 0, 500 ],
      slide: function( event, ui ) {
        $('#min-value').val(''+ ui.values[ 0 ]);
        $('#max-value').val('' + ui.values[ 1 ]);
        $( "#amount" ).val( " AED " + ui.values[ 0 ] + " to " + ui.values[ 1 ] + " AED ");
      }
    });
    $('#min-value').val(''+ $( "#slider-range" ).slider( "values", 0 ));
    $('#max-value').val('' +$( "#slider-range" ).slider( "values", 1 ));
    $( "#amount" ).val( " AED " + $( "#slider-range" ).slider( "values", 0 ) +
      " to " + $( "#slider-range" ).slider( "values", 1 ) + " AED ") ;    
  } 
  function resetSlider() {
    var $slider = $("#slider-range");
    $slider.slider("values", 0, 0);
    $slider.slider("values", 1, 500);
    $('#min-value').val(''+ $( "#slider-range" ).slider( "values", 0 ));
    $('#max-value').val('' +$( "#slider-range" ).slider( "values", 1 ));
    $( "#amount" ).val( " " + $( "#slider-range" ).slider( "values", 0 ) +
        " to " + $( "#slider-range" ).slider( "values", 1 ) );
  }

  // price range slider scripts ends
