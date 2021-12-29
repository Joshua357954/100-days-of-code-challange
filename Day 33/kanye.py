from tkinter import *
import tkinter
import requests

FONT=("Comic sans ms",14,"normal")

root=Tk()
root.title("Kanye Quote")
root.minsize(300,400)


def get_quote():
	try:
		res=requests.get('https://api.kanye.rest').json()
		real_quote=res['quote']
		canvas.itemconfig(quote_text,fill='black',text=f'             🌊 \n{real_quote}')
	except:
		canvas.itemconfig(quote_text,fill='yellowgreen',text=f'             🌊 \nPlease Check your internet connection and try again.')
		#https://api.kanye.rest


canvas=Canvas(width=200,height=240,bg="lightgray")
quote_text=canvas.create_text(100,100,text="🌊 My Quote ...",font=FONT,width=190)
canvas.pack(pady=10)

gob=Button(text='Search New',bd=1,bg='lightblue',font=("Sans serif",15,'bold'),command=get_quote)
gob.pack(pady=20)


get_quote()

looper=mainloop()
root.looper