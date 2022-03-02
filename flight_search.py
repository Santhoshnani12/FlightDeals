import requests

KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

HEADER = {
    "apikey": "V3oakUSbN6-TSWtVnUR20Pt3cI1rF5mD"
}

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city):
        params = {
            "term": city
        }

        response = requests.get(url=KIWI_ENDPOINT, headers=HEADER, params=params)
        response.raise_for_status()
        return response.json()['locations'][0]['code']
