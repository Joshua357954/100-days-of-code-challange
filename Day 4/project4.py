
# This is the day four project 

import random


choose=['rock','paper','scissors']


player=int(input("Choose one , 0 Rock 1 Papaer 2 scissors :\n"))
if player <=2:
	print(f"{choose[player]}\n")


computer=random.randint(0,2)
print(f"computer choosed , {choose[computer]}\n")

if player >=3 or player < 0:
	print("invalid input, try again  ... ")

elif player == computer:
	print("A Draw....\n")


# The main logic.....
elif player==0 and computer==2:
	print("You loose..")

elif computer==0 and player==2:
	print("You loose..")

elif computer > player:
	print("You loose")

elif player > computer:
	print("You win")

else:
	print("Pls enter a valid input.....")




