import pytest
import allure
from config import API_ENDPOINTS
from utils.data_generator import Orders


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("создание заказа")
class TestCreateOrders:
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

        # Копируем данные заказа и добавляем цвета
        order_data = Orders.order_data.copy()
        order_data["color"] = colors

        # Преобразуем в JSON для отправки
        data_order = order_data

        # Отправляем запрос на создание заказа
        response = self.client.post(API_ENDPOINTS["create_order"], data=data_order)

        # Если заказ создан успешно, отменяем его
        if response.status_code == 201:
            track_id = response.json().get("track")
            cancel_response = self.client.put(f'{API_ENDPOINTS["create_order"]}/cancel', data={"track": track_id})

         # Проверяем, что заказ был успешно создан
        assert response.status_code == 201, "Ожидался код ответа 201"
        assert "track" in response.json(), "Ответ должен содержать track"
    def test_cancel_order(self, setup_and_teardown, colors=["BLACK"]):
        allure.title("Проверяем удаление заказа")

        # Копируем данные заказа и добавляем цвета
        order_data = Orders.order_data.copy()
        order_data["color"] = colors

        # Преобразуем в JSON для отправки
        data_order = order_data

        # Отправляем запрос на создание заказа
        response = self.client.post(API_ENDPOINTS["create_order"], data=data_order)

        # Если заказ создан успешно, отменяем его
     
        track_id = response.json().get("track")
        cancel_response = self.client.put(f'{API_ENDPOINTS["create_order"]}/cancel', data={"track": track_id})

         # Проверяем, что заказ был успешно удален
        assert cancel_response.status_code == 200, "Ожидался код ответа 200"

