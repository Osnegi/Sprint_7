import requests
import urls

class SamokatApi:

    @staticmethod
    def registration_courier(body):
        return requests.post(urls.BASE_URL + urls.REG_COURIER_ENDPOINT, data=body)

    @staticmethod
    def login_courier(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, data=body)

    @staticmethod
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    def get_list_orders():
        return requests.get(urls.BASE_URL + urls.GET_LIST_ORDERS_ENDPOINT)