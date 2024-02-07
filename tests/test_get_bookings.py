import requests


def test_get_single_booking(set_up):
    # Assert
    assert set_up.get_single_booking(2).status_code == 200
    body = set_up.get_single_booking(2).json()
    assert body['firstname'] == 'Eric'
    assert body['lastname'] == 'Smith'


def test_get_filter_by_name(set_up):
    # Assert
    assert set_up.get_booking_by_name("Susan", "Wilson").status_code == 200


    