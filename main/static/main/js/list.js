

function welp(t){
    switch (t) {
        case "8":
            return "1d-2";
            break;
        case "9":
            return "1d-1";
            break;
        case "10":
            return "1d";
            break;
        case "11":
            return "1d+1";
            break;
        case "12":
            return "1d+2";
            break;
        case "13":
            return "2d-1";
            break;
        case "14":
            return "2d";
            break;
        case "16":
            return "2d+1";
            break;
    }
}

function welp2(t){
    switch (t) {
        case "8":
            return "1d-3";
            break;
        case "9":
            return "1d-2";
            break;
        case "10":
            return "1d-2";
            break;
        case "11":
            return "1d-1";
            break;
        case "12":
            return "1d-1";
            break;
        case "13":
            return "1d";
            break;
        case "14":
            return "1d";
            break;
        case "16":
            return "1d+1";
            break;
    }
}


$(document).ready(function () {
    t = $("#STR").val()
    $("#dmg_2").text(welp(t))
    $("#dmg_1").text(welp2(t))

    points = ($("#STR").val()-10)*10 + ($("#DX").val()-10)*20 + ($("#IN").val()-10)*20 + ($("#CON").val()-10)*10
    points += ($("#id_hp").val()-$("#CON").val())*5 + ($("#WIS").val()-$("#IN").val())*5 + ($("#CHR").val()-$("#IN").val())*5
    points += ($("#id_speed").val()- ($("#id_hp").val() -(- $("#DX").val()))/4)*4*5

    points += ($("#id_armour_class").val()- $("#id_speed").val())*5

    $("#class_lvl").text(points)

});

$("input").change(function () {
    t = $("#STR").val()
    $("#dmg_2").text(welp(t))
    $("#dmg_1").text(welp2(t))

    points = ($("#STR").val()-10)*10 + ($("#DX").val()-10)*20 + ($("#IN").val()-10)*20 + ($("#CON").val()-10)*10
    points += ($("#id_hp").val()-$("#CON").val())*5 + ($("#WIS").val()-$("#IN").val())*5 + ($("#CHR").val()-$("#IN").val())*5
    points += ($("#id_speed").val()- ($("#id_hp").val() -(- $("#DX").val()))/4)*4*5

    points += ($("#id_armour_class").val()- $("#id_speed").val())*5

    $("#class_lvl").text(points)

    // $(".STR").text(welp(t))
    // t = $("#DX").val()
    // $(".DX").text(welp(t))

    // t = $("#STR").val()
    // $(".STR").text(welp(t))

    // t = $("#CON").val()
    // $(".CON").text(welp(t))

    // t = $("#IN").val()
    // $(".IN").text(welp(t))

    // t = $("#WIS").val()
    // $(".WIS").text(welp(t))

    // t = $("#CHR").val()
    // $(".CHR").text(welp(t))
    
    // t = Math.floor($("#id_xp").val()/1000)
    // $("#class_lvl").text(t)
});



