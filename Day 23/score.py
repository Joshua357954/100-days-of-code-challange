from turtle import *

FONT=("courier",20,'normal')


class ScoreB(Turtle):
	def __init__(self):
		super().__init__()
		self.level=1
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color('black')
		self.goto(-200,160)
		self.write_it()



	def write_it(self):
		self.clear()
		self.write(f"Level : {self.level}",align="center",font=FONT)

	def next_level(self):
		self.level+=1
		self.write_it()

	def game_over(self):
		self.goto(0,0)
		self.write(" GAME OVER ",align='center',font=FONT)