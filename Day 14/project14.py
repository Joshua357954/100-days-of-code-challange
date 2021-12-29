# This is the Day14 project of the 100 dayas of code ...
# This is the higher or lower project ......
import random
from data import people
from os import system
from art import logo

# Print the logo and clear screen for the game to start ...
system('cls')
print(logo)

# This variable Keeps track of the score ...
score=0
go_again=True

# create a model for the questions with a function
def entity(person):
	name=person['name']
	discription=person['discription']
	country=person['country']
	return (f"{name} , {discription} from {country}")

def highest(a,b):
	''' This Function returns the account with the highest followers with the representation A or B'''
	if a['followers'] > b['followers']:
		return 'a'
	return 'b'

def check_answer(guess,answer):
	''' This Function checks the returned value from the highest function ,
	returns true or false based on if the users guess is equal to the highehst functions returned value '''
	if guess == answer:
		return True
	return False

# make the code run contineously until the user make a wrong guess ....
while go_again:

	# This holds the random account
	person_a=random.choice(people)
	person_b=random.choice(people)
	if person_a==person_b:
		person_b=random.choice(people)


	print(f"\nCompare A : {entity(person_a)}")

	print("\n                 V / S                 \n")

	print(f"Against B : {entity(person_b)}\n")


	# Ask the user to make a guess
	guess=input("Who has the highest follower ? ,A or B :").lower()

	# check if the answer is correct ...
	if check_answer(guess,highest(person_a,person_b)):
		score+=1
		# clear screen and print the logo again ...
		system('cls')
		print(logo+'\n')
		print(f"\n You got it right , Current Score {score}\n")

	else:
		print(f"\nYou Got It  Wrong :).....")
		go_again=False

























