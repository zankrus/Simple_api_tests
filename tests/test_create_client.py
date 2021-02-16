"""Модуль с тестами по созданию клиента."""
import pytest
from jsonschema import validate

from json_schemas.create_client_schema import CREATE_CLIENT_SCHEMA


class TestCreateClient:

    """
    Пример позитивного теста. С проверкой схемы ответа. Если есть подробная схема, можно сразу проверят типы
    данных в ответе и валидировать их.
    """
    @pytest.mark.smoke
    @pytest.mark.parametrize("name, surname, phone", ['Ваня', 'Ванюшкин', ''])
    def test_positive_creat_client(self, api_client, name, surname, phone):
        client = api_client
        response = client.create_new_client(name=name, surname=surname, phone=phone)
        response.verify_response(200)
        validate(response.json(), schema=CREATE_CLIENT_SCHEMA)

    """
    Пример негативных тестов, ибо спецификаций нет и не знаю, какие поля обязательные.
    """
    @pytest.mark.parametrize("name, surname, phone", [
        ('', '', ''),
        (None, None, None)])
    def test_negative_client_creating(self, api_client, name, surname, phone):
        client = api_client
        response = client.create_new_client(name=name, surname=surname, phone=phone)
        response.verify_response(400)
