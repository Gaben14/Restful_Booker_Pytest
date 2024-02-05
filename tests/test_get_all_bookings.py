import requests
from api_requests import make_requests


def test_get_single_booking():
    # Act
    Get_Single_Booking = make_requests.BookerClient('http://localhost:3001')

    # Assert
    assert Get_Single_Booking.get_booking(2).status_code == 200
    