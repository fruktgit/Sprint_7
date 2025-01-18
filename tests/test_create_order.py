import pytest
import allure
from config import API_ENDPOINTS
from utils.data_generator import Orders


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("создание заказа")
class TestCreateorders:
    @allure.suite("Создание заказа")
    @pytest.mark.parametrize(
        "colors",
        [
            (["BLACK"]),  # Один цвет — BLACK
            (["GREY"]),  # Один цвет — GREY
            (["BLACK", "GREY"]),  # Оба цвета
            ([]),  # Без указания цвета
        ],
    )
    def test_create_order_with_colors(self, setup_and_teardown, colors):
        allure.dynamic.title(f"Проверить создание заказа с цветами: {', '.join(colors) if colors else 'без цвета'}")

        order_data = Orders.order_data.copy()
        order_data["color"] = colors

        # Преобразуем в JSON для отправки
        data_order =  order_data

        response = self.client.post(API_ENDPOINTS["create_order"], data=data_order)
        assert response.status_code == 201, "Ожидался код ответа 201"
        assert "track" in response.json(), "Ответ должен содержать track"

