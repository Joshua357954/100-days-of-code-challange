from questModel import Question
from data import quests
from quizbrain import Quiz
# Parse the questions and append it to a list 
question_bank=[]

for vals in quests:
	new_question=Question(text=vals['question'],answer=vals['answer'])
	question_bank.append(new_question)

# This is the instanciate the Quiz class  as (quize)
quize=Quiz(q_list=question_bank)

while quize.remaining_q():	

	quize.next_question()

print("All Done ...")
print(f"Your Total score is {quize.score} out of {len(quize.questions)}")