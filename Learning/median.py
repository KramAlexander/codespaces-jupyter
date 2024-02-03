# getting user input for amount
import random
amount = int(input("Enter a amount pls\n"))

# getting biggest number of function
def maximum(numbers):
    value = numbers[0]
    for i in numbers:
        if i > value:
            value = i
    return value

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

global median_list
median_list = new_list1
# median 
print(median_list)
def median():
    if len(median_list) % 2 == 0:
        median = median_list[int(((len(median_list)/2-1)+len(median_list)/2)/2)]
    else:
        median = median_list[int(len(median_list)/2)]
    return median

print(median())