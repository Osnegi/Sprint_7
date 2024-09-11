from data import TestOrderData
from helper import TestDataHelper
from samokat_api import SamokatApi

class TestCreateOrder:

    def test_successful_create_order_code(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body = TestDataHelper.generate_login_courier_body(registration_body)
        SamokatApi.login_courier(login_body)

        order_request = SamokatApi.create_order(TestOrderData.ORDER_BODY)
        assert order_request.status_code == 201

    def test_successful_create_order_message(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body = TestDataHelper.generate_login_courier_body(registration_body)
        SamokatApi.login_courier(login_body)

        order_request = SamokatApi.create_order(TestOrderData.ORDER_BODY)

        assert order_request.json()['track'] != ""