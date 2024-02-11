# imports and global variable
import random
counter = 0

# getting range of list from user
start = int(input("Where should the list start?\n"))
end = int(input("Where should the list stop?\n"))

# creating list and filling it with unique numbers in given range
numbers = []
for i in range(end):
    numbers.append(random.randint(start,end))
numbers = list(set(numbers))

# getting number for searching-process
input_number = int(input("Give me a number\n"))

# function for checking if the list contains the number
def check_list():
    for element in numbers:
        global counter
        counter = counter + 1
        if element == input_number:
            return 1

# returning result of searching-process  
if check_list() == 1:
    print(f"The list contains the number {input_number} at position {counter}")
else: 
    print("Die Zahl ist nicht in der Liste")


   