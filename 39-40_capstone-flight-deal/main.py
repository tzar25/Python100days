from os import getenv
from dotenv import load_dotenv
from datetime import date, timedelta
import time

from sheetReader import SheetReader
from flightData import FlightData

load_dotenv(override=True)

ORIGIN_LOCATION = "BUD"

SHEETY_AUTH = getenv("SHEETY_AUTH")
AMADEUS_API_KEY = getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = getenv("AMADEUS_API_SECRET")

DATES = [(date.today()+timedelta(30+i)).strftime("%Y-%m-%d") for i in range(7)]

sheet = SheetReader(SHEETY_AUTH)

flight_data = FlightData(AMADEUS_API_KEY, AMADEUS_API_SECRET)


sheet_data = sheet.get_data()
# print(sheet_data)

# get IATA codes if the first is empty
try:
    if sheet_data[0]['code'] == '':
        for row in sheet_data:
            row['code'] = flight_data.get_destination_code(row['destination'])
            time.sleep(1)
        sheet.destination_data = sheet_data
        sheet.update_destination_codes()
except KeyError:
    for row in sheet_data:
        row['code'] = flight_data.get_destination_code(row['destination'])
        time.sleep(1)
    sheet.destination_data = sheet_data
    sheet.update_destination_codes()

# Look for better prices
for destination in sheet_data:
    found_better = False
    try:
        min_price = float(destination['price'])
    except KeyError:
        min_price = 99999999
    for date in DATES:
        flights = flight_data.get_flights(ORIGIN_LOCATION, destination['code'], date)['data']
        for flight in flights:
            if float(flight['price']['total']) < min_price:
                min_price = float(flight['price']['total'])
                print(f"Found lower price for {ORIGIN_LOCATION}-{destination['code']}:\nPrice: HUF{min_price}\nDate: {date}.")
                found_better = True
                min_date = date
        time.sleep(1)
    if found_better:
        sheet.update_price(destination['code'], min_price, min_date)
