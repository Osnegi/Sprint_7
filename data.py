class TestAuthorizationData:
    REGISTRATION_COURIER_BODY = {
      "login": "petrushka",
    "password": "12345",
    "firstName": "petr"
    }

    REGISTRATION_COURIER_BODY_EMPTY_LOGIN = {
        "login": "",
        "password": "12345",
        "firstName": "petr"
    }

    REGISTRATION_COURIER_BODY_EMPTY_PASSWORD = {
        "login": "petrushka",
        "password": "",
        "firstName": "petr"
    }

    REGISTRATION_COURIER_BODY_EMPTY_FIRSTNAME = {
        "login": "petrushka1",
        "password": "123456",
        "firstName": ""
    }

    REGISTRATION_COURIER_BODY_NOT_ALL_FIELDS = {
        "login": "privet",
        "password": "123456"
    }

    LOGIN_COURIER_BODY_NOT_EXISTED = {
            "login": "eukfhajsdrlgiaf",
            "password": "riogekjfdnmc"
        }

    LOGIN_COURIER_BODY_EMPTY_LOGIN = {
            "login": "",
            "password": "riogekdnmvzcc"
        }

    LOGIN_COURIER_BODY_EMPTY_PASSWORD = {
            "login": "kfhalgiafkjsd",
            "password": ""
        }

    LOGIN_COURIER_BODY_NOT_ALL_FIELDS = {
        "password": ""
    }

class TestOrderData:

    ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}