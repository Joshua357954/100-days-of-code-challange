import requests
from datetime import datetime

class DataManager:


	def get_sheet_items(self):
		sheet_endpoint="https://api.sheety.co/9c9131b74e93a891e24c213fc26b7da4/flightFinder/flights"
		response=requests.get(url=sheet_endpoint)
		all_sheet_items=response.json()['flights']

		return all_sheet_items

	def prettify_date(self,date):
		now=(datetime.now())

		year,month,day=(str(date).split(" ")[0].split("-")[0], str(date).split(" ")[0].split("-")[1],str(date).split(" ")[0].split("-")[2])

		pretty_date=(f"{day}/{month}/{year}")

	def prettify_time(self,time):
		
		new_time=time.split(":")[0].split("T")[0]

		return str(new_time)


		return pretty_date
