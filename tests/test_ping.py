import requests

#
# def test_ping():
#     response = requests.get("https://restful-booker.herokuapp.com/ping")
#     assert response.status_code == 201


def test_ping(api_base_url):
    response = requests.get(api_base_url + "/ping")
    assert response.status_code == 201
