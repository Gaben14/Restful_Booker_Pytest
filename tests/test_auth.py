def test_auth(auth_client):
    # Assert
    assert auth_client.authentication().status_code == 200
