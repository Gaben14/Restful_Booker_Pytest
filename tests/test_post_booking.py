import pytest


def test_post_booking(set_up):
    # Assert
    assert set_up.post_booking().status_code == 200
    response_body = set_up.post_booking().json()
    assert response_body["firstname"] == "James"

