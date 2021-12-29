# Quize with gui | words from an external api
from data import quests
from q_model import QMODEL
from q_brain import QBRAIN
from GUI import MyGUI
import html
# Fetch all the data
# parse the data 
# for every itteration store the quize object  in a list
# pass the list to the quize brain object
ALL_Q=[]

for items in quests:
	new_obj=QMODEL(question=html.unescape(items['question']),answer=items['correct_answer'])
	ALL_Q.append(new_obj)

QUIZE=QBRAIN(ALL_Q)

MyGUI(QUIZE)
	