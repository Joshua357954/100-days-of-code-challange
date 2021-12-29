# The day 28 of the 100day of code 
# Creating a pomodoro app for time management
import tkinter 
from tkinter import *
from  PIL import Image,ImageTk
import math
#===================== UI CONSTANTS =====================================
TITLE='Pomodoro'.title()
FONT=('comic sans ms',30,'bold')
FONT2=('Sans serif',35,'bold')
COLOR1='lightgreen'
COLOR2='white'
COLOR3='#FE8F8F'
COLOR4='#FFEDD3'

#==================== FUNCTIONAL CONSTANTS =============================
WORK=1
LONG_BREAK=1
SHORT_BREAK=.5
k_c=1
TIMER=None

#================== FUNCTION =================================
def reset_timer():
	global k_c
	root.after_cancel(TIMER)
	header.config(text="TIMER",fg='greenyellow',font=('comic sans ms',30,'bold'))
	canvas.itemconfig(time_text,text='00:00')
	k_c=1


def run_time():
	global k_c
	



	if k_c % 8==0:
		header.config(text="LONG BREAK",fg='lightgreen',font=('comic sans ms',30,'bold'))
		start(LONG_BREAK*60)
		
	elif k_c % 2==0:
		header.config(text="SHORT BREAK",fg='lightblue',font=('comic sans ms',30,'bold'))
		start(SHORT_BREAK*60)
		
	else:
		header.config(text="WORK",fg='red',font=('comic sans ms',30,'bold'))
		start(WORK*60)

	k_c+=1

def start(count):
	
	hours=math.floor(count/60)
	minute=math.floor(count%60)

	if minute<10:
		minute=f'0{minute}'

	fine_time=f"{hours}:{minute}"
	canvas.itemconfig(time_text,text=fine_time)

	if count <1:
		# once a paticular count is finished ,call run_time function to start another counter
		run_time()

	if count>0:
		global TIMER

		TIMER=root.after(1000,start , count-1)




root=Tk()
root.title(TITLE)
root.config(bg=COLOR3)
root.minsize(100,300)


header=Label(text='TIMER',font=FONT,width=30,fg=COLOR1,bg=COLOR3)
header.pack(pady=20)


#=========== Image ============
img=Image.open('tomatoes.png')
new=img.resize((300,300))
new_img=ImageTk.PhotoImage(new)
#==============================

canvas=Canvas(width=500,height=400,bg=COLOR3,highlightthickness=0)

canvas.create_image(250,233,image=(new_img))
time_text=canvas.create_text(250,250,text="00:00",font=FONT2,fill=COLOR2)
canvas.pack()


start_button=Button(text='Start',font=("sans serif",12,'bold'),bg=COLOR3,fg=COLOR4,command=run_time)
start_button.place(x=560,y=200)

reset_button=Button(text="reset",font=("sans serif",12,'bold'),bg=COLOR3,fg=COLOR4,command=reset_timer)
reset_button.place(x=100,y=200)

# TOdo list
# make a count down function with windows .after method
# make another function to call the count down function with the time as argument
# configure the text
# make a variable to hold the number of times each will run
# configure the header text with the specific pomodoro name 



root.mainloop()