$(function () {
    register_clickhandler();
    load_rooms();
    //$("#message").hide();
    $("#end").hide();
});

var room = -1;
var level = -1;
var hints;
var level_counter = 0;
var hint_counter = 0;

function register_clickhandler() {
    $("#btn_submit").click(function () {
        upload();
    });
    $("#btn_hint").click(function () {
        show_hint();
    });
    $("#load").click(function () {
        notify("Lade Räume...", false, false);
        console.log("loading rooms...");
        var deferreds = [];
        $("input.room:checked").each(function (elem) {
            room_name = ($(this).val());
            deferreds.push(
                $.post("/rooms/" + room_name, function (data) {
                    console.log("room loaded: ", room_name);
                    //console.log(data);
                })
            );
        }).promise().done(function () {
            $.when.apply($, deferreds).done(function () {
                show_loaded_rooms();
                next_room(); //i.e. the first one
            });
        });
    });
}

function load_rooms() {
    $.get("/rooms/available", function (data) {
        data.forEach(function (item, index) {
            $("#rooms").append("<input type='checkbox' class='room' value='" + item + "'>" + item + "</input><br>");
        });
    });
}

function show_loaded_rooms() {
    $("#game").show();
    $("#load_rooms").hide();
    $.get("/rooms", function (data) {
        notify("Räume geladen: " + data.room_names, true, true)
    });
}

function next_room() {
    room++;
    $.get("/rooms/" + room,
        function (room_data) {
            level = -1;
            show_room_data(room_data);
            next_level();
        }).fail(
            function (data) {
                console.log("no more rooms");
                end_game();
            }
        );
}

function notify(message, replace=false, fadeout=true) {
	if(replace){
		console.log(message, replace, fadeout);
		$("#message").empty();
	}
	
	p = $(document.createElement("p"));
	p.text(message);
	p.addClass("messageitem")
	$("#message").append(p)
		
    if (fadeout) {
		p.fadeTo(500, 1).delay(3500).fadeTo(500, 0, function(){p.remove()});
    }
    else {
        p.fadeTo(500, 1)
    }
}

function show_hint() {
    displayed_number_of_hints = $("#hints li").length
    if (displayed_number_of_hints < hints.length) {
        $("#hints").append("<li>" + hints[displayed_number_of_hints] + "</li>");
        $("#hints").show();
        hint_counter++;
    }
    else {
        notify("Keine weiteren Hinweise.");
    }
}

function next_level() {
    level++;
    $.get("/rooms/" + room + "/levels/" + level, function (level_data) {
        show_level(level_data);
        level_counter++;
    }).fail(function () {
        next_room();
    });
}

function show_room_data(data) {
    $("#room").text(data.room_name);
    $("#author").text(data.author);
    $("#levels").text(data.levels);
}

function show_level(data) {
    $("#level").text(level + 1);
    $("#task").empty();
    $("#hints").empty().hide();

    data.tasks.forEach(function (item, index) {
        $("#task").append("<li>" + item + "</li>")
    });

    hints = data.hints;
}

function end_game() {
    $("#task").empty();
    $("#game").hide();
    $("#end").html("Du hast " + level_counter + " Level gemeistert und " + hint_counter + " Tipp(s) benötigt.<br><a href='/'>Ein neues Spiel starten</a>").show();
    notify("Das Spiel ist zu Ende.")
}

function upload() {

    var form = document.getElementById("upload");
    var formData = new FormData(form);
    $.ajax({
        type: "POST",
        enctype: "multipart/form-data",
        url: "/rooms/" + room + "/levels/" + level + "/solve",
        data: formData,
        processData: false,
        contentType: false,
        cache: false,
        success: function (data) {
            show_result(data);
        }
    });
}

function show_result(result) {
    if (result.correct) {
        notify("Deine Lösung ist: " + result.solution + ". Juhu, das war richtig!");
        next_level();
    }
    else {
        notify("Deine Lösung ist: " + result.solution + ". Das ist leider falsch.");
    }
}