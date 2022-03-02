import requests
from datetime import datetime, timedelta
from flight_search import HEADER
from flight_info import FlightInfo

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.fly_from = "LHR"
        self.today = datetime.now()
        self.current_date = self.today + timedelta(days=1)
        self.current_date = self.current_date.strftime("%d/%m/%Y")
        self.next_date = datetime.now() + timedelta(days=5)
        self.final_date = self.next_date.strftime("%d/%m/%Y")
        self.min_return_date = self.next_date + timedelta(days=12)
        self.min_return_date = self.min_return_date.strftime("%d/%m/%Y")
        self.max_return_date = self.next_date + timedelta(days=35)
        self.max_return_date = self.max_return_date.strftime("%d/%m/%Y")

    def get_flight_cost(self, sheet_city):
        parameters = {
            "fly_from": self.fly_from,
            "fly_to": sheet_city,
            "date_from": self.current_date,
            "date_to": self.final_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=parameters, headers=HEADER)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {sheet_city}.")
            return None

        flight_info = FlightInfo(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_info.destination_city}: £{flight_info.price}")
        return flight_info
