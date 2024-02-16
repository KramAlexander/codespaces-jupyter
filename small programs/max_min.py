import random
import time

# explanation message
print("You have to give me two numbers but one after one. I will generate random numbers then and give you the maximum and minimum :)\n")

# getting numbers range
low = int(input("What is the start of the targeted range\n"))
high = int(input("Great! Which number is the end of the range?\n"))

print("Generating numbers...")
time.sleep(2)

# creating numbers in a list
numbers = []
for i in range(low,high):
    numbers.append(random.randint(low,high))
    
# removing duplicates and printing numbers
numbers = list(set(numbers))
print(f"Your numbers are: {numbers}")

# functions for getting max and min value of list numbers
def max(numbers):
    value = numbers[0]
    for i in numbers:
        if i > value:
            value = i
    return value

def min(numbers):
    value = numbers[0]
    for i in numbers:
        if i < value:
            value = i
    return value

# printing max and min
print(f"The maximum is number {max(numbers)}.")
print(f"The minimum is number {min(numbers)}.")
