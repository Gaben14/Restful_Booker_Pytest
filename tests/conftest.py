import pytest
from api import booking_api
from api import auth_api

base_url = 'http://localhost:3001'


# Moving the call initialization of the BookerClient to a fixture.
@pytest.fixture
def set_up():
    # Act
    # returning the BookerClient class
    return booking_api.BookerClient(base_url)


@pytest.fixture()
def get_token():
    # Act
    auth_client = auth_api.AuthClient(base_url)

    # returning the token from the AuthClient class
    token = auth_client.authentication().json()["token"]
    print(token)
    return token

# tear_down is not needed here at the moment, the libraries will close the session.
# but you can write it here - Homework read about scopes (set_up, tear_down)
