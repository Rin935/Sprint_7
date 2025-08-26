import pytest
import requests
import generators
from urls import Url
from data import Flags, DataForOrder

@pytest.fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier_body)
    login_courier = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body)
    yield [create_courier_body, login_courier_body, login, password]



@pytest.fixture
def generate_courier_data():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    creation_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    yield [creation_courier_body, login_courier_body]
    login_courier = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body)

@pytest.fixture
def order_data():
        return DataForOrder.order_data.copy()

@pytest.fixture(params=DataForOrder.scooter_color)
def scooter_color(request):
        return request.param

@pytest.fixture
def create_order(order_data, scooter_color):
    order_data_copy = order_data.copy()
    order_data_copy['color'] = scooter_color

    order_response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data_copy)

    assert order_response.status_code == 201, f"Ошибка создания заказа: {order_response.text}"
    assert Flags.SUCCESSFUL_ORDER_CREATION in order_response.json(), "Не найден флаг успешного создания"

    return order_response.json()

@pytest.fixture
def create_and_cancel_order(create_order):
    order_track = create_order['track']

    yield order_track

    try:
        cancel_response = requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{order_track}')
        if cancel_response.status_code == 200:
            print(f"✓ Заказ {order_track} успешно отменен")
        else:
            print(f"⚠ Ошибка отмены заказа {order_track}: {cancel_response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Ошибка сети при отмене заказа {order_track}: {e}")
    except Exception as e:
        print(f"✗ Неожиданная ошибка при отмене заказа {order_track}: {e}")

@pytest.fixture
def order_track(create_order):
    return create_order['track']




