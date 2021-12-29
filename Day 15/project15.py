# This is the 15th project of the 100days of code learning phase..
from os import system,name



MENU={
    "espresso":{
        "ingredient":{"water":50,'milk':10,"coffee":18},
        "cost":1.5
    },

    "latte":{
        "ingredient":{"water":200,"coffee":24,"milk":150},
        "cost":2.5
    },

    "cappuccino":{
        "ingredient":{"water":250,"coffee":24,"milk":100},
        "cost":3.0
    },
}
resources={
    "water":300,
    "milk":11,
    "coffee":100
}

AVAILABLE_CASH=0
ON=True
system('cls')

def process_ingredients(drink,ingredient):
	global resources
	for item in resources:
		if ingredient[item] >= resources[item] :
			print(f"Sorry the is not enoung {item}")
			return False
	return True

def process_coins():
	print("Please slot your money ")
	total=int(input("How many quaters : "))*0.25
	total+=int(input("How many dimes : "))*0.1
	total+=int(input("How many nickels: "))*0.05
	total+=int(input("How many pennies : "))*0.01

	return total

def brew_coffee(drink,user_money):

	global AVAILABLE_CASH

	if user_money>=drink['cost']:

		AVAILABLE_CASH+=drink['cost']

		for item in drink['ingredient']:

			resources[item]=resources[item]-drink['ingredient'][item]

		print(f"You change is {round(user_money-drink['cost'],2)}")

		print(" Please , You can take your coffee...")

	else:
		print("Insufficient amount ,money refunded ....")

while ON:

	order=input("\nWhat do you want espresso,latte,cappaccino : ")

	# ask what they want if report print the available resources from the resource dict
	if order.lower()=="report":
		for item in resources:
			if item !="coffee":
				print(f"\n{item} : {resources[item]}ml")
			else:
				print(f"\n{item} : {resources[item]}g")
		print(f"\nProfit : {AVAILABLE_CASH}\n")

	# if order equals off then turn off the while loop 
	elif order.lower()=="off":
		print("\n Bye ... :)\n")
		ON=False
	elif order.lower() == "espresso" or order.lower()=="cappuccino" or order.lower()=="latte":
		# else ,get the name of the specific drink ...
		drink=MENU[order]

		# process the order,check if the resources is available to brew that cup of coffee
		if process_ingredients(order,drink['ingredient']):
			print("\nResources are available\n")

			# check if the money entered is available to purchase that which is choosen ...
			# brew the coffee.... and deduct the money appropriately...
			brew_coffee(drink,process_coins())
			
	else:
		print("\n Invalid selection ....\n")

		

