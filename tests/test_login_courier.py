import requests
import allure
from data import ResponseBody
from urls import Url


class TestLoginCourier:


    @allure.title('Успешная авторизация курьера при заполнении всех обязательных полей.')
    def test_successful_courier_login(self, create_courier):
        with allure.step('Подготовка учетных данных для авторизации'):
            login_data = {
                "login": create_courier["login"],
                "password": create_courier["password"]
            }
        with allure.step(f'Отправка POST запроса на {Url.COURIER_LOGIN}'):
            response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_data)
        with allure.step('Проверка успешного статус кода 200'):
            assert response.status_code == 200
        with allure.step('Проверка наличия ID курьера в ответе'):
            courier_id = response.json().get('id')
            assert courier_id is not None
            assert courier_id != ''


    @allure.title('Ошибка авторизации курьера с пустым полем "Пароль".')
    def test_courier_login_empty_password_error(self, create_courier):
        with allure.step('Подготовка данных с пустым паролем'):
            data_response = {
                'login': create_courier[2],
                'password': ''
            }
        with allure.step(f'Отправка POST запроса на {Url.COURIER_LOGIN}'):
            response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        with allure.step('Проверка статус кода ошибки 400'):
            assert response.status_code == 400
        with allure.step('Проверка тела ответа с сообщением об ошибке'):
            assert response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA

    @allure.title('Ошибка авторизации курьера с пустым полем "Логин".')
    def test_courier_login_empty_login_error(self, create_courier):
        with allure.step('Подготовка данных запроса с пустым логином'):
            data_response = {'login': '', 'password': create_courier[3]}
        with allure.step('Отправка POST-запрос на вход курьера'):
            response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        with allure.step('Проверка статуса ответа и тела ответа'):
            assert response.status_code == 400
            response_json = response.json()
            assert response_json == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA

