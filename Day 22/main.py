# This is the day 22 of the 100days of code ...

from turtle import * 
from paddle import Paddle
from ball import Ball
import time
from score_b import Score_B
# constants
WIDTH=800
HEIGHT=450
TITLE='Pong Game'
R_POS=(370,0)
L_POS=(-370,0)
DELAY=0.04
GAME_ON=True

# setup screen 
screen=Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.title(TITLE)
screen.listen()
screen.tracer(0)

# paddles
r_paddle=Paddle(R_POS)

l_paddle=Paddle(L_POS)

# ball 
ball=Ball()

# score board 
score_b=Score_B()

screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")


while GAME_ON:
	time.sleep(DELAY)
	screen.update()
	ball.move()
	

	if ball.ycor()>205 or ball.ycor() <-205:
		ball.bounce_y()
	
	if ball.distance(r_paddle)<20 and ball.xcor()>360  or ball.distance(l_paddle)<20 and ball.xcor()<-360:
		print("Touch")
		ball.bounce_x()

	# right ball miss
	if ball.xcor()>380 :
		print(ball.xcor())
		score_b.l_score+=1
		score_b.update_score()
		ball.bounce_x()
		ball.goto(0,0)

	# left ball miss
	elif ball.xcor()<-380:
		print(ball.xcor())
		ball.bounce_x()
		score_b.r_score+=1
		score_b.update_score()

		ball.goto(0,0)


# move ball 

# calculate score









screen.mainloop()
















