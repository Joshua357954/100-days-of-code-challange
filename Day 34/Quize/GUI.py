from tkinter import *
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox

BACKGROUND_COLOR='lightgray'

class MyGUI:

	def __init__(self,Quize:object):
		self.root=Tk()
		self.root.minsize(350,450)
		self.root.config(background=BACKGROUND_COLOR)
		self.root.title("My Quize App")
		self.QUIZE=Quize
		self.score=0

		#===================================
		im3=Image.open('../bad.png')
		res_im3=im3.resize((100,100))
		self.BAD=ImageTk.PhotoImage(res_im3)
		#===================================
		im4=Image.open('../good.png')
		res_im4=im4.resize((100,100))
		self.GOOD=ImageTk.PhotoImage(res_im4)
		#===================================

		self.lab=Label(text='Score : 0',font=("Ariel",12,'normal'),bg=BACKGROUND_COLOR)
		self.lab.pack(padx=(150,0),pady=(10,0))

		self.canvas=Canvas(width=300,height=230,bg='white')
		self.show_text=self.canvas.create_text(150,100,text="The words to display",
								width=280,
								font=("Sans serif",13,'normal'))

		self.canvas.pack(pady=10,)

		#================= Buttons =============
		self.frame=Frame(bg=BACKGROUND_COLOR)
		self.frame.pack(pady=(10,0))

		self.b1=Button(self.frame,image=self.GOOD,command=lambda :self.check_answer("True"))
		self.b1.grid(row=0,column=0,padx=(0,45))

		self.b2=Button(self.frame,image=self.BAD,command=lambda :self.check_answer("False"))
		self.b2.grid(row=0,column=3,padx=(45,0))
		#======================================

		self.next_question()

		self.root.mainloop()

	def next_question(self):
		self.canvas.config(bg='white')
		if self.QUIZE.still_has_questions():
			
			current_text=self.QUIZE.next_question()

			self.canvas.itemconfig(self.show_text,text=current_text)
		else:
			self.root.after(2500,self.total)

	def check_answer(self,user_a):

		if self.QUIZE.still_has_questions():

			if self.QUIZE.check_answer(user_a):# if user ans passed to check ans method True
				self.correct_ans()
			else:
				self.canvas.config(bg='red')

			self.root.after(1000,self.next_question)

	def correct_ans(self):
		self.score+=1
		self.canvas.config(bg='lightgreen')
		self.lab.config(text=f"Score : {self.score}")

	def total(self):
		message=(f"You Got A Total of {self.score} out of {len(self.QUIZE.q_list)} Questions")
		messagebox.showinfo("Hello",message)
		self.score=0
		self.lab.config(text=f"Score : {self.score}")
		self.canvas.itemconfig(self.show_text,text=f"QUIZE ENDED\n\nTotal Score : {self.score}/{len(self.QUIZE.q_list)}",font=('Comic sans ms',13,"normal"))
