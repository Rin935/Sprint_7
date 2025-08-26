import requests
import pytest
import allure
from data import Flags
from urls import Url

class TestOrderList:

    @allure.title('Тело ответа возвращается список заказов.')
    def test_successful_get_order_list(self):
        with allure.step('Подготовка URL для получения списка заказов'):
            full_url = f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}'
        with allure.step('Отправка GET запроса для получения списка заказов'):
            response = requests.get(full_url)
        with allure.step('Проверка успешного статус кода 200'):
            assert response.status_code == 200
        with allure.step('Проверка наличия списка заказов в ответе'):
            response_json = response.json()
            assert Flags.SUCCESSFUL_GET_ORDER_LIST in response_json