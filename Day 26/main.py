# This is the day 26 of the 100days of code 


# let='Alfa,Bravo,Charlie,Delta,Echo,Foxtrot,Golf,Hotel,India,Julliet,Kilo,Lima,Mike,November,Oscar,Papa,Quebec,Romeo,Serria,Tango,Uniform,Victor,Whisky,Yankee,Zulu'
# print(let.split(','))
# ma=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
# wod=['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Julliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Serria', 'Tango', 'Uniform', 'Victor', 'Whisky', 'Yankee', 'Zulu']

import pandas

ma=pandas.read_csv('nato_words.csv')


# for index,row in ma.iterrows():
# 	print(row.word)

# 1 conver to csv to a python dictionary with dictionary comprehension 
# 2 loop through the users word and get the value of the users letter from the converted csv file

user_word='Angela'

nato_dict={item.letter:item.word for index,item in ma.iterrows()}

output=[nato_dict[letter] for letter in user_word.upper()]

print(output)




