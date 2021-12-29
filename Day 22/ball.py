from turtle import Turtle


class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.penup()
		self.move_x=10
		self.move_y=10
		self.color("pink")
		self.shape("circle")
		self.speed(10)
		self.goto(0,0)


	def move(self):
		self.goto(self.xcor()+self.move_x,self.ycor()+self.move_y)
		print(f"x : {self.xcor()} , y : {self.ycor()}")

	def bounce_y(self):
		self.move_y *= -1
		
	
	def bounce_x(self):
		self.move_x  *= -1	
			