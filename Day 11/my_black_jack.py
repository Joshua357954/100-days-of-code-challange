

# Print the black jack logo 
from art import logo
import random
from os import system 

system('cls')
# create a deel card function 
def deel_card():
	card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
	return random.choice(card)

# create a list of available carda
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]

# get current score ( fitered score with the black jack rules... )


def player_score(card):

	if len(card)==2 and sum(card)==21:
		return 0

	if 11 in card:
		card.remove(11)
		card.append(1)

	return sum(card)

def compare(computer_score,user_score):

	if computer_score== user_score:
		return "Aww , its a draw"
	elif computer_score==0:
		return "You won ,with a black jack ..."
	elif user_score==0:
		return "Ohh, you lose opponent win with a black jack"
	elif computer_score >21:
		return "You win ,opponent went over."
	elif user_score >21:
		return "Opponent won , you went over"
	elif computer_score > user_score:
		return " Computer , wins ..."
	else:
		return "You win"
def black_jack():
	user_card=[]
	computer_card=[]

	for _ in range(2):
		user_card.append(deel_card())
		computer_card.append(deel_card())

	go_again=False

	# create user and computer score 
	while not go_again:
		user_score=player_score(user_card)
		computer_score=player_score(computer_card)

		print(f"\n You have {user_card} = Current score {user_score}")
		print(f"\n Computers first card {computer_card[0]}\n")

		if computer_score==0 or user_score==0 or user_score>21:
			go_again=True
		else:
			#ask the user if they want to draw another card

			do_you=input("Do you want to draw another card : ")

			if do_you.lower()=='y' or do_you.lower()=='yes':
				user_card.append(deel_card())
			else:
				go_again=True

	# The computers turn to play....
	while computer_score!=0 and computer_score <17:
		computer_card.append(deel_card())
		computer_score=player_score(computer_card)

	print(f"\n You Ended With {user_card} which = {player_score(user_card)} ..\n And Computer With {computer_card} which = {player_score(computer_card)}..")

	# check the game with a compare function
	 
	print(f'\n {compare(computer_score,user_score)}')

	start_new=input(f"\nDo you want to play another round 'y' or 'n' :")

	if start_new.lower()=='y' or start_new.lower()=="yes":
		# run the loop again with a recursion ,clear screen and display art ....
		system('cls')
		black_jack()
	else:
		print("\n Game Over :)")

black_jack()