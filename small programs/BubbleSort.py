# user input for numbers
import random
amount = int(input("How many numbers do you want to sort?\n"))

# filling a list with random numbers
numbers = []
for i in range(amount):
    choice = random.randint(0,100)
    numbers.append(choice)
# converting list into set into list to remove duplicates
numbers = list(set(numbers))

# 
for number in numbers:
    for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                storage = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = storage

print(numbers)