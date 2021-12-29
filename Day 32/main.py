# This is the day 32 of the 100days of code 
# happy birthday wisher ....
import datetime
from datetime import datetime
import pandas
from random import *
# server=SMPTLIB.smpt("smpt@gmail.com")
# server.starttls()
# server.login(gmai.,password)
# server.sendmail(fromadd,toaddr,message)

# Read the csv 
# convert the day,month to a tuple as a key and the remaining values 
#as the value of the dict
#check if the day is same with the current day and month
# if so take a random tex file 
# replace with the [NAME] with the actual birthday name
# initialize the smptlib 
# send the mail......

dow=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

now=datetime.now()
date_t=(now.day,now.month)

file=pandas.read_csv("birthdays.csv")

people={ (values.day,values.month):values for index,values in file.iterrows()}


if date_t in people:
	b_person=people[date_t]

	with open(f"birthday_letters/birthday_letter_{randint(1,3)}.txt")as letter:

		new_letter=letter.read().replace("[NAME]",b_person['name'])

import smtplib

with smtplib.SMTP('smtp.gmail.com')as server:
	server.starttls()
	server.login('yusluvjoseph3@gmail.com',"nobodyboy")
	server.sendmail(from_addr="yusluvjoseph3@gmail.com",to_addr="boyijoshua72@gmail.com",message=f"Subject : Happy Birthday From {MY_NAME},\n\n{new_letter}")

