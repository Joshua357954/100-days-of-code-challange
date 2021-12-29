from os import system ,name
# This is the calculator project of the 100days of code.., we learn about dictionaries ,recursoin ,return statement,while loop and many others


def add(num1,num2):
	return num1+num2

def subtract(num1:int,num2:int ):
	return num1-num2

def divide(num1,num2):
	return num1/num2

def multiply(num1,num2):
	return num1*num2

def power(num1,num2):
	return num1**num2

operations={
	"+":add,
	"-":subtract,
	"*":multiply,
	"/":divide,
	"^":power
}

def calculate_me():
	system('cls')
	print("\n ---------------------------- Pythonista Calculator ,basic but complex.. ----------------------------------------- \n")

	num1=float(input("Enter the first number : "))

	for i in operations:
		print(i)
	again=True

	while again:

		operation=input("Enter operation : ")
		num2=float(input("Enter the next number : "))

		
		function=operations[operation]
		answer=function(num1,num2)
		print(f"\n{num1} {operation} {num2}  =  {answer} \n")

		ch_again=input(f"\nDo you want to continue calculating with {answer},\n 'Y' or 'N' to start afresh  ,Enter 'S' to stop :  ")
		
		if ch_again.lower() =="y":
			num1=answer

		elif ch_again.lower()=='s': 
			again=False
			print("\n Ok dude am dome ... :)")

		else:
			again=False
			calculate_me()
calculate_me()



