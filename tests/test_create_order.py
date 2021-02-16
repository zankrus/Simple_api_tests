"""Модуль с тестами по созданию заказа."""
import pytest
from jsonschema import validate

from json_schemas.create_order_schema import CREATE_ORDER_SCHEMA


class TestCreateOrder:

    @pytest.mark.parametrize(" address, phone, price, quantity", ['улица Колотушкина', '88005553535', '1', '1'])
    def test_positive_creat_order(self, api_client, created_client, address, phone, price, quantity):
        """
            Пример позитивного теста. С проверкой схемы ответа. Если есть подробная схема, можно сразу проверят типы
        данных в ответе и валидировать их.
        """
        client = api_client
        response = client.create_new_order(client_id=created_client, address=address, phone=phone, price=price,
                                           quantity=quantity)
        response.verify_response(200)
        validate(response.json(), schema=CREATE_ORDER_SCHEMA)

    @pytest.mark.parametrize(" address, phone, price, quantity", ['улица Колотушкина', '88005553535', '1', '1'])
    def test_negative_order_creating(self, api_client, created_client, address, phone, price, quantity):
        """
            Пример негативных тестов, ибо спецификаций нет и не знаю, какие поля обязательные.
            Можно кучу различных комбинаций указать, но зачем "упарываться" для тестового? :)
        """
        client = api_client
        response = client.create_new_order(client_id=created_client, address=address, phone=phone, price=price,
                                           quantity=quantity)
        response.verify_response(400)
