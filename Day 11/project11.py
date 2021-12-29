# This is project 11 of the 100 days of code ohhh.....
#BLACK JACK PROJECT...

# RULES ..
# The deck is unlimited in size 
# The queen/king/jack are 10
# The ace is 11 or 1 , as you choose what you want it to be 
# The following are the list of card that are used to play the game

# The cards in the list have equal probbility of being drawn 
# The card cannot be removed can only be drawn
import random 
from os import system,name
from art import logo


def deel_card():
	card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
	return random.choice(card)


# Calculate a calculate_sum function and it take a list as an argument and returns the sum of the
#list of the card

card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
system('cls')
def calculate_score(card): 

	# Call calculate score if computer or the user has a black jack (0), or if the 
	#user score already 21 or above ,end game

	if sum(card) ==21 and len(card)==2:

		return 0


	# inside the calculate function ,chack for a 11 (ace) ,if score already over 21,
	# remove the 11 and replace it with one,

	elif 11 in card and sum(card)>21:
		card.remove(11)
		card.append(1)
		
		

	return sum(card)


def compare(user_score,computer_score):

# Create a function called compare() and pass in the computer_score and the user_score , if
# the computer and user have same score then its a draw , if the computer has a blackjack of (0)
# then the user loses, if the user has a blackjack of (0) , then the user wins ,if the user score 
# is more than 21 , the the user loses ,if the computer score is more than 21 the computer loses
#if none of the above the player with the highest score wins 


	if user_score== computer_score:
		return "Its a draw ..."

	elif computer_score==0:
		return "Loose , with a blackjack owww."

	elif user_score==0:
		return "Hey you win , with a blackjack ...."

	elif user_score > 21:
		return "You lose ,You went over. "

	elif computer_score > 21:
		return "You win , Opponent went over."

	elif user_score > computer_score:
		return "You win  ...."

	else:
		return " You loose"

def play_game():

	# Deal the computer and user two cards each

	user_card=[]
	computer_card=[]

	for _ in range(2):
		user_card.append(deel_card())
		computer_card.append(deel_card())



	go_again=True

	while go_again:

		# The calculate_sum() will  rechecked everytime the deel card function is called ....
		
		user_score=(calculate_score(user_card))

		computer_score=(calculate_score(computer_card))

		print(f"\n Your cards {user_card} , Current score : {user_score}\n ")

		print(f" Computer 1st card is {computer_card[0]}\n ")

		if user_score==0 or computer_score==0 or user_score>21:
			go_again=False

		else:

			# If the game has not ended , ask if the user want to draw another card if yes ,use the
			# deel_card() to deal another card and add to the user card_list ,else game has ended ....

			draw_again=input("Do you want to draw another card 'y' or 'no' :  ")

			if draw_again.lower()=="y" or draw_again.lower()=="yes":

				user_card.append(deel_card())

			else:
				go_again=False



	# Ones the user is done and no longer wants to draw card ,its time to let the computer to play, 
	# while the computer score is less than 17 .

while computer_score !=0 and computer_score < 17:
	computer_card.append(deel_card())
	computer_score=calculate_score(computer_card)


	
	print (f'\n Computer ends with :: {computer_card} = {sum(computer_card)} and \n You with {user_card} = {sum(user_card)} \n')
	print(f"{compare(user_score,computer_score)} ...\n")
 
	wish=input("Do you wish to play again : ")
	if wish.lower()=='y' or wish.lower()=='yes':
		system('cls')
		play_game()
	else:
		print("\nBye ....")
		pass

play_game()
# ask if the want to play again ,if yes clear screen and start a new game and show the logo from
#art.py









