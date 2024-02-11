import re

list = [1,5,5,8,10]

def find_max_min(list):
    return min(list), max(list)
print(find_max_min(list))

transactions = [
    {'type':'purchase','amount':50,'date':'2024-01-14'},
    {'type':'purchase','amount':50,'date':'2024-01-14'}]

transaction_type = transactions[0]['type']
transaction_amount = transactions[0]['amount']
transaction_date = transactions[0]['date']

def list_of(my_key):
    amount_values = [transaction['amount'] for transaction in transactions]
    return amount_values
print(list_of('amount'))

def sum_up(my_type):
    amount_values = [transaction['amount'] for transaction in transactions
if transaction['type']==my_type]
    return(sum(amount_values))

income = sum_up('purchase')
expenses = sum_up('sale')
print("income =", income)
print("expenses =",expenses)

if(income > expenses): print("You made money")
else: print("You lost money!")

def find_all(my_key,my_value):
    values = [transaction for transaction in transactions if
transaction[my_key] == my_value]
    return values

my_transactions = find_all('date','2024-01-2024')
print(my_transactions)
print(len(my_transactions))

my_date = my_transactions[0]['date']
print(my_transactions[0]['date'])
print(type(my_date))
#print(is_valid_date_format(my_date))

def is_valid_date_format(date_string):
    test = 0

print(re.compile("14-01-2024"))