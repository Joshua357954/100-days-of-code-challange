import requests
import gspread
import time
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from pprint import pprint

DATE=datetime.now().strftime("%d/%m/%Y")
TIME=datetime.now().strftime("%X")

GENDER='male'
AGE=18
WEIGHT=14.8
HEIGHT=5.4

NX_APP_ID="9c3a4b13"
NX_API_KEY="a2ae2bbc7ba57d436b47f3eecd61abc4"
NX_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"

# #=================================
scope=['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("g-json.json",scope)
client = gspread.authorize(creds)
sheet= client.open("myworkout").sheet1

# #================================

NX_HEADER={
	"x-app-Id":NX_APP_ID,
	"x-app-Key":NX_API_KEY
}

NX_PARAMS={
	"query":"danced for 10minutes and cycled for 60seconds",
	"gender":GENDER,
	"weight_kg":WEIGHT,
	"height_cm":HEIGHT,
	"age":AGE
}


res=requests.post(url=NX_ENDPOINT,headers=NX_HEADER,json=NX_PARAMS)

# All_records=[({'exercise':item['user_input']},{'duration':item['duration_min']},{'calories':item['nf_calories']}) for index,item in enumerate(NEW_RES)]
# pprint(All_records)



# SHEET_ID="15X1QCbrxzjLpiZDiIOyFKIF4FWeF4p3ffS7-uSwUc1A"
# URL="https://api.sheety.co/9c9131b74e93a891e24c213fc26b7da4/myworkout/myworkout"

# S_HEADERS={
# 	"Authorization": "Bearer 3494gfrjbmivfnbsor0f4kekmsxz",
# 	"Content-Type":"application/json"
# }

# Sheety_params={
# 	"myworkout":
# 		{
		
# 		"Date":DATE,
# 		"Time":TIME,
# 		"Exercise":"Sunning",
# 		"Duration":"12",
# 		"Calories":"21"
# 		}
# }


# res=requests.post(url=URL,headers=S_HEADERS,json=Sheety_params)

# pprint(res.json())

# res=requests.get(url=URL,headers=S_HEADERS)
# pprint(res.json())

NEW_RES=res.json()['exercises']

for data in NEW_RES:

	C_TIME=datetime.now().strftime("%X")
	work_out_data=[
		C_TIME,
		DATE,
		data["user_input"],
		data["duration_min"],
		data["nf_calories"]
	]
	time.sleep(2)
	sheet.append_row(work_out_data)










