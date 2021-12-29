import turtle
from turtle import *
import pandas
WIDTH=700
HEIGHT=400
TITLE='States guessing game'
COLOR="yellow"
FONT=("Sans Serif",20,"normal")
IMAGE='map_of_nigeria.gif'
# Screen setup
screen=Screen()

screen.title(TITLE)
screen.bgcolor(COLOR)

# Top Heading
writer=Turtle()
writer.hideturtle()
writer.penup()
writer.goto(x=0,y=160)
writer.write("State Guessing Game",align='center',font=FONT)

screen.addshape(IMAGE)

turtle.shape(IMAGE)


data=pandas.read_csv('states_in_nigeria.csv')

# print(len(N_N))

# def get_mouse_click_coor(x,y):
# 	global i
# 	print
# 	if i <35 or i==35:
# 		print(N_N[i],x,y)
# 		i+=1



guessed_state=[]

all_states=data['State'].to_list()


while len(guessed_state)<37:
	try:
		user_choice=textinput(f'{len(guessed_state)}/36',"Enter a state ").title()
	except:
		print("Game Over ....")
	else:

		if user_choice not in guessed_state and user_choice in all_states:
			guessed_state.append(user_choice)
			tut=Turtle()
			tut.hideturtle()
			tut.penup()

			new_row=data[data['State']==user_choice]

			# goto
			tut.goto(float(new_row.X),float(new_row.Y))
			# write
			tut.write(new_row.State.item())

		elif user_choice=="Exit" or user_choice=="E":

			missing_s={"Missing":[item for item in all_states if item not in guessed_state]}
			
			df=pandas.DataFrame(missing_s)

			df.to_csv(f"Missing_{len(missing_s['Missing'])}_States ")

			exit(0)

	finally:

		pass


screen.mainloop()

# get hold of the user choice row
# append it to guessed state
# create an instance of the turtle module to write
# go to the x and y position of the specific state.