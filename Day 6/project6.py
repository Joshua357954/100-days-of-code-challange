# This is the 6th project of the 100 days of code..

# using a while loop with  a function


import string

stop_me =False

alpha=string.ascii_lowercase

num=0


def do_string():
	global alpha,num

	if num ==26:
		stop_me=True

	else:
		print(alpha[num])
		num+=1

	


while stop_me== False:
	
	do_string() 



























