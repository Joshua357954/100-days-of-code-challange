from tkinter import *
import math


DAYS=30

root=Tk()
root.title('Days Countdown ')

def start_count():

	TO_SECONDS=DAYS*86400

	counter(TO_SECONDS)

def counter(count):
	
	
	_DAYS=86400
	H=216000
	M=3600
	S=60

	# days=math.floor((count/86400))
	# HR=(count/3600)
	# hours=math.floor((HR)- (24*(DAYS)-24))

	# _min=math.floor(HR%86400)
	# print(count%86400)

	# _min,sec=divmod(count,60)
	# hours,_min=divmod(_min,60)
	# days,hours=divmod(hours,24)

	# Two
	# sec=math.floor(count%60)
	# _min=count/60

	# hours=_min/60
	# _min=math.floor(_min%60)

	# days=math.floor(hours/24)
	# hours=math.floor(hours%24)


	_min,sec=divmod(count,60)
	hours,_min=divmod(_min,60)
	days,hours=divmod(hours,24)
	weeks,days=divmod(days,7)
	print(weeks)

	print(_min,sec)
	
	time_label.config(text=f'{weeks} : {days :02d} : {hours:02d} : {_min:02d} : {sec:02d}',fg='#FE8F8F',font=("Sams serif",25,'bold'))

	root.after(1000,counter,count-1)


mainlabel=Label(text="Joshua boyi")

time_label=Label(text='0 : 0 : 0 : 0',fg='#FE8F8F',font=("Sams serif",25,'bold'))
time_label.pack(pady=20)

start_button=Button(text="start",font=("comic sans ms",15,'bold'),command=start_count)
start_button.pack()


start_count()














root.mainloop()