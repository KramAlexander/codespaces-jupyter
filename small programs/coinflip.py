import random
value = ''
def  inputting():
    global value
    value = ''
    while (value != "Kopf" and value != "Zahl" and value != "kopf" and value != "zahl"):
        value = str(input("Kopf oder Zahl?\n"))
    return value

print(f"You chose {inputting()}. Flipping a coin now... ")

numbers = ["Kopf","Zahl"]
result = random.choice(numbers)

if value == result:
    print(f"Congratulations! You won, the result was {result}.")
else: 
    print(f"Awwww! You lost, the result was {result}.")
