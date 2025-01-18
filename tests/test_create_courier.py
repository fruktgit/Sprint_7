import pytest
import allure
from utils.data_generator import generate_courier_data
from config import API_ENDPOINTS

@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Создание курьера")
class TestCreateCourier:
    @allure.suite("Создание курьера")
    @allure.title("Проверить, что курьера можно успешно создать и запрос возвращает правильный код ответа.")
    def test_create_courier_success(self, setup_and_teardown):
        response = self.client.post(API_ENDPOINTS["create_courier"], self.courier_data)
        assert response.status_code == 201

    @allure.title("Проверить, что при создании курьера возвращается правильный ответ ok: True.")
    def test_create_courier_correct_response_code(self, setup_and_teardown):
        response = self.client.post(API_ENDPOINTS["create_courier"], self.courier_data)
        assert response.json() == {"ok": True}

    @allure.title("Проверить, что попытка создать двух одинаковых курьеров приводит к ошибке.")
    def test_create_courier_duplicate(self, setup_and_teardown):
        # Первый запрос успешен
        self.client.post(API_ENDPOINTS["create_courier"], self.courier_data)
        # Второй запрос с дублирующими данными должен вернуть ошибку
        response = self.client.post(API_ENDPOINTS["create_courier"], self.courier_data)
        assert "Этот логин уже используется. Попробуйте другой." in response.json()["message"]

    @allure.title("Проверить, что создание курьера с отсутствующими полями возвращает ошибку.")
    @pytest.mark.parametrize("missing_field, expected_message", [
        ("login", "Недостаточно данных для создания учетной записи"),
        ("password", "Недостаточно данных для создания учетной записи")
    ])
    def test_create_courier_missing_fields(self, setup_and_teardown, missing_field, expected_message):
        """
        Проверяет, что при отсутствии обязательных полей запрос возвращает ошибку.
        """
        # Генерация данных курьера
        courier_data = generate_courier_data()
        del courier_data[missing_field]  # Удаляем указанное поле

        # Отправляем запрос
        response = self.client.post(API_ENDPOINTS["create_courier"], courier_data)

        # Проверки
        assert "message" in response.json(), "Ожидалось сообщение об ошибке"

    @allure.title("если создать пользователя с логином, который уже есть, меняем пароль, возвращается ошибка.")
    def test_create_courier_duplicate(self, setup_and_teardown):
        # Первый запрос успешен
        self.client.post(API_ENDPOINTS["create_courier"], self.courier_data)
        # Второй запрос с дублирующими данными должен вернуть ошибку
        duplicate_courier_data = self.courier_data.copy()
        duplicate_courier_data["password"] = "different_password"  # Изменяем пароль
        response = self.client.post(API_ENDPOINTS["create_courier"], duplicate_courier_data)
        assert "Этот логин уже используется. Попробуйте другой." in response.json()["message"]