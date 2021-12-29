import requests
from notification import Notfication

class Users:

	def __init__(self,name="",email1="",email2=""):
		self.NAME=name
		self.EMAIL=email1
		self.EMAIL2=email2
		self.email_min_length=15
		self.email_domain="@gmail.com"
		self.min_name_length=3
		self.sheet_name="flightFinder"
		self.sheet_sub_name="users"
		self.endpoint=f"https://api.sheety.co/8b35da8ed66eeb5e24fa4b4c111ade84/{self.sheet_name}/{self.sheet_sub_name}"

	def is_cred_valid(self):
		# NAME="Joshua"
		# EMAIL="boyijoshua72@gmail.com"
		# EMAIL2="boyijoshua72@gmail.com"

		if not self.NAME or len(self.NAME)< self.min_name_length or self.EMAIL =="" \
			or  not self.EMAIL.endswith(self.email_domain)\
		   	or self.EMAIL2 =="" or not self.EMAIL2.endswith(self.email_domain)\
		   	or self.EMAIL != self.EMAIL2 or len(self.EMAIL)< self.email_min_length\
		   	or len(self.EMAIL2)<self.email_min_length:

			err="Pls Check Your Info and try again ..." # ===========================
			print(err)
			return False

		else:
			correct="Valid Credentials"
			print(correct)
			return True

	def get_all_users(self):
		res=requests.get(url=self.endpoint)

		return res.json()['users']

	def user_exists(self):
		all_data=self.get_all_users()	
		# for user_data in all_data:
		# 	if self.EMAIL == user_data['email']:
		# 		print(user_data['email'])
		# 		return True 
		# 		break
		# 	else:
		# 		return False

		if self.is_cred_valid():

			check=[value for item in all_data for key,value in item.items() ]
			if self.EMAIL in check:
				print("Email exists ..")
				return True #===========================


		


	def create_new_user(self):

		if self.is_cred_valid():

			if not self.user_exists():
				param={
				"user":{
					"name":self.NAME,
					"email":self.EMAIL
					}
				}
				print("started")
				new_record=requests.post(url=self.endpoint,json=param)

				print(new_record.json())
				msg="New User Successfully Created"
				print(msg) 

				return True
			else:
				return ("Pls Try another email ,this user already exists")

		

	def send_all_notification(self,message):
		users_all=self.get_all_users()
		for users in users_all:
			mail=user['email']

			new_nofify=Notification(sent_to=mail)
			new_nofify.send_message(message)

