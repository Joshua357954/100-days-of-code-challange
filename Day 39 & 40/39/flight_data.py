import requests


class FlightData:

	def __init__(self):
		self.new_data=[]


	def get_flight_code(self,city_name):
		location_endpoint="https://tequila-api.kiwi.com/locations/query"
		header={"apikey":"ZwL2mYfOou3rFlJSSjAqa7ce8mLBkuC5"}
		l_params={"term":city_name,"location-types":"city"}

		res=requests.get(url=location_endpoint,headers=header,params=l_params)
		output=(res.json()["locations"][0]["code"])

		return output


	def update_flight_data(self):
		sheety_endpoint="https://api.sheety.co/9c9131b74e93a891e24c213fc26b7da4/flightFinder/flights/"
		
		for data in self.new_data:
			new_code=self.get_flight_code(data["destination"])
			
			put_data={
			"flight":{
				"iata":new_code}
			}


			sheet_update=requests.put(url=f"{sheety_endpoint}{data['id']}",json=put_data)
			print(sheet_update.json())



