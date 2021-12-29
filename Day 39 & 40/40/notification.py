import smtplib
import html

class Notfication:
	def __init__(self,sent_to):
		self.MY_EMAIL="csfun100@gmail.com"
		self.PASSWORD="mypassword"
		self.SEND_TO=send_to #"boyijoshua72@gmail.com"
		self.SUBJECT="Josh From Cheap Flight Club :)"
		self.MESSAGE="Calculator \n Pomodoro Timer \n Blackjack Game \n Random user generator\
				and many more in subsiquent times \n Peace from this side .."
	
	def unescape_emoji(self):
		pass

	def send_message(self,message):
		with smtplib.SMTP("smtp.gmail.com",587) as server:
			server.starttls()
			server.login(self.MY_EMAIL,self.PASSWORD)
			server.sendmail(self.MY_EMAIL,self.SEND_TO,msg=f"Subject: {self.SUBJECT}\n\n{message}")

 




