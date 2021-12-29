from os import system
system('cls')
class Quiz:
	'''This class models the Quiz game as a whole (THE ENGINE ROOM)'''
	def __init__(self,q_list):
		self.question_n=0
		self.questions=q_list
		self.score=0

	def remaining_q(self):
		"""This function returns True or False if the question number is less 
		than the length of the question_list it returns False else True...."""

		#print(len(self.questions) > self.question_n)
		return self.question_n < len(self.questions)

	def next_question(self):
		"""This Function increment the self.question number to change the question
		 when the class is instanciated once again ."""

		d_question=self.questions[self.question_n]
		self.question_n+=1

		choice=input(f"Q{self.question_n}. {d_question.question} \nTrue/False : ")
		self.check_answer(choice,d_question.answer)

	def check_answer(self,user_ans,correct_ans):
		"""This function is responsible for checking if the users choice is equal to the correct answer
		 which is the questions.answer, and prints wether the user is right or wrong ..."""

		if user_ans.lower()==correct_ans.lower():

			print("\nWow You got the answer ...")
			self.score+=1
		else:
			print("\nAww, You got it Wrong ...")
		# This will run after the if and else block...
		print(f"The correct answer is : {correct_ans.upper()}")
		print(f"Your currrent score is {self.score}/{self.question_n}")
		print("\n")


