#This is the day 33 of the 100days of code ..........
# project : iss notifier ...

import requests
from datetime import datetime
import time 
import smtplib

# MY_LAT=9.0820
# MY_LON=8.6753
MY_LAT=37.0902
MY_LON=95.7129

MY_MAIL="csfunn100@gmail.com"
PASSWORD="joshuajaymikee"
TO_MAIL="boyijoshua71@gmail.com"


def is_iss_overhead():
	r=requests.get('http://api.open-notify.org/iss-now').json()['iss_position']

	lng,lat= float(r['longitude']) , float(r['latitude'])
	
	if MY_LAT-5 <= lat <= MY_LON+5 and MY_LAT-5 <= lng <= MY_LON-5:

		return True


def is_night():

	sun=('https://api.sunrise-sunset.org/json')

	SUNS={
		'lat':MY_LAT,
		'lng':MY_LON,
		'formatted':0,
	}

	sun_res=requests.get(sun,params=SUNS).json()['results'] # goten hold of the key results out of the api returned json

	sunrise=sun_res['sunrise'].split(' ')[0].split('T')[1].split('+')[0].split(':')[0]

	sunset=sun_res['sunset'].split(' ')[0].split('T')[1].split('+')[0].split(':')[0]

	p_hour=datetime.now().p_hour

	if p_hour <= sunrise or p_hour >= sunset:

		return True 


def send_email(message):
	conn=smtplib.SMTP('smpt.gmail.com')
	conn.starttls()
	conn.login(MY_MAIL,PASSWORD)
	conn.sendmail(from_addr=MY_MAIL,to_addr=TO_MAIL,msg=f"Subject: Look up\n\n{message}")

print("I am running oh ...")

while True :
	time.sleep(5)

	if is_iss_overhead and is_night:
		send_email(message='The iss is overhead .......')

# url=('http://api.open-notify.org/iss-now')
# print(sunrise.split(' ')[0].split('T')[1].split('+')[0].split(':')[0])
# now=datetime.now()
# print(now.strftime('%H'))


# # {
#   "message": "success", 
#   "timestamp": UNIX_TIME_STAMP, 
#   "iss_position": {
#     "latitude": CURRENT_LATITUDE, 
#     "longitude": CURRENT_LONGITUDE
#   }
# }


