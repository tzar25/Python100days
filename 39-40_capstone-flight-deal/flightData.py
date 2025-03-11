import requests


class FlightData:
    def __init__(self, client_id, client_secret):
        self.base_url = "https://test.api.amadeus.com"
        self.url_for_flights = "/v2/shopping/flight-offers"
        self.client_id = client_id
        self.client_secret = client_secret
        self._token = ""

    def _get_new_token(self):
        url_for_token = "/v1/security/oauth2/token"
        token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_body = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        if self._token == "":
            response = requests.post(url=self.base_url + url_for_token, headers=token_headers, data=token_body)
            # print(response.json())
            self._token = response.json()['access_token']
        return self._token

    def get_destination_code(self, city_name):
        url_for_iata = "/v1/reference-data/locations"
        self._get_new_token()
        params = {
            "subType": "AIRPORT",
            "keyword": city_name
        }
        headers = {"Authorization": f"Bearer {self._token}"}
        response = requests.get(url=self.base_url + url_for_iata, params=params, headers=headers)
        print(response.json())
        code = response.json()["data"][0]['iataCode']

        return code

    def get_flights(self, origin, destination, date):
        self._get_new_token()
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": date,
            "adults": 2,
            "max": 10,
            "currencyCode": "HUF"
        }
        headers = {"Authorization": f"Bearer {self._token}"}
        response = requests.get(url=self.base_url+self.url_for_flights, headers=headers, params=params)
        # print(self._token)
        # print(response.json())
        return response.json()
