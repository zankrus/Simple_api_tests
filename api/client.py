"""Модуль для клиента сервиса."""
import logging

from apitist.hooks import PrepRequestInfoLoggingHook, ResponseInfoLoggingHook
from apitist.requests import session, ApitistResponse

logger = logging.getLogger("test_logger")


class APIClient:
    PURCHASE_BY_CLIENT_URL = "service/v1/item/purchase/by-client"
    CREATE_CLIENT_URL = "v1/client/create"
    CREATE_ORDER_URL = "v1/order/create"

    def __init__(self, app_hostname: str, username: str = None, password: str = None):
        """Конструктор APIClient."""
        self.s = session()
        self.s.add_hook(PrepRequestInfoLoggingHook)
        self.s.add_hook(ResponseInfoLoggingHook)
        self.app_hostname = app_hostname
        self.auth = (username, password)

        logger.info(f"Создаем экземпляр класса APIClient. Hostname - {self.app_hostname}")

    def create_new_client(self, name: str = '', surname: str = '', phone: str = '') -> ApitistResponse:
        """
        Создание клиента.
        :param phone: Номер телефон клиента
        :param surname: Фамилия клиента
        :param name: Имя клиента
        :return: Ответ от сервера.
        """
        data = {
            "name": name,
            "surname": surname,
            "phone": phone

        }
        logger.info("Создаем клиента")
        url = self.app_hostname + self.CREATE_CLIENT_URL
        response = self.s.post(url=url, json=data)
        try:
            client_id = response.json()["client_id"]
            logger.info(f"Создан клиент с id {client_id}")
        except KeyError:
            logger.info(f'Произошла ошибка.Клиент не создан')
        return response

    def create_new_order(self, client_id: str = None, address: str = None, phone: str = None,
                         item_id: str = None, price: str = None, quantity: str = None) -> ApitistResponse:
        """
        Метод создания нового заказа.
        :param client_id: Айди клиента
        :param address:  Адрес клиента
        :param phone:  Телефон клиента
        :param item_id: Айди товара
        :param price: Цена товара
        :param quantity: Количество товара
        :return: Ответ от сервера
        """
        logger.info("Создаем заказ]")
        url = self.app_hostname + self.CREATE_ORDER_URL
        data = {
            "client_id": client_id,
            "address": address,
            "phone": phone,
            "items": [
                {
                    "item_id": item_id,
                    "price": price,
                    "quantity": quantity,
                }
            ]
        }

        response = self.s.post(url=url, json=data)
        try:
            order_id = response.json()["order_id"]
            order_number = response.json()["order_number"]
            logger.info(f"Создан заказ с id {order_id} и номером - {order_number}")
        except KeyError:
            logger.info(f'Произошла ошибка.Клиент не создан')
        return response

    def purchases_of_client(self, client_id: str = None, item_ids: str = None) -> ApitistResponse:
        """
        Информация о покупках клиента.
        :param item_ids: Айди товара
        :param client_id: Айди клиента
        :return: Ответ от сервера.
        """
        logger.info("Покупка товара по айди клиента")
        url = self.app_hostname + self.PURCHASE_BY_CLIENT_URL
        data = {
            "client_id": "string",
            "item_ids": [
                "string"
            ]
        }

        response = self.s.post(url=url, json=data)
        return response
