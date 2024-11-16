 async function fetchLenders() {
        // Здесь  код для запроса к базе данных
        data = window.Telegram.WebApp.initDataUnsafe
console.log(data)
        res = await fetch(`https://pumibari.schtil.com:5005/get_user_lenders?debtor_tg=${data['user']['username']}`)
        res = 
        res = await res.json();
        console.log(res);
        return res
        // Возвращаем для примера статичные данные
        // resolve([
        //     { lenders_tg: 'user1', amount: 100 },
        //     { lenders_tg: 'user2', amount: 200 },
        //     { lenders_tg: 'user3', amount: 150 }
        // ]);
    }


// Функция для создания HTML элементов карточек пользователей
function createCard(lender) {
    const card = document.createElement('div');
    card.classList.add('card');
    card.id = `user-${lender.lenders_tg}`; // Устанавливаем уникальный id для каждой карточки

    const nameElement = document.createElement('p');
    const total_sum_element = document.createElement('h2');
    total_sum_element.textContent = `${lender.lenders_tg}`;//тег с тотальной суммой вашего долга
    nameElement.textContent = `${lender.lenders_tg}`;  
    const amountElement = document.createElement('p');
    nameElement.classList.add('name_of_user');
    amountElement.textContent = `Сумма: ${lender.amount} ₽`;

    const payButton = document.createElement('button');
    payButton.textContent = 'pay';
    payButton.classList.add('pay_button');
    payButton.addEventListener('click', () => {
        const targetCard = document.getElementById(`user-${lender.lenders_tg}`);
        targetCard.style.display = 'none';
        fetch('https://pumibari.schtil.com:5005/remove_debt?lender_tg=' + lender.lenders_tg + '&debtor_tg=' + '@' +`${data["user"]["username"]}`, {method: 'DELETE'});
    });

    card.appendChild(nameElement);
    card.appendChild(amountElement);
    card.appendChild(payButton);

    return card;
}

// Выбираем контейнер, в который будем добавлять карточки пользователей
const container = document.getElementById('users-container');

// Получаем данные о должниках и отображаем карточки на странице
fetchLenders().then(lenders => {
    lenders.forEach(lender => {
        const card = createCard(lender);
        container.appendChild(card);
    });
}).catch(error => {
    console.error('Ошибка при получении данных: ', error);
});

$(document).ready(async function() {
    $('.header_burger').click(async function(event) {
        $(this).toggleClass('active');
        $('.header_menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
});
