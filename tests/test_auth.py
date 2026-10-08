import requests


def test_create_token(api_base_url):
    credentials = {"username": "admin", "password": "password123"}
    response = requests.post(api_base_url + "/auth", json=credentials)
    assert response.status_code == 200
    assert "token" in response.json()
