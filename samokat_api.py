import requests
import urls
import allure

class SamokatApi:

    @allure.step('Зарегистрировать нового курьера')
    @staticmethod
    def registration_courier(body):
        return requests.post(urls.BASE_URL + urls.REG_COURIER_ENDPOINT, data=body)

    @allure.step('Авторизовать курьера')
    @staticmethod
    def login_courier(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, data=body)

    @allure.step('Создать новый заказ')
    @staticmethod
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @allure.step('Получить список всех заказов')
    @staticmethod
    def get_list_orders():
        return requests.get(urls.BASE_URL + urls.GET_LIST_ORDERS_ENDPOINT)