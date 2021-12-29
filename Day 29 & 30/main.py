# This is the Day29 0f the 100 days of code ...

# Making a password manager ...


from tkinter import *
import tkinter
from PIL import Image ,ImageTk
from string import ascii_lowercase,punctuation
import random
from tkinter import messagebox 
import kivy
import json
from kivy.core.clipboard import *
rik=None
#=============== Functions ================
# def new_top():
# 	global rik
# 	rik=Toplevel()
# 	rik.geometry("100x100")
# 	rik.overrideredirect(2)
# 	rik.title("Do you want ?")
# 	l1=Label(rik,text='Joshua label')
# 	ent=Entry(rik).pack()
# 	b1=Button(rik,text="click me",command=lambda : rik.destroy()).pack()


def random_password():
	alphabet=list(ascii_lowercase)
	numbers=[1,2,3,4,5,6,7,8,9,0]
	symbols=list(punctuation)

	alpha=[random.choice(alphabet) for alpha in range(random.randrange(6,8))]
	num=[random.choice(numbers) for num in range(random.randint(2,3))]
	sym=[sym for sym in range(random.randrange(2,3))]

	x=alpha+num+sym
	random.shuffle(x)
	net=[str(n) for n in x ]

	new_pas="".join(net)

	return new_pas

def make_search():
	name=website.get().title()

	if name !="":
		with open("Website&Pass.json","r")as data:
			new_data=json.load(data)
			if name in new_data:

				web=new_data[name]
				n_email=web['email']
				n_pass=web['password']
				Clipboard.copy(f"{name} , {n_email} , {n_pass}")
				messagebox.showinfo(name.title(),f"Credentials found :\nWebsite : {name}\nEmail : {n_email}\nPassword : {n_pass}")

			else:
				messagebox.showinfo("Not Found",f"No Website found for {name}")


def write_to_file(website,email,password):
	global rik
	# open file and append to it 
	# with open("website_password.txt",mode="a")as file:
	# 	file.write(f"{website} | {email} | {password}\n")
	new_file={
		website.title():{
			"email":email,
			"password":password,
		}
	}

	try:
		with open("Website&Pass.json","r")as data:
			new_data=json.load(data)
			new_data.update(new_file)
		with open("Website&Pass.json","w")as data:
			json.dump(new_data,data,indent=4)
	except:
		print("Camae here...")
		with open("Website&Pass.json","w")as data:
			json.dump(new_file,data,indent=4)


def create_password():
	
	wb=website.get().title()
	em=email.get()
	pa=password.get()

	if len(wb)>=4 and len(em)>=5 and len(pa)>8:

		with open("Website&Pass.json")as data:
			new_data=json.load(data)

			if wb in new_data :
				messagebox.showinfo("Alert..","This website name already exists \n\nTry adding an index to make it unique")
			else:
				if messagebox.askyesno("Hello guys",f"Do you want to save this data : \nwebsite : {wb}\nemail : {em}\nPassword : {pa}"):
					write_to_file(website=wb,email=em,password=pa)
					website.delete(0,END)
					password.delete(0,END)
				else:
					return
	else:
		messagebox.showinfo("Alert","Please fill all the empty fields and try again..")

def generate_password():
	_pass=random_password()
	password.delete(0,END)
	password.insert(0,_pass)
	Clipboard.copy(_pass)
# ===========================================

TITLE="Password MG"

#===============================
root=Tk()
root.title(TITLE)
root.minsize(400,400)
#===============================

#============ IMAGE ============
IMG=Image.open('pas-img.png')
RES=IMG.resize((150,150),)
IMAGE=ImageTk.PhotoImage(RES)

#==============================

#=========== FONT ===========
LABEL_FONT=('comic sans ms',12,"bold")
BUTTON_FONT=('Sans serif',12,'bold')
ENTRY_FONT=("Ariel",11,'bold')

#============================
WIDTH=200
HEIGHT=200

canvas=Canvas(width=WIDTH,height=HEIGHT)

canvas.create_image(100,100,image=IMAGE)
canvas.pack()

frame=Frame()
frame.pack()

# Website 
wl=Label(frame,text="Website : ",font=LABEL_FONT).grid(row=0,column=0)

website=Entry(frame,width=20,font=ENTRY_FONT)
website.grid(row=0,column=1,columnspan=2)

# Search button 

s_button=Button(frame,width=7,text="Search",bd=2,highlightcolor='red',font=BUTTON_FONT,command=make_search)
s_button.grid(row=0,column=3)


# Email
el=Label(frame,text="Email : ",font=LABEL_FONT).grid(row=1,column=0)

email=Entry(frame,width=30,font=ENTRY_FONT)
email.insert(0,"boyijoshua72@gmail.com")
email.grid(row=1,column=2,columnspan=3)

# Password
pl=Label(frame,text="Password : ",font=LABEL_FONT).grid(row=2,column=0)

password=Entry(frame,font=ENTRY_FONT)
password.grid(row=2,column=2)

# Generate
generate=Button(frame,text='Generate',bd=1,font=BUTTON_FONT,command=generate_password)
generate.grid(row=2,column=3,padx=(1,0))

# Add_password


add_password=Button(frame,text='Add',width=24,font=BUTTON_FONT,command=create_password)
add_password.grid(row=3,column=2,columnspan=2)








root.mainloop()