#    Библиотеки:
import pytest
import requests
import json

#    Тесты:
# 1) Метод создания (POST): Позитивный кейс (то что получаем всё то, что ожидаем получить по запросу)
# def test_create_post(base_url_jsonplaceholder, posts_endpoint, json_headers, payload_for_post_create):
#
#     response = requests.post(
#         url=base_url_jsonplaceholder + posts_endpoint,
#         json=payload_for_post_create,
#         headers=json_headers
#     )
#
#     assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
#
#     response_data = response.json()
#
#     assert 'userId' in response_data, "В ответе нет userId"
#     print(f"Пост создан: {response_data['userId']}")
#
#     booking = response_data['posts']
#     assert booking['userId'] == '1004', f"Ожидался \"Имя тестового пользователя\", получен {userId['firstname']}"
#     assert booking['id'] == '110044', f"Ожидался \"Фамилия тестового пользователя\", получен {userId['lastname']}"
#     assert booking['title'] == 'Заголовок_4', f"Ожидалась 500, получена {booking['totalprice']}"
#     assert booking['body'] == 'Какое-то тело', "depositpaid должен быть True"
#     print("Все фактические результаты соответствуют ожидаемым.")

@pytest.mark.regression('Тест в рамках регресса')    # Также можем промаркировать тип тестирования
def test_get_users():
    url = 'https://jsonplaceholder.typicode.com/users'
    print(f'Запрос ↓: \n{url}')
    result = requests.get(url)
    print(f'Статус-код ↓: \n{result.status_code}')
    assert 200 == result.status_code

@pytest.mark.smoke('Соук-тест')    # Также можем промаркировать тип тестирования
def test_get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    print(f'Запрос ↓: \n{url}')
    result = requests.get(url)
    print(f'Статус-код ↓: \n{result.status_code}')
    assert 200 == result.status_code

@pytest.mark.skip('Тест пропущен.')    # Эту маркировку используем тогда, когда хотим пропустить какой-то тест
def test_get_post_1():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    print(f'Запрос ↓: \n{url}')
    result = requests.get(url)
    print(f'Статус-код ↓: \n{result.status_code}')
    assert 200 == result.status_code
