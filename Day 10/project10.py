# This is the day 10  0f the 100days of code ........
# We are dealing with functions and later creating a calculator


def run_am(boy,girl=","):
	if boy =="" or girl=="":
		return "Please complete the fields and try again"
	
	return (girl +" "+boy)

(run_am("joshua","daniella"))




def is_leap(year):
	if year%4==0:
		if year%100==0:
			if year% 400==0:

				return True
			else:
				return False
		else:
			return True
	else:
		return False

def days_in_month(year,month) :

	month_days=[31,28,30,30,31,30,30,31,31,31,30,31]

	if is_leap(year) and month==2:

		return f"The number of days in month {month}/{year} is {29}  "

	return f"The number of days in month {month}/{year} is {month_days[month-1]} "

print(days_in_month(year=2020,month=3))



















