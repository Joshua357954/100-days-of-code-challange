import requests

FLIGHT_URL=""




class FlightSearch:



	def get_destination(self,From,To,Date1,Date2):
		tequila_endpoint="https://tequila-api.kiwi.com/v2/search"
		search_key="3-kRbw9VSRq96JUeCzfGY2W6IQQI2A4G"

		header={
			"apikey":search_key
		}

		Params={
		"fly_from":From,
		"fly_to":To,
		"dateFrom":Date1,
		"dateTo":Date2
		}


		response=requests.get(url=tequila_endpoint,headers=header,params=Params)
		flights_all=response.json()

		return flights_all









