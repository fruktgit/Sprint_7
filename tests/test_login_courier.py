import pytest
import allure
from utils.data_generator import generate_courier_data
from config import API_ENDPOINTS

@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Логин курьера")
class TestLoginCourier:
    @allure.title("существующий курьер может авторизоваться")
    def test_login_courier_success(self, setup_and_teardown):
        self.client.post(API_ENDPOINTS["create_courier"], self.courier_data)
        response = self.client.post(API_ENDPOINTS["login_courier"], self.courier_data)
        assert response.status_code == 200

    @allure.title("не существующий курьер не может авторизоваться")
    def test_login_incorrect_credentials(self, setup_and_teardown):

        response = self.client.post(API_ENDPOINTS["login_courier"], self.courier_data)
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

    @allure.title("Проверить, что при отсутствии обязательных полей возвращается ошибка при авторизации.")
    @pytest.mark.parametrize("missing_field, expected_message", [
        ("login", "Недостаточно данных для входа"),
        ("password", "Недостаточно данных для входа")
    ])
    def test_login_missing_fields(self, setup_and_teardown, missing_field, expected_message):
        """
        Проверяет, что при отсутствии обязательных полей запрос возвращает ошибку.
        """
        # Генерация данных курьера
        courier_data = generate_courier_data()
        self.client.post(API_ENDPOINTS["create_courier"], self.courier_data)
        del courier_data[missing_field]  # Удаляем указанное поле

        # Отправляем запрос
        response = self.client.post(API_ENDPOINTS["login_courier"], courier_data)

        # Проверки
        assert expected_message in response.text, "Ожидалось сообщение об ошибке"

    @allure.title("успешный запрос возвращает id.")
    def test_login_success_response_id(self, setup_and_teardown):
        self.client.post(API_ENDPOINTS["create_courier"], self.courier_data)
        response = self.client.post(API_ENDPOINTS["login_courier"], self.courier_data)
        assert response.status_code == 200 and 'id' in response.text

