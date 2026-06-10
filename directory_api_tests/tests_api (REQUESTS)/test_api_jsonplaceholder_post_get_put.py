#   Библиотеки:
import pytest
import requests
#   ____________________________________________________________________________________________________________________
#   Локаторы:
BASE_URL = 'https://jsonplaceholder.typicode.com/posts'
BASE_URL_FOR_PUT = 'https://jsonplaceholder.typicode.com/posts/1'
# HEADERS_FOR_POST = {
#     'Content-Type': 'application/json',
#     'Accept': 'application/json'
# }
PAYLOAD_FOR_POST = {
    "userId": 1,
    "title": "(какой-то заголовок)",
    "body": "(какое-то тело)"
}
#   ____________________________________________________________________________________________________________________

# Кейс_1: Создание POST-запроса
def test_create_booking():
    print(f'\n\t1) Создаю заявку:\n')
    response = requests.post(
        url=BASE_URL,
        json=PAYLOAD_FOR_POST
    )

    response_status = response.status_code
    response_otvet = response.json()
    created_post = response.json()['id']

    print(f'Статус-код = {response_status}')
    print(f'Тело ответа:\n{response_otvet}')
    print(f'ID созданного бронирования = {created_post}\n')

    print(f'\n\t2) Получаю инфу по только что созданной заявке:\n')
    get_booking_id = requests.get(
        url=f'{BASE_URL}/{created_post}'
    )

    status = get_booking_id.status_code
    otvet = get_booking_id.json()

    print(f'Получаю информацию по айди = {created_post}')
    print(f'Статус-код = {status}')
    print(f'Тело ответа:\n{otvet}')

def test_post_put():
    response = requests.put(    # Путом нужно быть поаккуратней, т.к. если мы им меняем только часть полей, то остальные автоматом затираются (в них значения становятся по дефолту)
        url=BASE_URL_FOR_PUT,
        json={    # в теле указываем поля, которые мы хотим обновить
            "title": "Новый заголовок",
            "body": "Новое тело"
        }
    )

    response_status_code = response.status_code
    response_body = response.json()

    print('\tПрогоняю метод PUT:')
    print(f'\nСтатус код = {response_status_code}')
    print(f'Ответ:\n{response_body}')

    # get_new_post = requests.get(
    #     url=BASE_URL_FOR_PUT
    # )
    #
    # response_get_status = response.status_code
    # response_get_body = response.json()
    #
    # print(f'Статус = {response_get_status}')
    # print(f'Ответ:\n{response_get_body}')

def test_post_patch():
    response = requests.patch(
        url=BASE_URL_FOR_PUT,
        json={    # в теле указываю только те поля, которые хочу обновить
            "title": "Новый заголовок",
            "body": "Новое тело"
        }
    )

    response_status_code = response.status_code
    response_body = response.json()

    print('\tПрогоняю метод PATCH:')
    print(f'\nСтатус код = {response_status_code}')
    print(f'Ответ:\n{response_body}')
