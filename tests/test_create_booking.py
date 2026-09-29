import requests


### POST
def test_create_booking(api_base_url):
    new_booking = {
        "firstname": "Liubov",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-05"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(api_base_url + "/booking", json=new_booking)
    print(response.json())
    assert response.status_code == 200

    created = response.json()
    assert "bookingid" in created
    assert created["booking"] == new_booking

    booking_id = created["bookingid"]
    response = requests.get(api_base_url + "/booking/" +  str(booking_id))
    assert response.status_code == 200
    assert response.json() == new_booking