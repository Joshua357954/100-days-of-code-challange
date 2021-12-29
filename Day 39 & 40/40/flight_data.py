import requests

class FlightData:
	def __init__(self):
		self.new_data=[]
		self.endpoint="https://api.sheety.co/8b35da8ed66eeb5e24fa4b4c111ade84/flightFinder/flights/"

	def get_codes(self,city):
		endpoint="https://tequila-api.kiwi.com/locations/query"
		header={"apikey":"ZwL2mYfOou3rFlJSSjAqa7ce8mLBkuC5"}
		param={"term":city,"location-types":"city"}

		response=requests.get(url=endpoint,headers=header,params=param)
		
		new_code=(response.json()["locations"][0]["code"])
		
		return new_code


	def update_flight_sheet(self):
		sheety_endpoint=self.endpoint
		for data in self.new_data:
			code=self.get_codes(data['destination'])
			new_record={
				"flight":{
					"iata":code
					}
				}

			update=requests.put(url=f"{sheety_endpoint}{data['id']}",json=new_record)
			print(update.json())

		







