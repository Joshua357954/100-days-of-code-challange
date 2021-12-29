
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=list(string.punctuation)
alpha=list(string.ascii_lowercase)
space=[" "]

alphabet=alpha+space+numbers+symbols+alpha+space+numbers+symbols

print(alphabet)



window=Tk()

window.title("CEASER CIPHER")
window.geometry("300x400")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR)

# ------------------- FUNCTION -----------------------

def cipher(*args):
	global alphabet
	end_text=""

	word=ent.get()
	shift=ent2.get()


	for letter in word:

		pos=alphabet.index(letter)

		if args[0]=="decrypt":
			new_pos=pos-shift
		else:
			new_pos=pos+shift

		new_letter=alphabet[new_pos]

		end_text+=new_letter