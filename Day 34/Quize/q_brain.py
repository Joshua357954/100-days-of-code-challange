


class QBRAIN:
	def __init__(self,q_list:list):
		self.q_list=q_list
		self.q_num=0
		self.current=self.q_list[self.q_num]


	def still_has_questions(self)-> bool:
		if self.q_num < len(self.q_list):
			return True

	def next_question(self):
		self.current=self.q_list[self.q_num]
		current_q=self.current.question
		return current_q
		

	def check_answer(self,user_answer):
		TOF=None
		if user_answer==self.current.answer:
			TOF=True
		self.q_num+=1
		return TOF
		