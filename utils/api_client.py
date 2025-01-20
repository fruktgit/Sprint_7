import requests
from config import BASE_URL

class APIClient:

    @staticmethod
    def post(endpoint, data=None):
        return requests.post(f"{BASE_URL}{endpoint}", json=data)

    @staticmethod
    def get(endpoint, params=None):
        return requests.get(f"{BASE_URL}{endpoint}", params=params)

    @staticmethod
    def delete(endpoint, data=None):
        return requests.delete(f"{BASE_URL}{endpoint}", json=data)

    @staticmethod
    def put(endpoint, data=None):
        return requests.put(f"{BASE_URL}{endpoint}", json=data)
