from data import TestOrderData
from helper import TestDataHelper
from samokat_api import SamokatApi

class TestGetListOrders:

    def test_successful_get_list_orders_code(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body = TestDataHelper.generate_login_courier_body(registration_body)
        SamokatApi.login_courier(login_body)

        SamokatApi.create_order(TestOrderData.ORDER_BODY)
        SamokatApi.create_order(TestOrderData.ORDER_BODY)
        SamokatApi.create_order(TestOrderData.ORDER_BODY)

        list_orders_request = SamokatApi.get_list_orders()

        assert list_orders_request.status_code == 200

    def test_successful_get_list_orders_message(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body = TestDataHelper.generate_login_courier_body(registration_body)
        SamokatApi.login_courier(login_body)

        SamokatApi.create_order(TestOrderData.ORDER_BODY)
        SamokatApi.create_order(TestOrderData.ORDER_BODY)
        SamokatApi.create_order(TestOrderData.ORDER_BODY)

        list_orders_request = SamokatApi.get_list_orders()

        assert list_orders_request.json()['orders'] != []