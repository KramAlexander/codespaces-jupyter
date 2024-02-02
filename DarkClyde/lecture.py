from faker import Faker
import random
fake = Faker()
#print(fake.name())

students = []

for _ in range(10):
    student = {
        "name": fake.name(),
        "age": random.randint(18,25),
        "major": random.choice(["Computer Science", "Mathematics","Physics"]),
        "gpa": round(random.uniform(2.0,4.0),2),
        "is_international": random.choice([True, False])
    }
    students.append(student)

for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    last_name = full_name.split()[1]
    print(first_name,last_name)

# printing all information about one student
print(students[0])

# printing specific information about one student
first_names = []
for student in students:
   first_name = student["name"].split()[0]
   first_names.append(first_name)
print(first_names)

# sorting out duplicates
duplicate_count = len(first_names) - len(set(first_names))
print(duplicate_count)

duplicate_count = {name: first_names.count(name)
                   for name in set(first_names)
                   if first_names.count(name) > 1}
print(duplicate_count)

# tets with list that has duplicates
first_names = ["John","jane","John","Alice","Bob","Jane"]
print(first_names)
duplicate_count = {name:first_names.count(name)
                   for name in set(first_names)
                   if first_names.count(name) > 1}
print(duplicate_count)

