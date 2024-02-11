import random

all = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!§%&/><°^*+-_()@"

length = int(input("How long should your random Password be?\n"))

password = ""
for i in range(length):
    password += random.choice(all)

print(f"Your random generated password is {password}")