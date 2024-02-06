import requests
from api import api_request


def test_get_single_booking():
    # Act
    Get_Single_Booking = api_request.BookerClient()

    # Assert
    assert Get_Single_Booking.get_single_booking(2).status_code == 200
    body = Get_Single_Booking.get_single_booking(2).json()
    assert body['firstname'] == 'Jim'
    assert body['lastname'] == 'Wilson'

    