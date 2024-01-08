# AND Gate
def AND(a,b):
    if (a == b and a == 1):
        return True
    else:
        return False
print("0 | 0 | 0\n0 | 1 | 0\n1 | 0 | 0\n1 | 1 | 1\n---------")
print(AND(1,1))

# OR Gate
def OR(a,b):
    if(a == 1 or b == 1):
        return True
    else: 
        return False
print("0 | 0 | 0\n0 | 1 | 1\n1 | 0 | 1\n1 | 1 | 1\n---------")
print(OR(1,1))

# NOT Gate
def NOT(a):
    if(a == 1):
        return False
    else: 
        return True
print("0 | 1\n1 | 0\n-----")
print(NOT(1))

# NAND Gate
# NOR Gate
# XOR Gate
# XNOR Gate


