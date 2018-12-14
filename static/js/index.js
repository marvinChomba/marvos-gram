$(document).ready(() => {
    $(".like-btn").click((e) => {
        e.preventDefault()
        id = $(".like-btn").attr("value")
        section = $("#image-section")
        $.ajax({
            "url":"/ajax/like/",
            "type": "POST",
            "data": {"id":id, "scrfmiddlewaretoken": },
            "dataType":"json",
            "success": function(res) {
                alert('hey')
            }
        })
    })
})