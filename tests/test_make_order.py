import requests
import pytest
import allure
from data import Flags, DataForOrder
from urls import Url



class TestCreationOrder:

    @allure.title('Успешное создание заказа со всеми цветовыми вариациями.')
    def test_create_order_with_different_color(self, create_and_cancel_order):
        with allure.step('Создание заказа с разными цветами'):
            order_track = create_and_cancel_order
        with allure.step('Проверка, что заказ создан успешно'):
            assert order_track is not None
            assert isinstance(order_track, int)