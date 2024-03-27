def test_post_booking(set_up):
    # Assert
    assert set_up.post_booking().status_code == 200
    # Refactor - call the booking object directly here, if later it's name is changed
    # You will only need to change it here.
    response_booking = set_up.post_booking().json()["booking"]
    # Refactor opportunity: Use the response from Get Booking
    # to check if the values are the same as we sent in the POST.
    err_msg = "Error! Incorrect value for "

    assert response_booking["firstname"] == "James", f"{err_msg} first name!"
    assert response_booking["lastname"] == "Brown", f"{err_msg} last name!"
    assert response_booking["totalprice"] == 111, f"{err_msg} total price!"
    assert response_booking["depositpaid"] == True, f"{err_msg} deposit paid!"
