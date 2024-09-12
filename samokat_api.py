import requests
import urls
import allure

class SamokatApi:

    @allure.step('Метод регистрирует нового курьера')
    def registration_courier(body):
        return requests.post(urls.BASE_URL + urls.REG_COURIER_ENDPOINT, data=body)

    @allure.step('Метод авторизует курьера')
    def login_courier(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, data=body)

    @allure.step('Метод создает новый заказ')
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @allure.step('Метод получает список всех заказов')
    def get_list_orders():
        return requests.get(urls.BASE_URL + urls.GET_LIST_ORDERS_ENDPOINT)