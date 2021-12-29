
# Hangman game

print("-------- Hangman -------------")

word="joshua"

display=[]


completed=False

tries=6

def hang():	

	global completed,tries

	print(f"You have {tries} tries...")

	guess=input("Guess the word : ")

	for letter in word:

		if guess == letter:
			display.append(guess)
			
			if letter.lower() in display:

				print(letter.upper(),end=" ")

		else :
			tries-=1
			print("_",end=" ")

	print("\n")


	# Check if the player has won..
	check_word="".join(display)

	if check_word == word:
		print("Hey you found the word...")
		completed=True

	if tries <= 0:
		print(f"\n You've run out of tries....The word is {word}\n")
		completed=True

while not completed:
	hang()





















