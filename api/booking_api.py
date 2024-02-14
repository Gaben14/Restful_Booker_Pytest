import requests


class BookerClient:

    # Constructor
    def __init__(self, base_url):
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
        # /booking?checkin=2014-03-13&checkout=2014-05-21
        response = requests.get(f'{self.base_url}/booking?checkin={checkin_date}&checkout={checkout_date}')

        return response

    # Refactor the class constructor to include these values?
    def post_booking(self):
        # Arrange
        url = f'{self.base_url}/booking'
        booking_data = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        # Act
        response = requests.post(url, json=booking_data)
        """We need to specify that the booking_data is the JSON that we are sending,
        otherwise the requests library will try to use it as the data= parameter, 
        data= is used for forms or form submissions
        
        The key here is naming parameters that post uses the following:
        post(url, data=None, json=None, **kwargs)
        Ctrl + Left Click / the Middle/scroller  on the post function will open the
        detailed description  
        """
        return response

    def put_update_booking(self, booking_id, token):
        # Arrange
        url = f'{self.base_url}/booking/{booking_id}'
        """
        For the Header we need to create a dictionary, and assign it to the 
        headers= as seen below. Token is coming from the get_token fixture.
        """
        head = {"Cookie": f"token={token}"}
        """
        for the PUT command all the values (keys) must be included, 
        otherwise you will get an error 
        """
        booking_data = {
                "firstname": "Gabor",
                "lastname": "Zorad",
                "totalprice": 111,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2019-01-01",
                    "checkout": "2020-01-01"
                },
                "additionalneeds": "Breakfast"
        }

        # Act
        response = requests.put(url, headers=head, json=booking_data)
        return response
