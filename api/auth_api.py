import requests


class AuthClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def authentication(self):
        # Arrange
        user_name = "admin"
        password = "password123"
        url = f"{self.base_url}/auth"
        login_data = {"username": user_name, "password": password}

        # Act
        response = requests.post(url, login_data)
        return response
