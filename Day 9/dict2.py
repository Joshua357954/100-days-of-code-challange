

score={
	"joshua":90,
	"samuel":56,
	"emma":80,
	"cosmos":35,
	"bridget":75
}

students_grade={}

max_grade=max([score[keys] for keys in score])


for student in score:
	scores=score[student]
	if scores >= 90:
		students_grade[student]="Outstanding "
	elif scores >= 80:
		students_grade[student]="Very good "
	elif scores >=70:
		students_grade[student]="Good "
	else:
		students_grade[student]="Failed "

#print(students_grade)


# Nesting .....


josh_dict={

	"names": {'all_names':["joshua",'boyi',"ifeola"]},

	"boys": {"davtech":"isreal","davtech":"olamide"},

	"can_code":False,

	"locations":("portharcourt","edo state")
}


for item in josh_dict:
	if item=="can_code":
		josh_dict[item]=True


#print(josh_dict['names']['all_names'])

users=[
{
	"name":["joshua","boyi","ifeola"],
	"age":18,
	"can_code":True,
	"gender":"male",
},

{
	"name":["solomon","boyi","onimise"],
	"age":23,
	"can_code":False,
	"gender":"male",
}

]

# Write a function to add new users...

def add_new(name,age,can_code,gender):
	n_users={
		"name":name,
		"age":age,
		"can_code":can_code,
		"gender":gender
	}

	users.append(n_users)

def add_news(name,age,can_code,gender):
	global users
	n_users={}
	n_users["name"]=name
	n_users["age"]=age
	n_users["can_code"]=can_code
	n_users["gender"]=gender
	users.append(n_users)

add_news(["joy","ugo","kenneth"],19,False,"female")


for i in users:
	print(i['name'])












