import turtle
from turtle import *
import random


COLORS=['red','orange','yellow','green','skyblue','cyan','grey','pink']
class RandomCars:

	def __init__(self):
		self.cars_list=[]
		self.generate_cars()


	def random_color(self):
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		return r,g,b

	def create_cars(self):
		new_car=Turtle()
		new_car.shape('square')
		new_car.shapesize(1,3)
		new_car.speed(0)
		new_car.color(random.choice(COLORS))
		new_car.penup()
		new_car.goto(270,random.randint(-140,140))
		self.cars_list.append(new_car)

	def generate_cars(self):
		num=random.choice([1,3,4,5,6,7,8,9])
		if num % 3==0:
			self.create_cars()
		


