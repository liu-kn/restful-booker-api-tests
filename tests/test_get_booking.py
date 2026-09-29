from http.client import responses

import requests

# test1
# def test_get_booking_ids():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     print(response.json()[0:5])
#     assert response.status_code == 200


# def test_get_booking_id(api_base_url):
#     response = requests.get(api_base_url + "/booking")
#     print(response.json()[0:5])
#     assert response.status_code == 200


# #test2 СПИСОК БРОНИРОВАНИЙ
def test_get_booking_ids(api_base_url):
    response = requests.get(api_base_url + "/booking")
    assert response.status_code == 200

    bookings = response.json()
    for booking in bookings:
        assert "bookingid" in booking

#
# # test 3 ОДНО БРОНИРОВАНИЕ
def test_get_booking_by_id(api_base_url):
    response = requests.get(api_base_url + "/booking/2")
    assert response.status_code == 200

    booking = response.json()
    expected_keys = [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
    ]

    for key in expected_keys:
        assert key in booking       # assert что in где

