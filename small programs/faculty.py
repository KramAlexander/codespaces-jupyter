# getting user-input for faculty
number = int(input("Please enter a number:\n"))

# recursive function for calculating faculty
def fak(number):
    if number == 0:
        return 1
    else:
        fakulty = number*fak(number-1)
        return fakulty

# printing faculty    
print(f"The faculty of {number} is {fak(number)}")