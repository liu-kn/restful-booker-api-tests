# Напиши в нём фикстуру base_url,
# которая возвращает адрес без слэша в конце:
# "https://restful-booker.herokuapp.com".
import pytest


@pytest.fixture
def api_base_url():
    return "https://restful-booker.herokuapp.com"
