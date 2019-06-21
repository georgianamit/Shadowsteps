$('#browse').click(function () {
    $("#browsefield").click();
    $(this).parents('form').submit();
})

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function prepareLangBtn(data) {
    return `<button type="button" data-id="${data.id}" class="mb-2 btn btn-sm btn-info mr-1 langDeleteBtn"> ${data.language} &nbsp;<span style="font-size: 14px; color: Tomato;"><i class="fas fa-times " ></i></button>`

}

function deleteLang(elm) {
    langID = $(elm).data('id')
    $.ajax({
        url: `/api/language/${langID}/`,
        type: 'delete',
        dataType: 'json',
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function (data) {
            console.log(getCookie("csrftoken"))
            $(elm).remove()
        }
    });
}

function addDeleteEvent() {
    $('.langDeleteBtn').each((i, elm) => {
        $(elm).on("click", (e) => {
            console.log(e)
            deleteLang($(elm))
        })
    })

}

function loadUserLanguages() {
    $.ajax({
        url: '/api/languages/',
        type: 'get',
        datatype: 'Json',
        success: function (data) {
            let langBtn = ''
            data.forEach(l => {
                langBtn += prepareLangBtn(l);

            });
            $('#sv-languages').append(langBtn)
            addDeleteEvent()
        }

    })
}

$('#sv-btn').click(function (event) {
    event.preventDefault()
    $.ajax({
        url: '/api/languages/',
        type: 'post',
        data: {
            'language': $('#language').val(),
            'level': $('#level').val(),
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function (data) {
            $('#sv-languages').append(prepareLangBtn(data))
            addDeleteEvent()
        }
    })
})

loadUserLanguages();