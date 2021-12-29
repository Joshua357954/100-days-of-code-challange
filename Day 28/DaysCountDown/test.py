# from  datetime import datetime
# import time
# mk=datetime.now().strftime('%Y:%B:%X:%A:%H:%M:%S')

# dm=divmod(3,2)


# What I learnt from NuralNine's countdown tutorial (off hand)


import tkinter
from threading import *
from tkinter import *
from time import sleep

END_LOOP=False
TITLE="S 2 D C"

def looper():

	global END_LOOP

	END_LOOP=False

	sec,_min,hours=0,0,0

	string=ent.get().split(':')

	if len(string)==3:
		sec=int(string[0])
		_min=int(string[0])
		hours=int(string[0])

	elif len(string)==2:
		sec=int(string[0])
		_min=int(string[1])

	elif len(string)==1:
	 	sec=int(string[0])

	else:
		print("Invalid format ...")

	all_seconds=hours*3600+_min*60+sec

	print(hours,_min,sec)

	while all_seconds>0 and not END_LOOP:
		sleep(1)
		all_seconds-=1

		_min,sec=divmod(all_seconds,60)
		hours,_min=divmod(_min,60)
		days,hours=divmod(hours,24)

		root.update()

		combo=f"   {days:02d}  :   {hours:02d} :  {_min:02d}  :  {sec:02d}\n Days  Hrs  Min Secs"

		show_label.config(text=combo)

	show_label.config(text="00:00:00:00")

def stop_t():

	global END_LOOP
	END_LOOP=True


def start_t():
	Thread(target=looper())

root=Tk()
root.title(TITLE)
ent=Entry(font=("Helvetica",13,'normal'))
ent.pack()

start_b=Button(text='start',font=("Helvetica",13,'normal'),command=start_t)
start_b.pack()

end_b=Button(text="stop",font=("Helvetica",13,'normal'),command=stop_t)
end_b.pack()


show_label=Label(text="00:00:00:00",font=("Helvetica",13,'normal'))
show_label.pack(pady=10)

root.mainloop()









