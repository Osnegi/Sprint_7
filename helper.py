from faker import Faker
from data import TestAuthorizationData

class TestDataHelper:

    @staticmethod
    def modify_registration_body_request(key, value):
        body = TestAuthorizationData.REGISTRATION_COURIER_BODY.copy()
        body[key] = value
        return body

    #@allure.step('Сформировать рандомные данные для регистрации нового курьера')
    @staticmethod
    def generate_registration_body():
        fake = Faker()
        return TestDataHelper.modify_registration_body_request('login', fake.user_name())

    @staticmethod
    def generate_login_courier_body(body):
        del body['firstName']
        return body

    @staticmethod
    def generate_mistake_login_courier_body(body):
        del body['firstName']
        body['login'] = body['login'] + '1'
        return body

    @staticmethod
    def generate_mistake_password_courier_body(body):
        del body['firstName']
        body['password'] = body['password'] + '1'
        return body