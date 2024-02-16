# getting user inputs for number and power 
number = int(input("Please enter a number:\n"))
exponent = int(input("Please enter a number for the exponent:\n"))

# function for calculating the power with given values
def pow(number,exponent):
    if exponent == 0:
        return 1
    else:
       power = number * pow(number,exponent-1)
       return power

# printing out the calculated values   
print(f"The result of {number} to the power of {exponent} is {pow(number,exponent)}.")