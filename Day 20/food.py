from turtle import Turtle 
import random 


class Food(Turtle):
	def __init__(self):
		super().__init__()

		self.shape('circle')
		self.color('blue')
		self.penup()
		self.random_food()


	def random_food(self):
		r1=random.randrange(-250,250)
		r2=random.randint(-250,250)
		self.goto(r1,r2) 


