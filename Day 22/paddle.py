from turtle import Turtle 


class Paddle(Turtle):
	def __init__(self,position):
		super().__init__()

		self.x_score=0
		self.y_score=0
		self.shape('square')
		self.shapesize(5,1)
		self.penup()
		self.speed(0)
		self.goto(position)


	def move_up(self):
		new_y=self.ycor()+10
		self.goto(self.xcor(),new_y)

	def move_down(self):
		new_y=self.ycor()-10
		self.goto(self.xcor(),new_y)
















