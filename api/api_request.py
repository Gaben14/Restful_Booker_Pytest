import requests


class BookerClient:

    # Constructor
    def __init__(self, base_url='http://localhost:3001'):
        # base_url needs to be changed to a GitHub Secret variable later
        self.base_url = base_url

    def get_ping(self):
        response = requests.get(self.base_url + "/ping")

        print(response)
        return response

    def get_single_booking(self, booking_number):
        # Arrange
        response = requests.get(self.base_url + '/booking/' + f"{booking_number}")
        return response


