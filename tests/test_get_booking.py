def test_get_single_booking(set_up):
    single_booking = set_up.get_single_booking(2)

    # Assert
    assert single_booking.status_code == 200
    body = single_booking.json()
    print(body)
    assert body['firstname'] == 'Eric'
    assert body['lastname'] == 'Smith'


def test_get_booking_by_name(set_up):
    # Assert
    assert set_up.get_booking_by_name("Susan", "Wilson").status_code == 200
