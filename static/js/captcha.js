$('img.captcha').click(function() {
    $.getJSON('/captcha/refresh/',function(json) {
        // This should update your captcha image src and captcha hidden input
        console.log(json);
        $("img.captcha").attr("src",json.image_url);
        $("#id_captcha_0").val(json.key);
    });

    return false;
});