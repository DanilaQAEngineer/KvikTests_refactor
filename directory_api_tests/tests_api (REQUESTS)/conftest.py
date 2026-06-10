import pytest
from requests.auth import HTTPBasicAuth

#    Фикстуры для https://restful-booker.herokuapp.com
# 1) Авторизация
@pytest.fixture
def base_url_booker_auth():    # Авторизация в сервисе
    return 'https://restful-booker.herokuapp.com/auth'

@pytest.fixture    # Хедеры для авторизации
def json_headers_for_auth():
    return {
        "Content-Type": "application/json"
    }

@pytest.fixture
def payload_for_authorization():
    return {
    "username" : "admin",
    "password" : "password123"
    }
# ______________________________________________________________________________________________________________________
@pytest.fixture
def base_url_booker():
    return 'https://restful-booker.herokuapp.com/booking'

@pytest.fixture
def json_headers_for_booking_create():    # Хедеры для создания
    return {
        "Content-Type": "application/json"
    }

@pytest.fixture
def json_headers_for_booking_update():    # Хедеры для редактирования
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "token=1dd87778d9aacaf"
    }

@pytest.fixture
def payload_for_booking_create():    # Тело для ручки POST: /booking
    return {
        "firstname": "Имя",
        "lastname": "Фамилия",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-04-09",
            "checkout": "2026-04-10"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture
def payload_for_booking_update():    # Тело для ручки PUT: /booking/{ID}
    return {
        "firstname": "Новое имя",
        "lastname": "Новая фамилия",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-04-10",
            "checkout": "2026-04-11"
        },
        "additionalneeds": "Breakfast"
    }

#    Фикстуры для https://jsonplaceholder.typicode.com
# @pytest.fixture
# def base_url_jsonplaceholder():
#     return 'https://jsonplaceholder.typicode.com'
#
# @pytest.fixture
# def posts_endpoint():
#     return '/posts'
#
# @pytest.fixture
# def json_headers():
#     return {
#         "Content-Type": "application/json",
#         "Accept": "application/json"
#     }
#
# @pytest.fixture
# def payload_for_post_create():
#     return {
#     "userId": 1004,
#     "id": 110044,
#     "title": "Заголовок_4",
#     "body": "Какое-то тело"
#     }
