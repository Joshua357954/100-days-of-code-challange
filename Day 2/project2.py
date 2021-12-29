
# Welcome to the day two project of the 100 days of code

print("Welcome to the bill calculator")

bill=float(input("What is the total bill : $"))

num_of_people=int(input("How many people are spliting the bill : "))

per_tip=int(input("Which percentage tip will you give ? 10 ,12, 15  : "))

# bill * percentage_tip  divide by 100 and add the bill and diivide everything by the number of people

total_bill =((bill*per_tip/100)+bill)/num_of_people

print(f"Your total bill is {round(total_bill,2)}")


