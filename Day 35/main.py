import requests 
from twilio.rest import Client 

key='5a846e9c968a4632f92d3e978c07c118'

# 4.8156° N, 7.0498°

MY_LAT=4.8156
MY_LON=7.0498


OWMP={
	"lat":MY_LAT,
	"lon":MY_LON,
	"appid":key,
	"exclude":['currently','minutely','daily','alerts']
}
weather_endpoint='http://api.openweathermap.org/data/2.5/onecall'
# https://api.openweathermap.org/data/2.5/onecall?
# lat={lat}&lon={lon}&exclude={part}&appid={API key}
# 9653fca2b29b0b09daa759356ccd713f
# 5a846e9c968a4632f92d3e978c07c118

res=requests.get(weather_endpoint,params=OWMP)
res.raise_for_status()
response=res.json()

twelve_hour_data=response['hourly'][:12]


def will_rain():
	for hour in twelve_hour_data:
		if hour['weather'][0]['id']<700:
			return True

if will_rain():

	account_sid = 'AC1e0520b0facda6157a17c60722c10d6c' 
	auth_token = '3bc587632e36a100f8d0922e6c3e7ede' 
	client = Client(account_sid, auth_token) 
	 
	message = client.messages.create(  
								body="Josh Bot : Hello it will rain remember to take your umbrella☂...",
								from_='+12722043425',
								to='+2349034954069' 
	                          ) 
	 
	print(message.status)

# sid='AC1e0520b0facda6157a17c60722c10d6c'
# auth_token='3bc587632e36a100f8d0922e6c3e7ede'
