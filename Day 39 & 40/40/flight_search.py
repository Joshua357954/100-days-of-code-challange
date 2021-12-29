import requests


class FlightSearch:


	def get_available_flights(self,From,To,Date1,Date2):
		tequila="https://tequila-api.kiwi.com/v2/search"
		key="3-kRbw9VSRq96JUeCzfGY2W6IQQI2A4G"

		header={
			"apikey":key
		}

		Params={
		"fly_from":From,
		"fly_to":To,
		"dateFrom":Date1,
		"dateTo":Date2
		}


		response=requests.get(url=tequila,headers=header,params=Params)

		avail_flights=response.json()

		return avail_flights