import requests
from twilio.rest import Client

class MakeNotification:


	def send_message(self,message):
		account_sid = 'AC1e0520b0facda6157a17c60722c10d6c'
		auth_token = '3bc587632e36a100f8d0922e6c3e7ede'
		twilio_number="+12722043425"
		my_number="+2349034954069"
		client=Client(account_sid,auth_token)

		message=client.messages.create(
					from_=twilio_number,
					to=my_number,
					body=message,
			)

		return (message.status)