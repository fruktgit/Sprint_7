import pytest
import allure
from config import API_ENDPOINTS


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("получение списка заказов")
class TestCreateorders:

    def test_get_order_list(self, setup_and_teardown):

        response = self.client.get(API_ENDPOINTS["create_order"])
        assert response.status_code == 200, "Ожидался код ответа 201"
