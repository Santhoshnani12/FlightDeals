from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet_data = DataManager()
data = sheet_data.get_data()

flight = FlightData()
flight_iata = FlightSearch()

notification_manager = NotificationManager()

for i in range(len(data)):
    if data[i]['iataCode'] == '':
        code = flight_iata.get_iata_code(data[i]['city'])
        sheet_data.update_sheet(code, i+2)
    flight_info = flight.get_flight_cost(data[i]['iataCode'])
    if flight_info != None and flight_info.price <= data[i]['lowestPrice']:
        notification_manager.send_sms(
            message=f"Flight Details: \n"
                    f"From: {flight_info.origin_city} \n"
                    f"To: {flight_info.destination_city} \n"
                    f"Price: {flight_info.price} \n"
                    f"Date: {flight_info.out_date}"
        )