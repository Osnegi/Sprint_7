from data import TestOrderData
from helper import TestDataHelper
from samokat_api import SamokatApi
import allure

class TestGetListOrders:

    @allure.title('Проверка успешного получения списка всех заказов - корректный код ответа')
    @allure.description('Проверить успешность получения списка всех заказов: код ответа 200 - позитивный сценарий')
    def test_successful_get_list_orders_code(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body = TestDataHelper.generate_login_courier_body(registration_body)
        SamokatApi.login_courier(login_body)

        SamokatApi.create_order(TestOrderData.ORDER_BODY_BLACK)
        SamokatApi.create_order(TestOrderData.ORDER_BODY_GREY)
        SamokatApi.create_order(TestOrderData.ORDER_BODY_NO_COLOUR)

        list_orders_request = SamokatApi.get_list_orders()

        assert list_orders_request.status_code == 200

    @allure.title('Проверка успешного получения списка всех заказов - корректное сообщение')
    @allure.description('Проверить успешность получения списка всех заказов: приходит сообщение со списком заказов - позитивный сценарий')
    def test_successful_get_list_orders_message(self):
        registration_body = TestDataHelper.generate_registration_body()
        SamokatApi.registration_courier(registration_body)
        login_body = TestDataHelper.generate_login_courier_body(registration_body)
        SamokatApi.login_courier(login_body)

        SamokatApi.create_order(TestOrderData.ORDER_BODY_BLACK)
        SamokatApi.create_order(TestOrderData.ORDER_BODY_GREY)

        list_orders_request = SamokatApi.get_list_orders()

        assert list_orders_request.json()['orders'] != []