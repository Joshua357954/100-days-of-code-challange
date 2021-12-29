# The final project of the dictionary class and its nesting ....


bid_list={}
# This is the mechanism to keep the while loop moving ....
finish_bid=False

def bid_me():
	global finish_bid
	name=input("Please enter your name : ")
	bid=input("Enter your bid : $")

	# This add the name and bid as key and value pairs in the dictionary...
	bid_list[name]=bid

	again=input("\nDo we still have any bidders 'y' or 'n' : ")
	if again =="y":
		bid_me()
	else:
		finish_bid=True

def highest_bid():
	global bid_list
	if bid_list:

		# This is to get the highest number out of the values of the dict in the list
		high_bid_num=max([bid_list[score] for score in bid_list])

		# This is to get the bidder through the high_bid_number
		high_bider= [k for k,v in bid_list.items() if v== high_bid_num]

	return f"\nThe highest bidder is  {high_bider[0]} with ${high_bid_num}"

while not finish_bid:

	bid_me()
	if finish_bid :
		print(bid_list)
		print(highest_bid())














