def test_post_booking(set_up):
    # Assert
    assert set_up.post_booking().status_code == 200
    response_body = set_up.post_booking().json()
    assert response_body["booking"]["firstname"] == "James"
    assert response_body["booking"]["lastname"] == "Brown"
    assert response_body["booking"]["totalprice"] == 111
    assert response_body["booking"]["depositpaid"] == True
