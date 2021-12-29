#This is the day 19 0f the 100 days of code still on the turtle module ...
# Project turtle race ...

import turtle as t 
from turtle import *
import random
WIDTH=500
HEIGHT=400
screen=Screen()
screen.setup(WIDTH,HEIGHT)

all_racers=[]

def play_game():
	global all_racers

	# User chooses who to win ...
	bet=textinput('Who Will Win',"Place Your Bet")
	# Standing positions of the turtles
	pos=[-90,-40,10,60,110,160]
	#Colors of the turtle ...
	colors=['red','orange','yellow','green','blue','indigo']

	for runer in range(0,6):
		player=t.Turtle("turtle")
		player.penup()
		player.color(colors[runer])
		player.goto(x=-200,y=pos[runer])
		all_racers.append(player)

	game_on=False

	if bet:
		game_on=True

	while game_on:
		for new_player in all_racers:
			if new_player.xcor() > 230:
				game_on=False
				winner_color=(new_player.pencolor())
				
				if bet.lower()==winner_color.lower():
					print(f"You Win ,The {winner_color} is the winner")
				else:
					print(f"You Lose ,The {winner_color} is the winner")

				
			else:
				# print(new_player.position())
				# print(new_player.color())
				speed=random.randrange(0,10)
				new_player.forward(speed)

play_game()

def go_again():
	global all_racers
	screen.clear()
	all_racers=[]
	play_game()



screen.listen()
screen.onkey(lambda : go_again(),'r')
screen.mainloop()

