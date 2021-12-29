# This is the day 37 of the 100days of code 
import requests
from datetime import datetime

USERNAME="jayblinks"

TOKEN="krog94fb03v4gkhg94f392j2rf3jgrg9"

GRAPH_ID="exercise"

USER_ENDPOINT="https://pixe.la/v1/users"

GRAPH_ENDPOINT=f"https://pixe.la/v1/users/{USERNAME}/graphs"

ADD_PIXEL_ENDPOINT=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

HEADER={"X-USER-TOKEN":TOKEN}

DT=datetime.now()

DATE=DT.strftime("20%y%m12")

UPDATE_PIXEL_ENDPOINT=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

DELETE_ENDPOINT=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

# setup pixela account with post requests

# user_params={
# 	"token":TOKEN,
# 	"username":USERNAME,
# 	"agreeTermsOfService":"yes",
# 	"notMinor":"yes"
# }

# res=requests.post(USER_ENDPOINT,json=user_params)
# print(res.json())

# GRAPH_PARAMS={
# 	"id":GRAPH_ID,
# 	"name":"work-out",
# 	"unit":"commit",
# 	"type":"int",
# 	"color":"kuro"
# }
# Graph setup
# res2=requests.post(GRAPH_ENDPOINT,headers=HEADER,json=GRAPH_PARAMS)
# print(res2.text)

AP_PARAMS={
	'quantity':'30',
	'date':DATE,
}
 
# Add a Pixel 
# res3=requests.post(ADD_PIXEL_ENDPOINT,headers=HEADER,json=AP_PARAMS)
# print(res3.json())

# Update a pixel
# res4=requests.put(UPDATE_PIXEL_ENDPOINT,headers=HEADER,json={"quantity":"40"})
# print(res4.json())


# Delete a pixel 

res5=requests.delete(DELETE_ENDPOINT,headers=HEADER)
print(res5.text)


