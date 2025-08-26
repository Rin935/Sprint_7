import generators

class DataForOrder:
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Театральный проезд, 5",
        "metroStation": 2,
        "phone": "89879998888",
        "rentTime": 3,
        "deliveryDate": "2025-07-19",
        "comment": "Позвоните перед доставкой"
    }

    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]


class DataForRegistration:
    reg_data = [
        {'login': generators.login_generator(), 'password': generators.password_generator()},
        {'login': generators.login_generator(), 'firstName': generators.name_generator()},
        {'password': generators.password_generator(), 'firstName': generators.name_generator()}
    ]


class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message': "Этот логин уже используется"}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code': 400, 'message':  "Недостаточно данных для создания учетной записи"}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': "Учетная запись не найдена"}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400, 'message':  "Недостаточно данных для входа"}


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'



