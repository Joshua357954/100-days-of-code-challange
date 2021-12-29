import pandas


new_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

s_squ=new_data[new_data['Lat/Long'] =='POINT (-73.9639431360458 40.7908677445466)']

# all_adult_squirrel=new_data[new_data.Age=='Adult']

# print(all_adult_squirrel)

# adult_squirrel={
# 	"Age":all_adult_squirrel.Age.to_list()
# }
# # adult_squirrel=all_adult_squirrel.Age.to_dict()



# new_file=pandas.DataFrame(adult_squirrel)
# new_file.to_csv("My_mature_Suqirrel.csv")



# CHALLANGE FROM THE SQUIRRIEL DATA GET THE NUMBER OF SQUIRRIEL WITH BLACK ,GRAY AND WHITE FUR COLOR


b_squ=  new_data[new_data['Primary Fur Color']=="Black"]
gray_squ= new_data[new_data['Primary Fur Color']=="Gray"]
w_squ=  new_data[new_data['Primary Fur Color']=="Cinnamon"]

num_of_squ_of_diff_colors={
		"Fur_Color":["Black","Gray","Red"],
		"Count":[len(b_squ),len(gray_squ),len(w_squ)]
}



new1=pandas.DataFrame(num_of_squ_of_diff_colors)
new1.to_csv("Squirriel_Colors_Number.csv")