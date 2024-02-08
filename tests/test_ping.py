def test_get_ping(set_up):

    # Assert
    assert set_up.get_ping().status_code == 201
