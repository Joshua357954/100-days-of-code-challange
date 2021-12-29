import turtle  as t
from tkinter import *
import random 

man=t.Turtle(shape='arrow')

directions=[0,180,90,270,180,90,0,270,]
man.pensize(4)
man.speed(0)
t.colormode(255)

def random_colors():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	return (r,g,b)

def draw_spirograph(size_of_gap):
	for i in range(int(360/size_of_gap)):
		man.pencolor(random_colors())
		man.setheading(man.heading() +size_of_gap)
		man.circle(120)


# draw_spirograph(5)
	

# Random Walk spirograph...

directions=[0,90,180,270]	
def random_walk():
	for _ in range(300):
		my_color=random_colors()
		man.pencolor(my_color)
		man.forward(30)
		man.left(random.choice(directions))

random_walk()








screen=t.Screen()
screen.exitonclick()

