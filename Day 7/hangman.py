# This is a hangman project of the 100 days of code
import random

WORD_LIST=['joshua','daniel','solomon']

CHOOSEN_WORD=random.choice(WORD_LIST)

TRIES=6

print(CHOOSEN_WORD)
print(f"You have {TRIES} in total... ")

DISPLAY=[]

WORD_LENGTH=len(CHOOSEN_WORD)

COMPLETED=False

for _ in range(0,WORD_LENGTH):
	DISPLAY.append("_")

# To print the dashes for the first time....
print((" ".join(DISPLAY))) 


# The main hangman function ....

def hangman(run_am=""):

	global DISPLAY,WORD_LENGTH,COMPLETED,TRIES,WORD_LIST,CHOOSEN_WORD

	GUESS=input("Enter a word : ")

	if  GUESS not in CHOOSEN_WORD:
		TRIES-=1
		print(f"You have {TRIES} left... \n")

	else:
		for position in range(len(CHOOSEN_WORD)):
			
			letter=CHOOSEN_WORD[position]

			if GUESS == letter:
				DISPLAY[position]=letter

	#To check if there is no dash in the DISPLAY list ,if no dash means the user found the word..
	if "_" not in DISPLAY:
		print("")
		print(f"You found the word {CHOOSEN_WORD} ..")
		COMPLETED=True

	elif GUESS:

		if GUESS==CHOOSEN_WORD:
			print(f"\nWow you got the answer at once {CHOOSEN_WORD}..")
			COMPLETED=True	

		else:
			# If you got the answer at once , it should print like this....
			print(" ".join(DISPLAY))
			print("")

	elif TRIES==0:
	 	print(f"\nYou have exhuated your number of TRIES ,The word was {CHOOSEN_WORD} ..")
	 	COMPLETED=True



# While loop to run the code contineously...
while not COMPLETED:

	hangman()
	











