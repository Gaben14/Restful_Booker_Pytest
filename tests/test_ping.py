from api import api_request


def test_get_ping():
    # Act
    BookerClient = api_request.BookerClient()

    # Assert
    assert BookerClient.get_ping().status_code == 201
