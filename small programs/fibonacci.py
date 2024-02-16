number = int(input("Which fibonacci-number to you want to calculate?\n"))

def fib(number):
    if number == 0 or number == 1:
        print("Y")
        return 1
    else:
        return fib(number-2)+fib(number-1)
        
    
print(f"The {number}. number of the fibonacci-row is {fib(number)}")