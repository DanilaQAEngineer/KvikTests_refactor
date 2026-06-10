
class LocatorsForApiTests():
    AUTH_URL = 'https://restful-booker.herokuapp.com/auth'
    HEADERS_FOR_POST_AUTH = {
        'Content-Type': 'application/json'
    }
    PAYLOAD_FOR_AUTH = {
        "username": "admin",
        "password": "password123"
    }
    BASE_URL = 'https://restful-booker.herokuapp.com/booking'
    HEADERS_FOR_POST_GET = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    PAYLOAD_FOR_POST = {
        "firstname": "Имя_тест",
        "lastname": "Фамилия_тест",
        "totalprice": 300,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-04-09",
            "checkout": "2026-04-10"
        },
        "additionalneeds": "Breakfast"
    }
    HEADERS_FOR_POST_PUT = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': 'token={}'
    }
    PAYLOAD_FOR_PUT = {
        "firstname": "Новое имя",
        "lastname": "Новая фамилия",
        "totalprice": 300,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-04-11",
            "checkout": "2026-04-12"
        },
        "additionalneeds": "Breakfast"
    }
