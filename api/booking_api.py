import requests


class BookerClient:

    # Constructor
    def __init__(self, base_url='http://localhost:3001'):
        # base_url needs to be changed to a GitHub Secret variable later
        self.base_url = base_url

    def get_ping(self):
        response = requests.get(f'{self.base_url}/ping')

        print(response)
        return response

    def get_single_booking(self, booking_number):
        # Arrange - Follow this string format approach
        response = requests.get(f'{self.base_url}/booking/{booking_number}')
        return response

    def get_booking_by_name(self, lastname, firstname):
        # Arrange
        response = requests.get(f'{self.base_url}/booking?lastname={lastname}&firstname={firstname}')

        return response

    def get_booking_by_date(self, checkin_date, checkout_date):
        # Arrange
        response = requests.get(f'{self.base_url}/booking?checkin')

        return response