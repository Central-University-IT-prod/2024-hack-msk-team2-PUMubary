async function req(){
    a = await fetch('https://pumibari.schtil.com:5005/?id=1')
    a = await a.json()
    console.log(a)
    document.getElementById('res').innerHTML = a['site']
    console.log(a['data'])
}

// function open(key) {
//     setTimeout(move_to_place(key), 1000);
// }

function move_to_place(key) {
    switch (key) {
        case 1:
            window.location.href = "add.html";
            break;
        case 2:
            window.location.href = "owe.html";
            break;
        case 3:
            window.location.href = "debtors.html";
            break;
        case 4:
            window.location.href = "groups.html";
            break;
    }
}

$(document).ready(function() {
    $('.header_burger').click(function(event) {
        $(this).toggleClass('active');
        $('.header_menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
});