from model import Questions
from quest import quests
from os import system

system('cls')
score=0

for num,QUEST in enumerate(quests):
	question1=Questions(question=QUEST['question'],answer=QUEST['answer'])

	choice=input(f"Q{num+1}. {question1.question} \nTrue/False : ")

	if choice.lower()==question1.answer.lower():
		print("\nYo ,you got it right ...")
		score+=1


	else:
		print("\nAwww, Its wrong ...")
	print(f"The Correct answer is : {question1.answer}")
	print(f'Your Current Score is {score}/{num+1} \n')

