# Напиши в нём фикстуру base_url,
# которая возвращает адрес без слэша в конце:
# "https://restful-booker.herokuapp.com".
import pytest
import requests


@pytest.fixture
def api_base_url():
    return "https://restful-booker.herokuapp.com"


@pytest.fixture
def auth_token(api_base_url):
    credentials = {"username": "admin", "password": "password123"}
    response = requests.post(api_base_url + "/auth", json=credentials)
    return response.json()["token"]
