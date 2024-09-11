import requests
import random
import string
import allure

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


from faker import Faker
from data import TestAuthorizationData


class TestDataHelper:
    @allure.step('Изменить шаблон данных курьера')
    @staticmethod
    def modify_registration_body_request(key, value):
        body = TestAuthorizationData.REGISTRATION_COURIER_BODY.copy()
        body[key] = value

        return body


    @allure.step('Сформировать рандомные данные для регистрации нового курьера')
    @staticmethod
    def generate_registration_body():
        fake = Faker()
        return TestDataHelper.modify_registration_body_request('login', fake.user_name())

    @allure.step('Сформировать данные для авторизации курьера из данных вновь зарегистрированного курьера')
    @staticmethod
    def generate_login_courier_body(body):
        del body['firstName']
        return body

    @allure.step('Создать данные для авторизации курьера с ошибкой в логине')
    @staticmethod
    def generate_mistake_login_courier_body(body):
        del body['firstName']
        body['login'] = body['login'] + '1'
        return body

    @allure.step('Создать данные для авторизации курьера с ошибкой в пароле')
    @staticmethod
    def generate_mistake_password_courier_body(body):
        del body['firstName']
        body['password'] = body['password'] + '1'
        return body