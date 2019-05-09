$(document).ready(function(){

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

			// to denote the value of dropdown in text to button
			$(".dropdown-menu li a").click(function(){
			  $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
			  $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
        
			});
        $('.lang_dropdwn_btn').click(function(){
          if ($(this).text() == "Arabic ") {
            $("html").attr("dir", "rtl");
            $("#styleLink").attr('href', '/static/css/rtl_style.css');
          }
          if ($(this).text() == "English ") {
            $("html").attr("dir", "");
            $("#styleLink").attr('href', '/static/css/style.css');
          }
        });
			$('.currncy_dropdwn_btn').html('USD<span class="caret"></span>') ;
      $('.lang_dropdwn_btn').html('English<span class="caret"></span>') ;
      
	$('.top_products_slides1').not('.slick-initialized').slick({ 
		slidesToShow: 4,
  		slidesToScroll: 1,
  		variableWidth: true,
      rtl: true,
	  // autoplay: true,
	  // autoplaySpeed: 2000,
	   nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
	  prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>',	
    responsive: [
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2

        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
});
$('.top_products_slides2').not('.slick-initialized').slick({ 
		slidesToShow: 4,
  		slidesToScroll: 1,
  		variableWidth: true, rtl: true,
  autoplay: true,
  autoplaySpeed: 2000,
   nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
  prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>',			
  responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        infinite: true,
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,slidesToScroll: 1,centerMode:false,variableWidth:false,infinite:true
      }
    }
  ]
});
$('.provider_slider').not('.slick-initialized').slick({ 
    slidesToShow: 5,
      slidesToScroll: 1,centerMode:true, rtl: true,
    // autoplaySpeed: 2000,
     nextArrow: '<a class="carousel-control right carousel-control-next" href="#myCarousel" data-slide="next"><i class="flaticon-next"></i></a>',
    prevArrow: '<a class="carousel-control left carousel-control-prev" href="#myCarousel" data-slide="prev"><i class="flaticon-back"></i></a>',     
  responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2

      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

   $('input[type="range"]').change(function () {
          var val = ($(this).val() - $(this).attr('min')) / ($(this).attr('max') - $(this).attr('min')); 
          $(this).css('background-image',
                '-webkit-gradient(linear,  right top, left top,'
                + 'color-stop(' + val + ', #3c94e6), '
                + 'color-stop(' + val + ', #cfe1f1)'
                + ')'
                ); 
});