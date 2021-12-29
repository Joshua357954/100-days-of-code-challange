
# This is the etch a sketch project ...

import turtle as t 
from turtle import *
import random

t.colormode(255)
jack=Turtle() 
screen=Screen()





# # def f():
# 	jack.forward(10)




def clear():
	jack.clear()
	jack.penup()
	jack.home()
	jack.pendown()


def change_c():
	r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
	jack.color(r,g,b)

def plus_pen():
	current_size=jack.pensize()
	new_s=jack.pensize() +1
	jack.pensize(new_s)
	#screen.update()

def minus_pen():
	current_size=jack.pensize()
	if current_size >0:
		new_s=jack.pensize()-1
		jack.pensize(new_s)

screen.listen()
screen.onkey(lambda : plus_pen() , 'n')
screen.onkey(lambda : minus_pen() , 'm')
screen.onkey(lambda : jack.left(jack.heading()+5),'a')
screen.onkey(lambda : jack.right(jack.heading()-5),'s')
screen.onkey(lambda : jack.backward(10),'d')
screen.onkey(lambda : jack.forward(10),'f')
# Exit the screen ....
screen.onkey(lambda : exit(0),'e')
screen.onkey(change_c,'k')
screen.onkey(clear,'c')
screen.mainloop()