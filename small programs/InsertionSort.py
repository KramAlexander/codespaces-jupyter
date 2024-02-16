# import
import random

# getting biggest number of function
def maximum(numbers):
    value = numbers[0]
    for i in numbers:
        if i > value:
            value = i
    return value

# asking user for amount of numbers in list
amount = int(input("How many numbers do you want to sort?\n"))

# filling a list with random numbers from 0 - 100
numbers = []
for i in range(amount):
    choice = random.randint(0,100)
    numbers.append(choice)

# sorting out duplicates
numbers = list(set(numbers))

# sorting numbers through adding them to a new list
new_list1 = []
new_list2 = []
for number in range(len(numbers)):
    max = maximum(numbers)
    new_list1.insert(0,max)
    new_list2.append(max)
    numbers.remove(max)

print(f"Aufsteigend: {new_list1}")
print(f"Absteigend: {new_list2}")


