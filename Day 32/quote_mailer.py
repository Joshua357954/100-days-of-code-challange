
from datetime import datetime
from random import *
import smtplib

day_of_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

EMAIL='csfunn100@gail.com'
PASSWORD="joshuajaymikee"



# check weekday
now=datetime.now()
day=day_of_week[now.weekday()]
month=now.month

# open quotes file 
with open('quote.txt','r')as quotes:
	new_quote=quotes.readlines()

	# pick a random quote
	choosen_quote=choice(new_quote)
	

# if weekday==Tuesday:
if day == "Thursday":
	print(f"Yes is {day} , hurray ....")



# send to your self
server=smtplib.SMTP('smap.gmail.com',576)
server.starttls()
server.login(EMAIL,PASSWORD)
server.sendmail(from_addr=EMAIL,to_addr='boyijoshua72@gmail.com',
					message=f"Subject: {day} Quote\n\n{choosen_quote}")

server.close()




