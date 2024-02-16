def test_put_booking(set_up, get_token):
    booking_id = 1

    assert set_up.put_update_booking(booking_id, get_token).status_code == 200
    response_body = set_up.put_update_booking(booking_id, get_token).json()
    assert response_body["firstname"] == "Odett"
    assert response_body["lastname"] == "Zorad"
