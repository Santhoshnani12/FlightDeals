import requests

USERNAME = "santhosh"
PASSWORD = "testingtesting"

SHEETY_USERNAME = "c67bbbfde9be50800194ed630cecdf86"
PROJECT_NAME = "flightDeals"
SHEET_NAME = "prices"

AUTHENTICATION = (USERNAME, PASSWORD)

SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"


class DataManager:
    # This class is responsible for talking to the Google Sheet
    def get_data(self):
        get_response = requests.get(url=SHEETY_ENDPOINT, auth=AUTHENTICATION)
        return get_response.json()['prices']

    def update_sheet(self, code, i):
        sheety_params = {
            "price": {
                "iataCode": code,
            }
        }

        put_response = requests.put(url=SHEETY_ENDPOINT + f"/{i}", auth=AUTHENTICATION, json=sheety_params)
        print(put_response.status_code)
