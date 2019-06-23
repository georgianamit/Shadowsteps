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

function prepareBtn(data, deleteBtnClass) {
    // return `<a type="button" style="font-size: 18px; color: white;" class="mb-2 btn btn-sm btn-info mr-1"> ${data.language} &nbsp;<span style="font-size: 14px; color: Tomato;"><button data-id="${data.id}" class="fas fa-times cancel-button langDeleteBtn" ></button></a>`
    if ('language' in data) {
        txt = data.language
    } else
    if ('framework' in data) {
        txt = data.framework
    } else
    if ('platform' in data) {
        txt = data.platform
    }
    return `<a type="button" style="font-size: 16px; color: white;" class="mb-2 btn btn-sm btn-info mr-1"> ${txt} &nbsp;<button type="button" data-id="${data.id}" class="close ${deleteBtnClass}" aria-label="Close"> <span style="font-size: 24px; color: Tomato; backgroud-color: white;">&times;</span></button></a>`
}

function deleteElement(elm, uri) {
    ID = $(elm).data('id')
    $.ajax({
        url: `/api/${uri}/${ID}/`,
        type: 'delete',
        dataType: 'json',
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function (data) {
            $(elm).parent().remove()
        }
    });
}

function addDeleteEvent(deleteBtnClass, uri) {
    $('.' + deleteBtnClass).each((i, elm) => {
        $(elm).on("click", (e) => {
            console.log(e)
            deleteElement($(elm), uri)
        })
    })

}

function loadProfSetting(listUri, editUri, listID, deleteBtnClass) {
    $.ajax({
        url: `/api/${listUri}/`,
        type: 'get',
        datatype: 'Json',
        success: function (data) {
            let btn = ''
            data.forEach(l => {
                btn += prepareBtn(l, deleteBtnClass);

            });
            $('#' + listID).append(btn)
            addDeleteEvent(deleteBtnClass, editUri)
        }

    })
}

$('#sv-lang-btn').click(function (event) {
    event.preventDefault()
    $.ajax({
        url: '/api/languages/',
        type: 'post',
        data: {
            'language': $('#language').val(),
            'level': $('#lang-level').val(),
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function (data) {
            $('#list-languages').append(prepareBtn(data, 'langDeleteBtn'))
            addDeleteEvent('langDeleteBtn', 'language')
        }
    })
})

$('#sv-fw-btn').click(function (event) {
    event.preventDefault()
    $.ajax({
        url: '/api/frameworks/',
        type: 'post',
        data: {
            'framework': $('#framework').val(),
            'level': $('#fw-level').val(),
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function (data) {
            $('#list-frameworks').append(prepareBtn(data, 'fwDeleteBtn'))
            addDeleteEvent('fwDeleteBtn', 'framework')
        }
    })
})

$('#sv-pf-btn').click(function (event) {
    event.preventDefault()
    $.ajax({
        url: '/api/platforms/',
        type: 'post',
        data: {
            'platform': $('#platform').val(),
            'level': $('#pf-level').val(),
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function (data) {
            $('#list-platforms').append(prepareBtn(data, 'pfDeleteBtn'))
            addDeleteEvent('pfDeleteBtn', 'platform')
        }
    })
})

loadProfSetting('languages', 'language', 'list-languages', 'langDeleteBtn')
loadProfSetting('frameworks', 'framework', 'list-frameworks', 'fwDeleteBtn')
loadProfSetting('platforms', 'platform', 'list-platforms', 'pfDeleteBtn')