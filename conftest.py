"""Тут хранятся фикстуры."""
import random

import pytest
import Faker

from api.client import APIClient

fake_data = Faker('RU-ru')


@pytest.fixture(scope='function')
def api_client(request):
    client = APIClient(app_hostname=request.config.getoption("--hostname"))
    return client


@pytest.fixture(scope='session')
def created_client(api_client):
    client = api_client
    response = client.create_new_client(name=fake_data.name(), surname=fake_data.surname(), phone=fake_data.phone())
    return response.json().get("client_id", '')


@pytest.fixture(scope='session')
def created_order(api_client, created_client):
    client = api_client
    address = fake_data.adress()
    phone = fake_data.phone()
    price = fake_data.int()
    quantity = fake_data.int()
    item_id = random.choice('ТУТ СПИСОК ВОЗМОЖНЫХ АЙДИШНИКОВ')
    response = client.create_new_order(client_id=created_client, address=address, phone=phone, price=price,
                                       quantity=quantity,item_id=item_id)
    return {
        'client_id' :client,
        'address': address,
        'phone' : phone,
        'pice' :price,
        'quantity' : quantity,
        'item_id' : item_id,
        'order_id': response.json().get('order_id'),
        'order_number' :response.json().get('order_number')}


def pytest_addoption(parser):
    parser.addoption(
        "--hostname",
        action="store",
        default="https://some-url.ru",
        help="enter url",
    )
