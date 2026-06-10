#    Библиотеки:
import pytest
import requests
import json
from directory_api_tests.locators.locators_for_api_tests import LocatorsForApiTests


# *) Авторизация в сервисе
def test_authorization_in_booker():
    response = requests.post(
        url=LocatorsForApiTests.AUTH_URL,
        headers=LocatorsForApiTests.HEADERS_FOR_POST_AUTH,
        json=LocatorsForApiTests.PAYLOAD_FOR_AUTH
    )

    auth_response = requests.post(LocatorsForApiTests.AUTH_URL, json=LocatorsForApiTests.PAYLOAD_FOR_AUTH)
    token = auth_response.json()['token']  # Извлекаем токен из ответа
    print(f'Токен получен = {token}')


# 1) Метод создания (POST): Позитивный кейс (то что получаем всё то, что ожидаем получить по запросу)
def test_create_booking():    # Создаю тест + В скобках указываю функции-фикстуры, в которых есть данные для этой ручки
    response = requests.post(    # Создаю переменную "Ответ" + Через равно обращаюсь к библиотеке REQUESTS + Через точку указываю метод запроса (POST)
        url=LocatorsForApiTests.BASE_URL,    # Указываю УРЛу, на которую стучусь (уже описана в фикстуре)
        headers=LocatorsForApiTests.HEADERS_FOR_POST_GET,  # Указываю хедеры (уже описаны в фикстуре)
        json=LocatorsForApiTests.PAYLOAD_FOR_POST  # Указываю тело POST-запроса (уже описано в фикстуре)
    )

    response_status = response.status_code
    response_body = response.json()
    created_id = response.json()['bookingid']
    print(f'Статус-код = {response_status}')
    print(f'Ответ:\n{response_body}')
    print(f'Айди заявки = {created_id}')

    get_booking_id = requests.get(
        url=f'{LocatorsForApiTests.BASE_URL}/{created_id}',
        headers=LocatorsForApiTests.HEADERS_FOR_POST_GET
    )

    status = get_booking_id.status_code
    otvet = get_booking_id.json()

    print(f'Получаю информацию по айди = {created_id}')
    print(f'Статус-код = {status}')
    print(f'Тело ответа:\n{otvet}')


# 2) Метод обновления (PUT): Позитивный кейс (то что получаем всё то, что ожидаем получить по запросу)
def test_update_booking():
    response = requests.put(
        url=f'{LocatorsForApiTests.BASE_URL}/{created_id}',
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': 'token={'
        },
        json=LocatorsForApiTests.PAYLOAD_FOR_PUT
    )

    response_status = response.status_code
    response_body = response.json()
    print(f'Статус-код = {response_status}')
    print(f'Ответ:\n{response_body}')
