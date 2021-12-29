
# This is the day three project done on the 16 of october 2021


# Todo 1

'''
There is a cross road , do you want to follow left  or right


if you follow left you will see an island , enter swim to cross

ones you cross there are three houses  on with fire,gold,wild animals



if you follow right there is an underground tunnel , enter dig to start diging 

you have dug three holes on full of ants ,silver,ground snakes



'''

print("..............Welcome to treasure  island.......................")


print("Your mission is to find the treasure.")
print("")

cross_road=input("There is a cross road , do you want to follow left or right :\n ")
print("")

if cross_road=="left":
	
	iland=input("There is an island enter swim to cross : ")
	print("")
	
	if  iland.lower() =="swim".lower():
		crossed_island= input("You have just crossed the island , there are three houses red, green ,blue choose one to enter : ")
		print("")

		if  crossed_island=="red":
			print("You have just entered the house and it is filled with diamodns ,\n You have found the treasure...")
		
		elif cross_road.lower()=="blue":
			print(" You have entered the house and it is field with wild animals , You loose")

		elif cross_road.lower()=="green":
			print(" You have just entered the house and it is filled with fire.... ,You loose")
		
		else:
			print("Invalid input , You loose")

	else:
		print("You have drowned inside the river.....")

elif cross_road=="right":
	print("")

	tunnel=input("There is a tunnel here enter 'go' to enter it safely: ")
	print("")

	if tunnel.lower() == 'go':
		entered_tunnel=input("You have just entered the turnnel enter 'dig' to start finding the treasure : ")
		print("")

		if entered_tunnel.lower() == "dig":
			
			finished_dig=input("You have successfully dug three dip hole one is dip,dipper,dippest choose one : ")
			
			if  finished_dig.lower()=="dip":

				print("You just entered the dip hole and it is full of ants, You loose..")

			elif finished_dig.lower()=="dipper":
				print(" You just entered the dipper hole and has gold in it ,You win ")

			elif finished_dig.lower()=="dippest":
				print(" you just entered the dippest hole and it is filled with ground snakes, You loose")

			else:
				print("You could not choose a hole , You loose......")

		else:
			print("You cannot dig and find the treasure , You loose")

	else:
		print("You have just fallen into the turnnel ,  You loose...")


else:
	print("The input you gave is invalid..")











