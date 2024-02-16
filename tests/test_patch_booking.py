def test_patch_booking(set_up, get_token):
    booking_id = 2

    assert set_up.patch_update_booking(booking_id, get_token).status_code == 200

    response_body = set_up.patch_update_booking(booking_id, get_token).json()
    assert response_body["firstname"] == "Alexandro"
    assert response_body["lastname"] == "Del Piero"
