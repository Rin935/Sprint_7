import requests
import pytest
import allure
from data import ResponseBody, DataForRegistration
from urls import Url


class TestsCreateNewCourier:

    @allure.title('Успешное создание курьера.')
    def test_creation_courier_success(self, generate_courier_data):
        with allure.step('Подготовка данных курьера для регистрации'):
            courier_data = generate_courier_data
        with allure.step('Отправка POST запроса на {Url.CREATE_COURIER}'):
            registration = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=courier_data)
        with allure.step('Проверка ответа от сервера'):
            assert registration.status_code == 201
            assert registration.json() == ResponseBody.COURIER_CREATION_SUCCESS


    @allure.title ('Невозможность создания двух одинаковых курьеров.')
    def test_creation_courier_clone_error(self, create_courier):
        with allure.step('Получение данных уже созданного курьера'):
            courier_data = {
                "login": create_courier["login"],
                "password": create_courier["password"],
                "firstName": create_courier["firstName"],
            }
        with allure.step('Отправка POST запроса на создание такого же курьера'):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=courier_data)
        with allure.step('Проверка ошибки конфликта'):
            assert response.status_code == 409
        with allure.step('Проверка тела ответа с сообщением об ошибке'):
            assert response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST

    @allure.title('Если одного из полей(логин и пароль) нет, запрос возвращает ошибку.')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_failure_data_error(self, data_setup):
        with allure.step('Подготовка данных для регистрации с недостающими полями'):
            missing_fields = []
            if 'login' not in data_setup:
                missing_fields.append('логин')
            if 'password' not in data_setup:
                missing_fields.append('пароль')
            if 'firstName' not in data_setup:
                missing_fields.append('имя')
        with allure.step(f'Отправка POST запроса на {Url.CREATE_COURIER}'):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=data_setup)
        with allure.step('Проверка статус кода ошибки 400'):
            assert response.status_code == 400
        with allure.step('Проверка тела ответа с сообщением об ошибке'):
            assert response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA