import turtle
from turtle import *
import random


dok=turtle.Turtle()
turtle.colormode(255)
dok.penup()
dok.fillcolor("red")
dok.speed(0)

def random_colors():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	return (r,g,b)


dok.setheading(215)
dok.forward(400)

num_of_dot=100

for d_count in range(1,num_of_dot+1):
	dok.setheading(0)
	dok.dot(20,random_colors())
	dok.forward(50)

	if d_count % 10 == 0:
		
		dok.setheading(90)
		dok.forward(50)
		dok.setheading(180)
		dok.forward(500)
		dok.setheading(0)

dok.hideturtle()

# This is my own version of the herist painting...
# def heirst(gap,gaps,dot_size):
# 	for _ in range(10):
# 		for _ in range(10):
# 			dok.color(random_colors())
# 			dok.dot(dot_size)
# 			dok.forward(50)

# 		dok.goto(x=-160,y=gaps)
# 		gaps-= gap

# heirst(-50,-150,20)

# dok.hideturtle()




screen=Screen()
screen.exitonclick()