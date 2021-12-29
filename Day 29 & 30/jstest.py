import json

new_data={
	'joshua':{'python':'programmers'},
}

# with open("my_words.json",'r')as file:
# 	data=json.load(file)
# 	data.update(new_data)
# 	nf=open("my_words.json",'w')
# 	json.dumps(data,nf,indent=4)	

# # write to json file
# with open("my_words.json",'w')as file:
# 	print('i came here..'.title())
# 	json.dump(data,file,indent=4)
# 


# json_string=json.dumps(new_data,indent=2)

# with open('my_words.json','a')as file:
# 	file.write(json_string)




file={
	"Instagram":{
		"username":"Joshua boyi",
		"password":"0825654255"
	}
}

#  read from a json file

# with open("my_words.json",'r')as data:
# 	new_data=json.load(data)
# 	print(new_data)

#Write to a json file

# with open("my_words.json","w")as data:
# 	json.dump(file,data,indent=4)



# Update or append to a  JSON FILE

with open("my_words.json","r")as data:
	new_data=json.load(data)

	new_data.update(file)


with open("my_words.json","w")as data:
	json.dump(new_data,data,indent=4)




























