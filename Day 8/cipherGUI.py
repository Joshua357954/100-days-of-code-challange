
from tkinter import *
import random 
import string
from tkinter import filedialog
from tkinter import messagebox
#import pyperclip

BACKGROUND_COLOR='#c9c9c9'

numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=list(string.punctuation)
alpha=list(string.ascii_lowercase)
space=[" "]

alphabet=alpha+space+numbers+symbols+alpha+space+numbers+symbols


window=Tk()

window.title("CEASER CIPHER")
window.geometry("600x500")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR)

# ------------------- FUNCTION -----------------------

def open_text():
	text=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])

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

		end_text+=alphabet[new_pos]

	label1.config(text=f"{args[0]} : {end_text}")




# ----------------- UI SETUP ----------------------------
label1=Label(window,text="Encrypt / Decrypt	",font=('comic sans ms',15),bg=BACKGROUND_COLOR)
label1.pack(pady=12)


ent=StringVar()
entry_box=Entry(window,textvariable=ent,relief=SOLID,font=('Ariel',16),width=15).pack(pady=40)

ent2=IntVar()
entry_box2=Entry(window,textvariable=ent2,relief=SOLID,font=('Ariel',16),width=3).place(x=420,y=98)

encrypt_button=Button(window,text="Encrypt",font=('comic sans ms',14),command=lambda :cipher("encrypt")).pack(pady=20)


decrypt_button=Button(window,text="Decrypt",font=('comic sans ms',14),command=lambda :cipher("decrypt")).pack(pady=20)

File_button=Button(window,text="Encrypt text file",font=('comic sans ms',14),command=open_text).place(x=100,y=370)

File_button2=Button(window,text="Decrypt text file",font=('comic sans ms',14),command=open_text).place(x=300,y=370)

file_label=Label(window,text="No file yet..",font=('comic sans ms',15),bg=BACKGROUND_COLOR)
file_label.place(x=200,y=430)





window.mainloop()












