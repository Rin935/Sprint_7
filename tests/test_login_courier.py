import requests
import allure
import generators
from data import ResponseBody, Url


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера при заполнении всех обязательных полей.')
    def test_successful_courier_login(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=create_courier)
        courier_id = response.json()
        assert response.status_code == 200 and courier_id != ''

    @allure.title('Ошибка авторизации курьера с пустым полем "Пароль".')
    def test_courier_login_empty_password_error(self, create_courier):
        data_response = {'login': create_courier[2], 'password': ''}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA)

    @allure.title('Ошибка авторизации курьера с пустым полем "Логин".')
    def test_courier_login_empty_login_error(self, create_courier):
        data_response = {'login': '', 'password': create_courier[3]}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA)

