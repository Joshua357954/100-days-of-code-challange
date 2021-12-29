import requests

# make the flight_data model then send it to the main .py 
# Flight search role 1: get iata code from the location api with 
# Flight search role 2: is to update flight data with the iata code

# make the data_manager which contains the data gotten from the sheety flight api
# Data manager role 1: get all the flight from the flight data
# Data manager role 2: get all the users from the flight api

# make the flight_search_model which search the api and returns relevant data to the user
# flight_search role 1: make flight search to the kiwi api


# main.py is to merge all the data and make it one master piece
# main.py role : if flight search iata code is missing, updating the flight search sheet 
# main.py role 2 : if the return data from the flight search model is lower than the 
# normal price specified in the flight sheet, the send message to all the users 
# in the user sheet and send them alert ,with already crafted from message from flight search model


# make a notification model to send emails to all the users in user sheet
# notification role 1: send message
# notification role 2 : unescape emoji
from datetime import datetime
from datetime import timedelta
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from users import Users

flight_data=FlightData()
data_mgr=DataManager()
flight_search=FlightSearch()
users=Users()

# Defaults variables
NOW=datetime.now()
NEXT_DAY=data_mgr.prettify_date(date=str(NOW+timedelta(days=1)))
NEXT_60_DAYS=data_mgr.prettify_date(date=str(NOW+timedelta(days=60)))
CURRENT_LOCATION={"country":"Nigeria","iata":"NG"}

# Fake User Inputs


DATE_1=NEXT_DAY
DATE_2=NEXT_60_DAYS
FROM=CURRENT_LOCATION['iata']
TO='IST'

#----------------------------

# Write a program
flight_data.new_data=data_mgr.get_flight_data()

def needs_update():
	for each_data in flight_data.new_data:
		if each_data['iata']=='':
			return True
needs_update()

if needs_update() :
	flight_data.update_flight_sheet()

# make the flight search with the available data from the user


for data in flight_data.new_data:

	flight_search_result=flight_search.get_available_flights(From=CURRENT_LOCATION['iata'],To=data['iata'],Date1=DATE_1,Date2=DATE_2)

	new_data=(flight_search_result['data'][0])

	city_from=(new_data['cityFrom'],new_data['cityCodeFrom'])

	city_to=(new_data['cityTo'],new_data['cityCodeTo'])

	date_from=data_mgr.prettify_time(str(new_data["local_departure"]))

	date_to=data_mgr.prettify_time(str(new_data["local_arrival"]))
	
	currency=flight_search_result['currency']

	price=new_data['price']
	

	if price < data['price']:

		print(f"We have a cheap flight to {data['destination']}")

		# https://www.google.co.uk/flights?hl=en#flt={city_to[1]}.{city_from[1]}.{date_from}*{city_from[1]}.{city_to[1]}.{date_to}

		flight_url=f"https://www.google.co.uk/flights?hl=en#flt={city_to[1]}.{city_from[1]}.{date_from}*{city_from[1]}.{city_to[1]}.{date_to}"
		message=f"Low Price Alert : \nTo Fly From {city_from[0]} to {city_to[0]} for only ${price}\nFrom {date_from} to {date_to} \n{flight_url}"
		
		# post all data to the user sheet
		# get all the user data and  send them the derived message ...
		# message to send
		print(message)

		# users.send_all_notification(message)
