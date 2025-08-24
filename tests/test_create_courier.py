import requests
import pytest
import allure
from data import ResponseBody, Url, DataForRegistration


class TestsCreateNewCourier:

    @allure.title('Успешное создание курьера.')
    def test_creation_courier_success(self, generate_courier_data):
        registration = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=generate_courier_data)
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Невозможность создания двух одинаковых курьеров.')
    def test_creation_courier_clone_error(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier)
        assert response.status_code == 409 and (response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST)

    @allure.title('Если одного из полей(логин и пароль) нет, запрос возвращает ошибку.')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_failure_data_error(self, data_setup):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', data_setup)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA)