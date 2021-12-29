#This is project 5 of the 100 days of code....

# random password generator
import string
import random 

alphabet=string.ascii_lowercase
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=string.punctuation

def random_password(length="",num="",sym=1):
	passw=""
	for _ in range(length):
		passw+=random.choice(alphabet)

	for _ in range(num):
		ran_num=random.choice(numbers)
		passw+=str(ran_num)

	for _ in range(sym):
		ran_sym=random.choice(symbols)
		passw+=str(ran_sym)
	
	x=list(passw)
	random.shuffle(x)

	new_pass="".join(x)

	return new_pass

l=int(input("How many letters do you want in the password : "))
n=int(input("How many numbers do you want in the password : "))
s=int(input("How many symbol do you want in the password : "))

print("")
d_password=(random_password(l,n,s))

print(f"Your Password is  {d_password}")





























