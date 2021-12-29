import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from users import Users


FONT1=("comic sans ms",15,"bold")
FONT2=("ariel",12,"normal")
BTN_FONT=("ariel",12,"bold")
YELLOW="lightyellow"
BLUE="lightblue"

class GUI:

	def __init__(self):
		# window setup
		self.window=Tk()
		self.window.minsize(400,500)
		self.window.title("Cheap Flight Club")
		self.cleared_entry=False
		



		self.logo=Label(text="🚁 Cheap Flight Club ",font=FONT1)
		self.logo.pack(pady=10)

		self.frame=Frame()
		self.frame.pack(pady=(50,30))

		self.e1=Entry(self.frame,width=20,relief=SOLID,font=FONT2)
		self.e1.insert(0,"Name")
		self.e1.bind('<KeyRelease>',self.clear_entries)
		self.e1.pack(pady=10)

		self.e2=Entry(self.frame,width=20,relief=SOLID,font=FONT2)
		self.e2.insert(0,"Email")
		self.e2.bind('<KeyRelease>',self.clear_entries)
		self.e2.pack(pady=10)

		self.e3=Entry(self.frame,width=20,relief=SOLID,font=FONT2)
		self.e3.insert(0,"Confirm - Email")
		self.e3.bind('<KeyRelease>',self.clear_entries)
		self.e3.pack(pady=10)

		self.progress=ttk.Progressbar(self.frame,orient="horizontal",length=180, mode="indeterminate")
		self.progress.pack(pady=(30,0))


		self.action=Button(text="Sign Up",command=self.register,activebackground=BLUE,bg=YELLOW,font=BTN_FONT)
		self.action.pack()


		self.window.mainloop()



	def clear_entries(self,e):
		if not self.cleared_entry:
			self.e1.delete(0,END)
			self.e2.delete(0,END)
			self.e3.delete(0,END)

		self.cleared_entry=True

	def register(self):
		name=self.e1.get()
		email1=self.e2.get()
		email2=self.e2.get()

		new_user=Users(name,email1,email2)

		res=new_user.create_new_user()

		if new_user.user_exists():
			err1="Pls this user already esists , try another gmail account ...."
			naame="User"
			messagebox.showinfo(f"Hello {naame if not name else name}",err1)

		elif res :
			msg=f"User has been sucessfully created \n\nEmail : {email2}\n\n Enjoy your cheap flight notification 😊😊😊 "
			messagebox.showinfo(f"Hello {name}",msg)
			self.clear_entries("anything")

		else:
			err2="Pls check you information and try again .\nName must be >=3 \nGmail must be correct \nEmails must not be different ..."
			messagebox.showinfo(f"Hey {'User' if not name else name}",err2)

		



GUI()