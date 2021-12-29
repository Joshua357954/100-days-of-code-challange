# This is the day 31 of the 100 days of code 

# Project Flash card to learn french (french to english ...)
import tkinter 
from tkinter import *
from  PIL import Image,ImageTk
import pandas
import random

root=Tk()
root.config(bg="white")
root.title("Flash Card")
root.minsize(width=600,height=500)


#========== Words Iniialization ============
try:
	new_words=pandas.read_csv('words_to_learn.csv')
except:
	new_words=pandas.read_csv('french_to_eng.csv')
	word_dict=new_words.to_dict(orient='records')
else:
	word_dict=new_words.to_dict(orient='records')

current_word={}
TIMER=None
greetings=["Wow","Nice","Awesome","Great","Superb"]
def next_word():
	global current_word,TIMER
	root.after_cancel(TIMER)
	try:
		current_word=random.choice(word_dict)
	except:
		canvas.itemconfig(W_IMG,image=IMAGE1)
		canvas.itemconfig(text1,text=random.choice(greetings),fill='black')
		canvas.itemconfig(text2,text="You've Learnt All Words...",fill='purple')
	else:
		canvas.itemconfig(W_IMG,image=IMAGE1)
		canvas.itemconfig(text1,text='French',fill='black')
		canvas.itemconfig(text2,text=current_word['French'],fill='black')
		TIMER=root.after(1000,flip_card)

def flip_card():
	canvas.itemconfig(W_IMG,image=IMAGE2)
	canvas.itemconfig(text1,text='English',fill='white')
	canvas.itemconfig(text2,text=current_word['English'],fill='white')


def Known_words():
	global word_dict
	try:
		word_dict.remove(current_word)
		print(len(word_dict))
		new_frame=pandas.DataFrame(word_dict)
		new_frame.to_csv("words_to_learn.csv",index=False)
		next_word()
	except:
		print("Already Known")


#========== Images Setup ================

im1=Image.open('w_card.png')
res_im1=im1.resize((320,300))
IMAGE1=ImageTk.PhotoImage(res_im1)
#===================================
im2=Image.open('red.png')
res_im2=im2.resize((320,300))
IMAGE2=ImageTk.PhotoImage(res_im2)
#===================================
im3=Image.open('bad.png')
res_im3=im3.resize((100,100))
BAD=ImageTk.PhotoImage(res_im3)
#===================================
im4=Image.open('good.png')
res_im4=im4.resize((100,100))
GOOD=ImageTk.PhotoImage(res_im4)

#+=================================
TIMER=root.after(1000,flip_card)

canvas=Canvas(width=340,height=340,bg='white')
W_IMG=canvas.create_image(170,170,image=IMAGE1)
text1=canvas.create_text(175,110,text="French",font=("sans serif",20,'bold'))
text2=canvas.create_text(170,190,text="Word",font=("sans serif",17,'italic'))
canvas.pack()

frame=Frame(bg='white')
frame.pack(pady=10)
#============= Button Frame ==========

bad_button=Button(frame,image=BAD,command=next_word)
bad_button.grid(row=0,column=0,padx=50)

good_button=Button(frame,image=GOOD,command=Known_words)
good_button.grid(row=0,column=2,padx=50)

next_word()

root.mainloop()
