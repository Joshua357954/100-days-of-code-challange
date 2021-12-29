# Day 26


# Test 1
# square every number in the list using the list comprehension 
numbers=[1,1,2,3,5,8,13,21,34,55]

# squared_numbers=[num*num for num in numbers]

# print(squared_numbers)



# Test 2 
# sort out the even number out of the list with list comprension

# even_numbers=[num for num in numbers if num %2==0]

# print(even_numbers)



# medium level Test
# check the file1 and file2 and get the common numbers in the 

# file1=open('file1.txt').readlines()
# file2=open('file2.txt').readlines()

# compare_file=[int(c_num) for c_num in file1 if c_num  in file2]
# print(compare_file)



# Learn Dictionary comprension
dom={
	"josh":"boyi",
	"daniel":"sam",
	"jays":"boyi",
	"josh":"boyi"

}

# comp={key+"ua" for key,value in dom.items() if value =="boyi"}

# print(comp)

# nd={k:ko for k,ko in dom.items()}

# import random

# Test 
# generate a random score for each names using dictionary comprension
# names=['joshua','samuel','emma','chamberlin','precious']

# student_score={name: random.randint(23,97) for name in names }
# print(student_score)

# passed_student={key:value for key,value in student_score.items() if value >=60}

# print('\n',passed_student)



# Test 
# loop through the sentence and get every word as key and the length of the word as value 
# using dictionary comprension

# sentence='What is the Airspeed Velocity of an Unladen Swallow?'

# word_length={word:len(word) for word in sentence.split()}

# print(word_length)


# Test 
# convert day temperature from celcius to farenhight
# weather_c={
# 	"Monday":12,
# 	"Tuesday":14,
# 	"Wednesday":15,
# 	"Thursday":14,
# 	"Friday":21,
# 	"Saturday":22,
# 	"sunday":24
# }


# weather_in_farenheight={day:((w_c*9/5)+32) for day , w_c in weather_c.items()  }

# print(weather_in_farenheight)



# Learinig 
# Loop in rows in a dataframe in pandas
student_dict={
	"student":["Joshua","Daniel","Solomon","Ubani"],
	"Score":[56,76,98,99]
}

import pandas
s_df=pandas.DataFrame(student_dict)

# for key,value in s_df.items():
# 	# print(key[1],value[1])   # To get the particlar row by index
# 	print(key,value)


for index,item in s_df.iterrows(): # pandas dataframe method iterrows to loop through the
	if item.student =="Joshua":    # DataFrame easily ....
		print(item)





		