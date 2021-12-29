import csv
import pandas
import math
# with open('weather_data.csv')as data_file:
# 	data=csv.reader(data_file)
# 	temperatures=[]
# 	for each in data:
# 		if each[1]!='temp':
# 			temperatures.append(int(each[1]))
# 	print(temperatures)f



# with open("weather_data.csv")as data:
# 	allCaps=data.readlines()
# 	print(allCaps)


data=pandas.read_csv('weather_data.csv')


# row_search=data[data.temp ==22]

# print(row_search)


# Challange Get Average temperature ...

# data_list=data['temp'].to_list()

# a_temp=sum(data_list)/len(data_list)

# print(a_temp)


# TO GET THE AVERAGE WITH AN INBUILT FUNCTION 

# mean=data.temp.mean()
# print(mean)

# CHALLANGE TO GET THE MAX VALUE FROM AN IN BUILT METHOD
# print(data.temp.max())


# print(data[data['condition'] == "Rain"])

# CHALLANGE PULL OUT THE DATA FROM THE ROW WHERE THAT HAS THE MAXIMUM TEMPERATURE

# max_row_temp=data[data.temp==data.temp.max()]

# print(max_row_temp['temp'])

# CHALLANGE  PULL OUT THE TEMP FROM THE MONDAY ROW AND CONVERT IT FROM CELCIUS TO FARENHIGHT
# monday=data[data.day=="MonDAy".title()]

# # FARENHIGHT= (CELCIUS*9/5)+32

# print('your answer in FARENHIGHT : ',(monday.temp*9/5)+32)

# TO CREATE A NEW DATAFRAME 

my_dicts={
	'boys':["josh","daniel",'samuel'],
	"girls":['benita','ofuje','omeime']
}

my_datas=pandas.DataFrame(my_dicts) 
my_datas.to_csv("new_csv_gender.csv")






