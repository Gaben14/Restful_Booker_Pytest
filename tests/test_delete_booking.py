def test_delete_booking(set_up, get_token):
    booking_id = 13

    assert set_up.delete_booking(booking_id, get_token).status_code == 201
    # Validate if the booking has been deleted by using the get_single_booking for the 404