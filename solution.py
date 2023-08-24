#Task 1
big_numbers = None
count = 0

while count < 3:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    
    if first_number == second_number:
        print("Numbers are equal")
    else:
        print("Numbers are not equal")
    
    if second_number > first_number:
        print("Second number is greater than first number")
    else:
        print("Second number is not greater than first number")
    
    if second_number >= first_number:
        print("Second number is greater than or equal to first number")
    else:
        print("Second number is not greater than or equal to first number")
    
    if first_number > 100 and second_number > 100:
        print("Both numbers are big!")
        big_numbers = True
    else:
        print("Both numbers are not big!")
        big_numbers = False
        
    print(f"big_numbers is set to {big_numbers}")
    count += 1

    #Task2
Months = {
    "January" : 31,
    "February" : 28,
    "March" : 31,
    "April" : 30,
    "May" : 31,
    "June" : 30,
    "July" : 31,
    "August" : 31,
    "September" : 30,
    "October" : 31,
    "November" : 30,
    "December" : 31
}


print(Months)
month_name = (input(" wich month "))

if month_name in Months:
    days = Months[month_name]
    print("Number of days are", days, "in", month_name )
else:
    print("Give me a Months")

