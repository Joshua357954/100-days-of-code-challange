# This is the day 20 of the 100 days of code ...
# Project : Making a snake game 

import turtle as t
from turtle import *
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time
import random


DELAY=0.2
WIDTH=600
HEIGHT=600
TITLE="SNAKE GAME "
GAME_ON=True


# Screen Setup 
screen=Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.title(TITLE)
screen.tracer(0)
screen.listen()
# The food of the snake 

food=Food()
snake=Snake()
score_b=ScoreBoard()

screen.listen()
# on key movement
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

while GAME_ON:

	time.sleep(DELAY)
	screen.update()

	snake.move()

	# check if snake collide with food
	if snake.head.distance(food)<17:
		
		food.random_food()
		snake.add_snake()
		# Add score board 
		score_b.add_score()
		if DELAY >-1:
			
			print(DELAY)

	
	# Check if collide with wall
	if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
		score_b.reset_score()
		score_b.writer()
		DELAY-=0.001
		
		snake.reset()

	# Check if collide with snake 
	for part in snake.segments[1:]:
		if snake.head.distance(part)<19:
			# implement the high sccore fnctionality 
			score_b.reset_score()
			snake.reset()



screen.exitonclick()











