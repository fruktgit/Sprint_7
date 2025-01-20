import random
import string


class Orders:
    order_data = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Test Street, 1",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-01-12",
            "comment": "Test order",
            "color": ["BLACK"]
        }

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_courier_data():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

