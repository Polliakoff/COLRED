// $( window ).resize(function() {
//     $(".floating_search").css("display","none")
// });

$( "#main_search" ).change(function() {
    value = $("#main_search").val().toLowerCase();
    if(value==""){
        $("#search_operand").css("display","none")
    } else {
        $("#search_operand").addClass("floating_search")
        $("#search_operand").css("left", $("#main_search").offset().left - 42);
        $("#search_operand").css("display","flex")

        $( ".search_field>a" ).each(function() {
            t = $( this ).attr("filter").toLowerCase()
            // if($( this ).attr("filter")=="")
            if(t.indexOf(value)!=-1) {
                $( this ).css("display","unset");
            } else {
                $( this ).css("display","none");
            }
        });

        $( ".new_one" ).css("display","unset");
    }
    document.activeElement.blur();
});


$( "#hamb_search" ).change(function() {
    value = $("#hamb_search").val().toLowerCase();
    if(value==""){
        $("#search_operand").css("display","none")

    } else {
        $("#search_operand").removeClass("floating_search")
        $(".floating_search").css("display","flex")


        $( ".search_field>a" ).each(function() {
            t = $( this ).attr("filter").toLowerCase()
            // if($( this ).attr("filter")=="")
            if(t.indexOf(value)!=-1) {
                $( this ).css("display","unset");
            } else {
                $( this ).css("display","none");
            }
        });

        $( ".new_one" ).css("display","unset");
    }
    document.activeElement.blur();
});




$( ".hamburger" ).on("click", function() {    
    if ($(".hamburger_main").css("display") != "flex" ){
        $( ".hamburger_main" ).css("display", "flex");
        $( ".mainf" ).css("display", "none");
                $("footer").css("display","flex")
    }
    else{
        $( ".hamburger_main" ).css("display", "none");
        $( ".mainf" ).css("display", "flex");
        $("footer").css("display","none")
    }
});
var path;

function temp_func() {
    $('#head_black').attr("href",path);
}

function revert() {
    $('#head_black').attr("href","");
}



$( "#toggle-button2" ).change(function() {
    $("#toggle-button1").prop('checked', $("#toggle-button2").is(':checked'));
    if($("#toggle-button2").is(':checked')) temp_func();
    else revert()
});

$( "#toggle-button1" ).change(function() {
    $("#toggle-button2").prop('checked', $("#toggle-button1").is(':checked'));
    if($("#toggle-button2").is(':checked')) temp_func();
    else revert()
});

window.onload = function(){
    path = $('#head_black').attr("href");
    console.log($("#toggle-button1").is(':checked'));
    if($("#toggle-button1").is(':checked')){
        temp_func();
    } else revert()
}

