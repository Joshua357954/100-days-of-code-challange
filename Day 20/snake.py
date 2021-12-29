from turtle import Turtle


class Snake:

	def __init__(self):
		self.segments=[]
		self.xpos=[(0,0),(0,-20),(0,-40)]
		self.create_snake_parts()
		self.head=self.segments[0]
		self.head.color('red')


	def create_snake_parts(self):
		for pos in self.xpos:
			self.make_snake(pos)


	def make_snake(self,position):
		pak=Turtle(shape='square')
		pak.penup()
		pak.goto(position)
		self.segments.append(pak)

	def move(self):
		current_snake_length=len(self.segments)-1

		for snake_p in  range(current_snake_length, 0, -1):

			x=self.segments[snake_p-1].xcor()

			y=self.segments[snake_p-1].ycor()

			self.segments[snake_p].goto(x=x,y=y)
		self.head.forward(20)

	def reset(self):
		for seg in self.segments:
			seg.goto(10000,-10000)
		self.segments.clear()
		self.create_snake_parts()
		self.head=self.segments[0]
		self.head.color('red')

	def left(self):
		if self.head.heading() !=0:
			self.head.setheading(180)

	def right(self):
		if self.head.heading() !=180:
			self.head.setheading(0)

	def up(self):
		if self.head.heading() !=270:
			self.head.setheading(90)

	def down(self):
		if self.head.heading() !=90:
			self.head.setheading(270)

	def add_snake(self):
		new_pos=self.segments[-1].position()
		self.make_snake(new_pos)