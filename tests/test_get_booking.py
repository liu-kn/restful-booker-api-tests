from http.client import responses

import requests

# test1
# def test_get_booking_ids():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     print(response.json()[o:3])
#     assert response.status_code == 200


#test2
# def test_get_booking_ids():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     assert response.status_code == 200
#
#     bookings = response.json()
#     for booking in bookings:
#         assert "bookingid" in booking


def test_get_booking_by_id():
    response = requests.get("https://restful-booker.herokuapp.com/booking/2")
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
        assert key in booking