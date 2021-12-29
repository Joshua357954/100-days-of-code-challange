from os import system 
system("cls")
MENU={
    "espresso":{
        "ingredient":{"water":50,"coffee":18,'milk':10},
        "cost":1.5
    },

    "latte":{
        "ingredient":{"water":200,"coffee":120,"milk":150},
        "cost":2.5
    },

    "cappuccino":{
        "ingredient":{"water":250,"coffee":24,"milk":100},
        "cost":3.0
    },
}
resources={
    "water":1000,
    "coffee":1000,
    "milk":1110
}

AVAIL_MONEY=0
RUN_AGAIN=True

def process_ingredient(drink, resources):
	finish_process=True
	for item in drink["ingredient"]:
		if  drink["ingredient"][item] > resources[item] :
			print(f"Sorry the is not enoung {item}...")
			finish_process=False

	return finish_process

def process_coin():
	print("Please enter coin...")
	total=int(input("Enter quaters : "))*0.5
	total+=int(input("Enter Nickels : "))*0.2
	total+=int(input("Enter Dimes : "))*0.02
	total+=int(input("Enter Pennies : "))*0.01

	return total

def brew_coffee(drink,user_money):
	global resources,AVAIL_MONEY
	if user_money>=drink['cost']:
		change=round(user_money-drink['cost'],2)
		if not change:
			print("\nYou dont have any change ..")
		else:
			print(f"\nYour change is ${change}")

		AVAIL_MONEY+=drink['cost']

		print("\nYay ,You can take your coffee...\n")

		for each in drink['ingredient']:
			resources[each]-=drink['ingredient'][each]
	else:
		print("\nInsufficient coin entered ,Money refunded ...")





while RUN_AGAIN:

	order=input("\nWhat do you want espresso,cappuccino,latte : ")

	if order=="report":
		print(f"\nWater : {resources['water']}ml")
		print(f"Milk : {resources['milk']}ml")
		print(f"Coffee :{resources['coffee']}g")
		print(f"Profit : ${AVAIL_MONEY}")

	elif order.lower()=="off":
		print("\nGood Bye :) ....")
		RUN_AGAIN=False

	elif order.lower()  in [name for name in MENU]:

		drink=MENU[order]

		if process_ingredient(drink,resources) and brew_coffee(drink,process_coin()):

			print("Done , lets go brew another coffee ...\n")


	else:

		print("Pls Your Order Is Not Available ,Try another one :)")

	
			
			