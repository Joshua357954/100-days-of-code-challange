from turtle import Turtle 


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score=0
		with open("dta.txt")as sc:
			self.high_score=int(sc.read())
		self.color('black')
		self.hideturtle()
		self.penup()
		self.goto(0,200)
		self.writer()

	def game_over(self):
		self.goto(0,0)
		self.write("Game Over",align='center',font=('courier',25,'normal'))

	def writer(self):
		self.clear()
		self.write(f"Score : {self.score}    High Score : {self.high_score}",align='center',font=('comic sans ms',25,'normal'))
	
	def add_score(self):
		self.score+=1
		self.writer()

	def reset_score(self):
		if self.score>self.high_score:
			self.high_score=self.score
			with open("dta.txt",mode='w')as ws:
				ws.write(f'{self.score}')
		self.score=0
		self.writer()