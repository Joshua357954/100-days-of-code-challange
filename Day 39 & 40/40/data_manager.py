import requests


class DataManager:

	sheety_endpoint="https://api.sheety.co/8b35da8ed66eeb5e24fa4b4c111ade84/flightFinder/flights"

	def prettify_date(self,date):
		new_date=date.split(" ")[0]

		day,month,year=new_date.split("-")[2],new_date.split("-")[1],new_date.split("-")[0]

		prettified=f"{day}/{month}/{year}"

		return prettified

	def prettify_time(self,time):
		
		new_time=time.split(":")[0].split("T")[0]

		return new_time

	def get_from_api(self,endpoint):

		api_data=requests.get(url=endpoint).json()

		return api_data

	def get_flight_data(self):

		flights=self.get_from_api(endpoint=self.sheety_endpoint)
		
		sheet_items=flights['flights']
		print(sheet_items)
		return sheet_items








	

