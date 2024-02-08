from api import auth_api


def test_auth():
    # Assert
    assert auth_api.AuthClient().auth_client().status_code == 200

    # TODO - Move the token to a fixture, so it can be used by the PUT, Patch, Delete tests later?
    token = auth_api.AuthClient().auth_client().json()["token"]
    print(token)
