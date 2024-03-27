def test_get_single_booking(set_up):
    single_booking = set_up.get_single_booking(2)

    # Assert
    assert single_booking.status_code == 200
    body = single_booking.json()
    print(body)

    err_msg = "Error! Incorrect value for "
    assert body['firstname'] == 'Eric', f"{err_msg} first name!"
    assert body['lastname'] == 'Smith', f"{err_msg} last name!"


def test_get_booking_by_name(set_up):
    # Assert
    assert set_up.get_booking_by_name("Susan", "Wilson").status_code == 200
