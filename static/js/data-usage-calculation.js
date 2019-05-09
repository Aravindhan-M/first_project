$(document).ready(function() {
    var max_height = 526;
    var initial_bottom = 38

    var height_px = 0;
    var total_email_ht = 0;
    var total_music_ht = 0;
    var total_web_surf_ht = 0;
    var total_social_post_ht = 0;
    var total_hd_ht = 0;
    var total_gaming_ht = 0;
    var total_4k_ht = 0;
    var total_sd_ht = 0;

    var total_gb = 0;
    var total_email_gb = 0;
    var total_music_gb = 0;
    var total_web_surf_gb = 0;
    var total_social_post_gb = 0;
    var total_hd_gb = 0;
    var total_gaming_gb = 0;
    var total_4k_gb = 0;
    var total_sd_gb = 0;
    initializeRangeSlider('#emailsentRange');
    initializeRangeSlider('#musicRange');
    initializeRangeSlider('#websurfRange');
    initializeRangeSlider('#socialpost_Range');
    initializeRangeSlider('#hdVideo_Range');
    initializeRangeSlider('#gaming_Range');
    initializeRangeSlider('#_4kVideo_Range');
    initializeRangeSlider('#sdVideo_Range');



    var emailsentRange_slider = document.getElementById("emailsentRange");
    var emailsentRangeval_output = document.getElementById("emailsentRangeval");
    emailsentRangeval_output.innerHTML = emailsentRange_slider.value;
    emailsentRange_slider.oninput = function() {
        emailsentRangeval_output.innerHTML = this.value;
        update_gb(this.value,"email");
    }
    // Hours of streaming music
    var musicRange_slider = document.getElementById("musicRange");
    var musicRangeval_output = document.getElementById("musicRangeval");
    musicRangeval_output.innerHTML = musicRange_slider.value;
    musicRange_slider.oninput = function() {
        musicRangeval_output.innerHTML = this.value;
        update_gb(this.value,"music");

    }
    // Hours of surfing the web
    var websurfRange_slider = document.getElementById("websurfRange");
    var websurfRangeval_output = document.getElementById("websurfRangeval");
    websurfRangeval_output.innerHTML = websurfRange_slider.value;
    websurfRange_slider.oninput = function() {
        websurfRangeval_output.innerHTML = this.value;
        update_gb(this.value,"web");
    }
    // Social media posts with photos
    var socialpost_Range_slider = document.getElementById("socialpost_Range");
    var socialpost_Rangeval_output = document.getElementById("socialpost_Rangeval");
    socialpost_Rangeval_output.innerHTML = socialpost_Range_slider.value;
    socialpost_Range_slider.oninput = function() {
        socialpost_Rangeval_output.innerHTML = this.value;
        update_gb(this.value,"post");
    }
    //  Hours of streaming standard-definition video
    var sdVideo_Range_slider = document.getElementById("sdVideo_Range");
    var sdVideo_Rangeval_output = document.getElementById("sdVideo_Rangeval");
    sdVideo_Rangeval_output.innerHTML = sdVideo_Range_slider.value;
    sdVideo_Range_slider.oninput = function() {
        sdVideo_Rangeval_output.innerHTML = this.value;
        update_gb(this.value,"sd");
    }
    //  Hours of streaming standard-definition video
    var hdVideo_Range_slider = document.getElementById("hdVideo_Range");
    var hdVideo_Rangeval_output = document.getElementById("hdVideo_Rangeval");
    hdVideo_Rangeval_output.innerHTML = hdVideo_Range_slider.value;
    hdVideo_Range_slider.oninput = function() {
        hdVideo_Rangeval_output.innerHTML = this.value;
        update_gb(this.value,"hd");
    }
    //  Hours of streaming 4K video
    var _4kVideo_Range_slider = document.getElementById("_4kVideo_Range");
    var _4kVideo_Rangeval_output = document.getElementById("_4kVideo_Rangeval");
    _4kVideo_Rangeval_output.innerHTML = _4kVideo_Range_slider.value;
    _4kVideo_Range_slider.oninput = function() {
        _4kVideo_Rangeval_output.innerHTML = this.value;
        update_gb(this.value,"4k");
    }
    //  Time spent online gaming
    var gaming_Range_slider = document.getElementById("gaming_Range");
    var gaming_Rangeval_output = document.getElementById("gaming_Rangeval");
    gaming_Rangeval_output.innerHTML = gaming_Range_slider.value;
    gaming_Range_slider.oninput = function() {
        gaming_Rangeval_output.innerHTML = this.value;
       update_gb(this.value,"game");

    }

    var total_usage_count = document.getElementById("totalUsageCount");

    function update_gb(value,param){
    if (param == 'email'){
    total_email_ht = parseInt(value) * 160
    total_email_gb = convert_to_gb(total_email_ht)
    }
    if (param == 'music'){
    total_music_ht = parseInt(value) * 4000
    total_music_gb = convert_to_gb(total_music_ht)
    }
    if (param == 'web'){
    total_web_surf_ht= parseInt(value) * 15000
    total_web_surf_gb = convert_to_gb(total_web_surf_ht)
    }
    if (param == 'post'){
    total_social_post_ht = parseInt(value) * 5000
    total_social_post_gb = convert_to_gb(total_social_post_ht)
    }
    if (param == 'sd'){
    total_sd_ht = parseInt(value) * 702000
    total_sd_gb = convert_to_gb(total_sd_ht)
    }
    if (param == 'hd'){
    total_hd_ht = parseInt(value) * 2502000
    total_hd_gb = convert_to_gb(total_hd_ht)
    }
    if (param == '4k'){
    total_4k_ht = parseInt(value) * 5850000
    total_4k_gb = convert_to_gb(total_4k_ht)
    }
     if (param == 'game'){
    total_gaming_ht = parseInt(value) * 12000
    total_gaming_gb = convert_to_gb(total_gaming_ht)
    }



    calculate_value()
    calculate_height()

    }

    function calculate_height(){
    var temp_height;
    var bottom;
    temp_height = total_email_ht + total_music_ht + total_web_surf_ht + total_social_post_ht + total_hd_ht + total_gaming_ht + total_4k_ht + total_sd_ht
    height_px = temp_height* 0.000000432
    $(".dcalc_bari").height(height_px);
    bottom = initial_bottom + height_px;
    if (height_px >= max_height){
    bottom = initial_bottom + max_height;
    }
    $(".dcalc_usage_flag").css('bottom', bottom)
    }

    function calculate_value(){
        total_gb = total_email_gb + total_music_gb + total_web_surf_gb + total_social_post_gb + total_sd_gb + total_hd_gb + total_4k_gb + total_gaming_gb


        total_usage_count.innerHTML = parseFloat(Math.round(total_gb * 100) / 100).toFixed(2);

    }

    function convert_to_gb(kb){


        return  (kb / 1000)/1000;

    }
    function reset_values(){
      total_gb = 0;
      total_email_gb = 0;
      total_music_gb = 0;
      total_web_surf_gb = 0;
      total_social_post_gb = 0;
      total_hd_gb = 0;
      total_gaming_gb = 0;
      total_4k_gb = 0;
      total_sd_gb = 0;
      total_email_ht = 0;
      total_music_ht = 0;
      total_web_surf_ht = 0;
      total_social_post_ht = 0;
      total_hd_ht = 0;
      total_gaming_ht = 0;
      total_4k_ht = 0;
      total_sd_ht = 0;


    }

    function reset_inner(id){
    id.innerHTML = 0;
    }
    $(".reset_datacalc_btn").click(function(){
     initializeRangeSlider(emailsentRange_slider)
     initializeRangeSlider(musicRange_slider)
     initializeRangeSlider(websurfRange_slider)
     initializeRangeSlider(socialpost_Range_slider)
     initializeRangeSlider(sdVideo_Range_slider)
     initializeRangeSlider(hdVideo_Range_slider)
     initializeRangeSlider(_4kVideo_Range_slider)
     initializeRangeSlider(gaming_Range_slider)
     reset_inner(emailsentRangeval_output)
     reset_inner(musicRangeval_output)
     reset_inner(websurfRangeval_output)
     reset_inner(socialpost_Rangeval_output)
     reset_inner(sdVideo_Rangeval_output)
     reset_inner(hdVideo_Rangeval_output)
     reset_inner(_4kVideo_Rangeval_output)
     reset_inner(gaming_Rangeval_output)
     reset_values()


    $(".dcalc_usage_flag").css('bottom', initial_bottom);
    $(".dcalc_bari").height(0);
    total_usage_count.innerHTML = "0.00";


    })

});


