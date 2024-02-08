import requests


class AuthClient:

    def __init__(self):
        self.base_url = 'http://localhost:3001'
        self.username = "admin"
        self.password = "password123"

    # TODO - Is this okay like this, or should I move it to a fixture?
    def auth_client(self):
        # Arrange
        url = f"{self.base_url}/auth"
        login_data = {"username": self.username, "password": self.password}

        # Act
        response = requests.post(url, login_data)

        return response
