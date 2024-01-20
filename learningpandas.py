import pandas as pd

mydataset = {
    'cars': ["BMW", "Porsche", "Audi", "Ford"],
    'passings': [3,7,2,5]
    }

calories = {"day1": 420, "day2": 380, "day3": 390}

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
a = [1,7,3]
myvar = pd.DataFrame(mydataset)
myvar2 = pd.Series(a, index = ["x","y","z"])
myvar3 = pd.Series(calories)
myvar4 = pd.DataFrame(data)

print("-----------------")
print(myvar)
print("-----------------")
print(pd.__version__)
print("-----------------")
print(myvar2)
print("-----------------")
print(myvar2[2])
print("-----------------")
print(myvar2["y"])
print("-----------------")
print(myvar3)
print("-----------------")
print(myvar4)