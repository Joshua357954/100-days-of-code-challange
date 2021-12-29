from os import system,name
# This is the way the secret auction is done by angela .....

bid_list={}

finished_bid=False
print("----------------------------------SECRET AUCTION BID---------------------------------------------")

def bid_me(bid_record):
	highest_bid=""
	winner=""
	for bidder in bid_record:
		bid_amount=bid_record[bidder]
		if bid_amount> highest_bid:
			highest_bid=bid_amount
			winner=bidder

	return f"\nThe winner of the bid is {winner} with bid of ${highest_bid}"

while not finished_bid:

	nama=input("\nEnter your name : ")
	price=input("Enter your bids : $")
	bid_list[nama]=price

	again=input("\nDo we still have any bidders 'y' or 'n' ")
	if again == 'n':
		print(bid_me(bid_list))
		finished_bid=True
	else:
		if name=='nt':
			system('cls')









