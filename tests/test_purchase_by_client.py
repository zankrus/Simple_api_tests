"""Модуль с тестами по списку покупок."""
import pytest
from jsonschema import validate

from json_schemas.purchase_by_client_schema import PURCHASE_BY_CLIENT_SCHEMA


class TestPurchases:

    @pytest.mark.parametrize(" address, phone, price, quantity", ['улица Колотушкина', '88005553535', '1', '1'])
    def test_positive_purchases(self, api_client, created_order):
        """
            Пример позитивного теста. С проверкой схемы ответа. Если есть подробная схема, можно сразу проверят типы
        данных в ответе и валидировать их.
        """
        client = api_client
        response = client.purchases_of_client(client_id=created_order.get('client_id'),
                                              item_ids=created_order.get('item_id'))
        response.verify_response(200)
        validate(response.json(), schema=PURCHASE_BY_CLIENT_SCHEMA)
        items_from_response = response.json().get('items')[0]
        assert items_from_response['item_id'] == created_order['item_id']
        assert items_from_response['purchased'] is True
        assert items_from_response['last_order_number'] == created_order['order_number']
        assert items_from_response['last_purchase_date'] == 'Тут надо из БД дергать время покупки'
        assert items_from_response['purchase_count'] == created_order['quantity']

    @pytest.mark.parametrize("client_id, item_id", ['1', '1'])
    def test_negative_purchases_client_not_exists(self, api_client, client_id, item_id):
        """
            Тут негативных сценариев очень много - напишу без параметризации
        """
        client = api_client
        response = client.purchases_of_client(client_id=client_id,
                                              item_ids=item_id)
        response.verify_response(404)
