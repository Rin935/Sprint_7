import requests
import pytest
import allure
from data import Url, Flags, DataForOrder


class TestCreationOrder:

    @allure.title('Успешное создание заказа со всеми цветовыми вариациями.')
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_color)
    def test_create_order_with_different_color(self, scooter_color):
        order_data = DataForOrder.order_data
        order_data['color'] = scooter_color
        order = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
        assert order.status_code == 201 and Flags.SUCCESSFUL_ORDER_CREATION in order.json()
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{order.json()['track']}')