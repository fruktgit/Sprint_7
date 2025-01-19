
BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'

API_ENDPOINTS = {
    "create_courier": "/courier",
    "login_courier": "/courier/login",
    "create_order": "/orders"
}
class Api_messages:
    account_name_already_exists = "Учетная запись с таким именем уже существует"
    missing_required_registration_fields = "Этот логин уже используется. Попробуйте другой."
    missing_required_login_fields = "Недостаточно данных для входа"
    account_not_found = "Учетная запись не найдена"
    missing_fields = "Недостаточно данных для создания учетной записи"
    right_answer = {"ok": True}
