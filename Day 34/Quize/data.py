import requests

parameters={
	'amount':5,
	'category':18,
	'difficulty':'easy',
	'type':'boolean'
}

url='https://opentdb.com/api.php'

res=requests.get(url,params=parameters).json()

quests=res['results']

