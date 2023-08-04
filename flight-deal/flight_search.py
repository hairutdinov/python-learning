import requests

TEQUILA_KIWI_API_ENDPOINT = "https://api.tequila.kiwi.com"
LOCATION_API_ENDPOINT = f"{TEQUILA_KIWI_API_ENDPOINT}/locations/query"
API_KEY = "oTyLxTPx8YLV-8zRqBtUYlV-ch06Z-y8"

tequila_kiwi_parameters = {
    "apikey": API_KEY
}

class FlightSearch:
    def find_airports(self, country):
        params = {
            "term": country,
            "location_types": "airport",
        }

        response = requests.get(LOCATION_API_ENDPOINT, headers=tequila_kiwi_parameters, params=params)
        return response.json()

    def get_country_code(self, country):
        airports = self.find_airports(country)
        print(airports)
        return None
        return airports[0].get("city").get("code")
