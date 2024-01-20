import configuration
import data
import requests


# Создаю заказ
def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.BODY,
                         headers=data.HEADERS)


# Получение информацию о заказе
def order_info_about_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track),
                        headers=data.HEADERS)
