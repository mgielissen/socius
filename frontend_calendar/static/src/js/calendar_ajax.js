$(document).ready(function () {
    if ($("#calendar_container").length) {
        display_calendar('');
    }
});

$(function() {
    $(".calendar_direction").on("click", function(event) {
        var direction = $(this).attr("id");
        console.log('inside click event');
        display_calendar(direction);
    });
});

function display_calendar(direction) {
    var month = $("#month").val();
    var year = $("#year").val();
    $.ajax({
        type:"POST",
        url: "/web/public-calendar/",
        data: ({
            'direction' : direction,
            'month': month,
            'year': year
        }),
        async: false,
        dataType: "json",
        success: function(data) {
            $("#month").val(data.month);
            $("#year").val(data.year);
            $("#calendar_container").html(data.html_calendar_code);
        }
    });
}
