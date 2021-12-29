# create variable ATTEMPTS set it to 10
import random
from os import system

ATTEMPTS=10
NUMB=random.randint(0,101)
GAME=False

# This is the function that starts the game and re-runs the code  .... 
def play() :
	global GAME,ATTEMPTS,NUMB
	NUMB=random.randint(0,101)
	system('cls')

	print("\n-------------- Guess The NUMBER --------------------------------------\n")

	print("I am thinking of a word from 1 - 100")

	# This is the function thats holds the main game functionality..
	def guess():
		global ATTEMPTS,NUMB,GAME
		user_input=int(input("Guess the NUMBER :  "))

		if user_input==NUMB:
			print (f"\nHey you got it right is {NUMB}")
			GAME=True
		else:
			ATTEMPTS-=1
			if user_input>NUMB:
				print("Too high ..")
			else:
				print("Too low")
			print(f"You have {ATTEMPTS} ATTEMPTS left\n")

		if ATTEMPTS==0:
			print(f"\n You loose ...The NUMBER is {NUMB}")
			GAME=True
		
		if GAME:
			p_a=input("\nDo you want to play again : ")
			if p_a.lower()=="y":
				play()
				GAME=False
			else:
				print("\nGame Over :) .........")

	# choose your levels ....		
	level_up=input("Choose your level easy or hard : ")
	if level_up=="hard":
		ATTEMPTS=5
	else:
		ATTEMPTS=10
	# use a while loop to continue checking the NUMBER 
	while not GAME :

		guess()

play()
