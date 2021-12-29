
from turtle import *


class Score_B(Turtle):
	def __init__(self):
		super().__init__()

		self.l_score=0
		self.r_score=0
		self.penup()
		self.color("black")
		self.hideturtle()
		self.update_score()

		

	def update_score(self):
		self.clear()
		self.goto(50,170)
		self.write(f"{self.r_score}",font=("Ariel",40,"normal"))

		self.goto(-50,170)
		self.write(f"{self.l_score}",font=("Ariel",40,"normal"))


	
