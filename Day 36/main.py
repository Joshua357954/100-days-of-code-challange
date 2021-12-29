# A clone bloomberg terminal
# STOCK_API_KEY="E9p1dCO0NfVXjhBfq9JCRsgAHAQl8irU"
# My python imports (pythons in-built packages)

from twilio.rest import Client
from requests import get
from  datetime import datetime

# STOCK_NAME="TSLA"
# COMPANY_NAME="Tesla, Inc"
STOCK_NAME="FB"
COMPANY_NAME="Meta Platforms, Inc"

#==============
account_sid = 'AC1e0520b0facda6157a17c60722c10d6c' 
auth_token = '3bc587632e36a100f8d0922e6c3e7ede'

#==============
SN_API_KEY="1e9892d6117d4fa080ed658c4fbb09dd"    #"TbUYpt0M8oK1IUhu9DJWM4IZ0nhMyjSVze3Y32Iv"
AV_API_KEY="3UJMF1EP5FFZS6W5"

DT=datetime.now().day

SN_PARAMS={
	"apiKey":SN_API_KEY,
	"q":COMPANY_NAME,
	#"filter_entities":'True'
# 	exchanges=NYSE&filter_entities=true&limit=10&published_after=2021-12-09T09:30&api_token=YOUR_API_TOKEN
}

AV_PARAMS={
	"function":"TIME_SERIES_DAILY",
	"symbol":STOCK_NAME,
	"apikey":AV_API_KEY
}
SN_URL="https://newsapi.org/v2/everything"     #https://api.marketaux.com/v1/news/all"
AV_URL="https://www.alphavantage.co/query"

AV_RES=get(AV_URL,params=AV_PARAMS)
SN_RES=get(SN_URL,params=SN_PARAMS)

AV_RES.raise_for_status()

# get yesterdays closing stock price
Y_Close=float(AV_RES.json()['Time Series (Daily)'][f'2021-12-{DT-1:02d}']['4. close'])

# get the day before yesterday closing stock price
DB_Y_Close=float(AV_RES.json()['Time Series (Daily)'][f'2021-12-{DT-2:02d}']['4. close'])


# get the difference if the stock went high or low 
high_low=(Y_Close -DB_Y_Close)

def is_stock_up():
	if Y_Close > DB_Y_Close:
		return "👆Up"
	return "👇Down"


# get the percentage difference
P_DIFF=((Y_Close - DB_Y_Close)/(Y_Close + DB_Y_Close)/2)*100


# get a stock news api endpoint

# get the stock news headline about that comapany name
# print(SN_RES.json()['articles'][0]['description'])

# pick the first three news headline 
Two_News=SN_RES.json()['articles'][:1]

# if the percentage is greater than 4 or what so ever 
if abs(P_DIFF)>=.05:
	for news in Two_News:
		full_msg=f"{STOCK_NAME}\n Stock : {is_stock_up()} \nNews : {news['description']}"

# send message to me with the (percentage diff ,stock name ,headline )

		client=Client(account_sid,auth_token)

		message=client.messages.create(
									body=full_msg,
									from_="+12722043425",
									to="+2349034954069"
			)
	 
		print(message.status)

else:
	print("The stock does not have value ...")
