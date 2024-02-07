import pytest
from api import booking_api


# Moving the call initialization of the BookerClient to a fixture.
@pytest.fixture
def set_up():
    # Act
    BookerClient = booking_api.BookerClient()

    return BookerClient
