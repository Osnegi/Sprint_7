from data import TestAuthorizationData
from helper import TestDataHelper
from samokat_api import SamokatApi

class TestLoginCourier:

    def test_successful_login_courier_code(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body= TestDataHelper.generate_login_courier_body(registration_body)
        login_request = SamokatApi.login_courier(login_body)
        assert login_request.status_code == 200

    def test_successful_login_courier_message(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body = TestDataHelper.generate_login_courier_body(registration_body)
        login_request = SamokatApi.login_courier(login_body)
        assert login_request.json()['id'] != ""

    def test_failed_mistake_login_courier_code(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body= TestDataHelper.generate_mistake_login_courier_body(registration_body)
        login_request = SamokatApi.login_courier(login_body)
        assert login_request.status_code == 404

    def test_failed_mistake_login_courier_code(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body= TestDataHelper.generate_mistake_login_courier_body(registration_body)
        login_request = SamokatApi.login_courier(login_body)
        assert login_request.json()['message'] == "Учетная запись не найдена"

    def test_failed_mistake_password_courier_code(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body= TestDataHelper.generate_mistake_password_courier_body(registration_body)
        login_request = SamokatApi.login_courier(login_body)
        assert login_request.status_code == 404

    def test_failed_mistake_password_courier_code(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body= TestDataHelper.generate_mistake_password_courier_body(registration_body)
        login_request = SamokatApi.login_courier(login_body)
        assert login_request.json()['message'] == "Учетная запись не найдена"

    def test_failed_login_courier_not_existed_error_code(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_NOT_EXISTED)
        assert login_request.status_code == 404

    def test_failed_login_courier_not_existed_error_message(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_NOT_EXISTED)
        assert login_request.json()['message'] == "Учетная запись не найдена"

    def test_failed_login_courier_empty_login_error_code(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_LOGIN)
        assert login_request.status_code == 400

    def test_failed_login_courier_empty_login_error_message(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_LOGIN)
        assert login_request.json()['message'] == "Недостаточно данных для входа"

    def test_failed_login_courier_empty_password_error_code(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_PASSWORD)
        assert login_request.status_code == 400

    def test_failed_login_courier_empty_password_error_message(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_PASSWORD)
        assert login_request.json()['message'] == "Недостаточно данных для входа"


    def test_failed_registration_courier_not_all_fields(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_NOT_ALL_FIELDS)
        assert login_request.status_code != 201