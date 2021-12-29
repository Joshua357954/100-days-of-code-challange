# This is the day 23of the 100days of code and the project is the crossing turtle
from turtle import *
from crosser import Crosser
from random_cars import RandomCars
from score import ScoreB
import time
# CONSTANTS
TITLE='My Turtle Crosser Game .'
HEIGHT=400
WIDTH=600
GAME_ON=True
SPEED=10

# create the random cars class
# create the crossing turtle class
# define the moving strategy
# instanciate the turtle and the random cars object
# move the crosser with the up arrow key
# check collision with random cars
# check if it has reached is end point

# OTHER OBJECT
cars=RandomCars()
crosser=Crosser()
score=ScoreB()


# SCREEN SETUP
screen=Screen()
screen.title(TITLE)
screen.setup(width=WIDTH,height=HEIGHT)
screen.listen()

screen.onkey(crosser.walk,'Up')

while GAME_ON:

	time.sleep(0.4)
	
	cars.generate_cars()

	if crosser.ycor()>170:
		print("Reached ...")

		# Go to the next level
		score.next_level()

		# Increase the speed by 10
		SPEED+=5
		# Take the turtle to the start pos
		crosser.goto(0,-180)
		

	for car in cars.cars_list:
		if crosser.distance(car)<40:
			score.game_over()
			crosser.hideturtle()
			GAME_ON=False

		car.backward(SPEED)


	
		








screen.mainloop()
