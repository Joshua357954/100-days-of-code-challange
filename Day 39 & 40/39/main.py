import requests
from datetime import datetime ,timedelta
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notify import MakeNotification
from pprint import pprint

MAIN_ENDPOINT="https://tequila-api.kiwi.com"
CURRENT_LOCATION={"Nigeria":"NG"}

flight_data=FlightData()
flight_search=FlightSearch()
data_mgr=DataManager()
notifcation=MakeNotification()

# This is to update the flight database or sheet
flight_data.new_data=data_mgr.get_sheet_items()

# Needs_update=False
# for dats in flight_data.new_data:
# 	if dats[0]['iata']=="":
# 		Needs_update=True

# if Needs_update:
# 	flight_data.update_flight_data()

currency_symbols={"EUR":"€","NGN":"₦","ZAR":"R","BDT":"৳","CNY":"¥ /元","INR":"₹","SGD":"$","CAD":"$","USD":"$","BRL":"R$"
}


# make the search part 
# learn how to get date upfront 
# qurey the api with the informatin

now=datetime.now()

tomorrow=data_mgr.prettify_date(now+timedelta(days=1))

next_six_month=data_mgr.prettify_date(now+timedelta(days=60*3))




# Search For Flights Available
for data in flight_data.new_data:

	data_to_send=flight_search.get_destination(From=CURRENT_LOCATION["Nigeria"],To=data["iata"],Date1=tomorrow,Date2=next_six_month)
	try: 
		new_result=data_to_send["data"][0]
	except Exception as e:
		print(e,"No available flight ....")
	else:

		currency=data_to_send["currency"]

		symbol=currency_symbols[currency]

		city_from=(new_result['cityFrom'],new_result['cityCodeFrom'])

		city_to=(new_result['cityTo'],new_result['cityCodeTo'])

		date_from=data_mgr.prettify_time(new_result["local_arrival"])

		date_to=data_mgr.prettify_time(new_result["local_departure"])

		price=new_result['price']

		print(str(price))

		if price < data['price']:
			#send_message
			print(data['price'] ,'yes')
			new_message=f"Low Price Alert ⚠️ . \nOnly {symbol}{price} to ✈️ from {[item for item in CURRENT_LOCATION][0]}-{city_from[1]}\
						 TO {city_to[0]}{city_to[1]} ,\n Form {str(date_from)} TO {str(date_to)}"

			msg=notifcation.send_message(new_message)

			print(msg)









