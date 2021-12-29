

def minus(a,b):
	return a-b

def plus(a,b):
	return a+b

# def calculate(n1,n2,func=plus):

# 	return func(n1,n2)

# print(calculate(50,20,func=plus))




def calc(path='',func=' '):

	if func:
		if func.lower()=='byte':
			return to_byte(file)

		elif func.lower()=='kb':
			return to_kb(file)

		elif func.lower()=='mb':
			return to_mb(file)

		elif func.lower()=='gb' :
			return to_gb(file)
		else:
			raise KeyError("invalid keyword entered")
	else:
		pass
















