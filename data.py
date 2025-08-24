import generators


class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    CREATE_COURIER = '/api/v1/courier'
    COURIER_LOGIN = '/api/v1/courier/login'
    COURIER_DELETE = '/api/v1/courier/:id'
    CREATE_ORDER = '/api/v1/orders'
    GET_ORDER_LIST = '/api/v1/orders'
    ORDER_CANCEL = '/api/v1/orders/cancel'
    TRACK_ORDER = '/api/v1/orders?track?t='


class DataForOrder:
    order_data = {
        "firstName": "РРІР°РЅ",
        "lastName": "РРІР°РЅРѕРІ",
        "address": "Р РѕР¶РґРµСЃС‚РІРµРЅРєР° 5",
        "metroStation": 2,
        "phone": "89879998888",
        "rentTime": 3,
        "deliveryDate": "2025-07-19",
        "comment": "РЎРїР°СЃРёР±Рѕ"
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



