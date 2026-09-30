# Restful-Booker API Tests

Automated API tests for [Restful-Booker](https://restful-booker.herokuapp.com)
written in Python with pytest and requests.

## Tech stack
- Python 3.11
- pytest
- requests

## How to run
pip install -r requirements.txt
pytest -v





## Known API bugs

- `POST /booking` with an empty body returns `500 Internal Server Error` instead of `400 Bad Request`.
  Covered by `test_create_booking_empty_body` (marked as `xfail`).