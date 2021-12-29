# This is the encryption,decryption(ceaser cipher) project of the 100days of code...
import random
import string

numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=list(string.punctuation)
alpha=list(string.ascii_lowercase)
space=[" "]

alphabet=alpha+space+numbers+symbols+alpha+space+numbers+symbols

print("\n---------------------------WELCOME TO ENCRYPT AND DECRYPT ---------------------------------------\n")

completed=False


# This function consists of deceypt and encrypt........

def ceaser_cipher(word,shift,direction):
	global alphabet
	end_text=""

	for letter in word:

		pos=alphabet.index(letter)

		if direction=="d":
			new_pos=pos-shift
		else:
			new_pos=pos+shift

		new_letter=alphabet[new_pos]

		end_text+=new_letter

	print(f"\nThe {direction} text is {end_text} \n")


# To add continuity to the function to keep performing our task...
while not completed:

	encrypt_or_decrypt=input("Do you want to encrypt or decrypt : ")

	w=input("Enter the word : ")

	s=int(input("Enter shift  number : "))

	ceaser_cipher(word=w,shift=s,direction=encrypt_or_decrypt)

	again=input("Do you want to go again : ")

	if again =="yes":
		print("")
	else:
		completed=True












# encrypt function

# def encrypt(word,shift,e_or_d=""):
# 	global alphabet,symbol,number
# 	com=""
# 	for i in word:

# 		pos=alphabet.index(i)
# 		new_pos=pos+shift
# 		com+=alphabet[new_pos]
# 	return com




# # decryption function

# def decrypt(word,shift):
# 	global alphabet,number,symbol
# 	wod=""
# 	for i in word:
# 		pos=alphabet.index(i)
# 		new_pos=pos-shift
# 		wod+=alphabet[new_pos]

# 	return wod

# input

# while not c:

# 	ed=input("Do you want to encrypt or decrypt : ")

# 	if ed =='encrypt':
# 		w=input("Enter the word to encrypt : ")
# 		s=int(input("Enter word shift : "))
# 		print(encrypt(w,s))

# 	elif ed=="decrypt":
# 		w=input("Enter the word to decrypt : ")
# 		s=int(input("Enter word shift : "))
# 		print(decrypt(w,s))

# 	else:
		#c=True

