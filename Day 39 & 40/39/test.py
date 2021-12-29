import requests
from datetime import datetime

SH_URL="https://api.sheety.co/9c9131b74e93a891e24c213fc26b7da4/flightFinder/flights"
UP="https://api.sheety.co/9c9131b74e93a891e24c213fc26b7da4/flightFinder/flights"

# res=requests.get(url=SH_URL)
# print(res.json())
New_data={
	"flight":
	{
		"destination":"Senegal",
		"iata":"SG",
		"price":300
	}
}
# res1=requests.post(url=f"{UP}",json=New_data)

# print(res1.json())

Tequila_Endpoint="https://tequila-api.kiwi.com"
KIWI_APIKEY="LrdXOK1wdtFjQX8n7v6wd7mezGUMXICU"








# First get a flight search api
# configure and test the api functionalities (main.py)
# Get a class structure for the code to be written 
# like date manager ,flight search ,notify 

Params={
	"fly_from":"LGA",
	"fly_to":"MIA",
	"dateFrom":"19/12/2021",
	"dateTo":"10/5/2022"
	}

Params2={
"term":"new york", # city name to get iata code ...
"location_types":"city"
}

LOCATION_ENDPOINT="https://tequila-api.kiwi.com/locations/query"
Tequila_endpoint="https://tequila-api.kiwi.com/v2/search"
Search_T="/v2/search"

SEARCH_KEE="3-kRbw9VSRq96JUeCzfGY2W6IQQI2A4G"
LOCATION_KEE="ZwL2mYfOou3rFlJSSjAqa7ce8mLBkuC5"

res4=requests.get(url=LOCATION_ENDPOINT,headers={"apikey":LOCATION_KEE},params=Params2)
print(res4.json()["locations"][0]["code"])


# res3=requests.get(url=Tequila_endpoint,headers={"apikey":KEE},params=Params)
# print(res3.json())


































