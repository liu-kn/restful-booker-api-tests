import requests


def test_ping():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    assert response.status_code == 201
