# This is the project 18 of the 100days of code and involves The Turtle Module In python 

from turtle import Turtle,Screen, screensize, shapesize
import time
import random

jack=Turtle()

def draw_shape(num_of_sides):
	for i in range(num_of_sides):
		angle=360/num_of_sides
	
		jack.forward(55)
		jack.rt(angle)



# letter=['d','f','c','e']
# for num in range(3,10):
# 	nik=random.randrange(3,9)
# 	jack.pensize(5)
# 	jack.color(f"#{random.choice(letter)}{nik}{random.choice(letter)}{nik}{random.choice(letter)}{nik}")
# 	draw_shape(num)
 
# n_o_s=9
# for i in range(n_o_s):
# 	ang=360/n_o_s
# 	jack.forward(70)
# 	jack.right(ang)

for _ in range(74):	
	jack.left(65)
	jack.forward(70)
	jack.left(20)
	jack.forward(70)
	jack.setheading(jack.heading()+10)

jack.hideturtle()





screen=Screen()
screen.exitonclick()




















