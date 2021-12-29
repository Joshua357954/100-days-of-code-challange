# This is the day 27 of the  100 days of code ,
# Topic Tkinter and more about functions ...

# Miles to kilometers project

import tkinter 
from tkinter import *

FONT=('Sans serif',15,'bold')
FONT2=('Ariel black',11,'italic')



def convert():
	try:
		current_n=int(e1.get())*1.609
	except:
		print("Invalid")
	else:
		new_num= round(current_n,1)
		l2.config(text=f'{new_num}km')
	finally:
		e1.delete(0,END)
		e1.insert(0,0)

root=Tk()
root.title("Miles To Km Convert")
root.minsize(width=300,height=200)

l1=Label(text="Miles to Km",font=FONT).pack(side='top')

en1=IntVar()
e1=Entry(textvariable=en1,width=6,font=FONT,relief=SOLID)
e1.pack()

l2=Label(text="0 Km",font=FONT2)
l2.pack(pady=10)


b1=Button(text="Convert",font=FONT2,activebackground='lightgreen',command=convert)
b1.pack()




root.mainloop()
