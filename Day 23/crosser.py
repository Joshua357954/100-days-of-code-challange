from turtle import *



class Crosser(Turtle):
	def __init__(self):
		super().__init__()
		self.shape('turtle')
		self.color('black')
		self.penup()
		self.speed(0)
		self.setheading(90)
		self.goto(0,-170)

	def walk(self):
		self.setheading(90)
		self.forward(10)
