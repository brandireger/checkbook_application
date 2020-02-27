
filename = 'my_checkbook.txt'

#Check if file exists
import os.path
from os import path

if not path.exists(filename):
    with open(filename, 'w') as f:
        f.write('0')

# balance function
def balance(filename):
    with open(filename) as f:
        line = f.read().split('\n')
        balance = 0
        for x in line:
            balance += float(x)
        return round(balance, 2)

# debit function
def debit(debit_prompt):
    with open(filename, 'a') as f:
        if float(debit_prompt) > balance(filename):
            print('balance is too low for this debit')
        else:
            f.write('\n' + f'-{round(float(debit_prompt), 2)}')

# credit function
def credit(credit_prompt):
    with open(filename, 'a') as f:
        f.write('\n' + f'{round(float(credit_prompt), 2)}')

# checkbook app
print()
print('~~~ Welcome to your terminal checkbook! ~~~')
print()

def userchoice():
    prompt = input('What would you like to do?\n\n\
    1) view current balance\n\
    2) record a debit (withdraw)\n\
    3) record a credit (deposit)\n\
    4) exit\n')
    return prompt
print()
prompt = userchoice()

while prompt not in ['1', '2', '3', '4'] and prompt != '4':
    print(f'Invalid choice: {prompt}')
    prompt = userchoice()

while prompt != '4':
    # 1: view current balance
    if prompt == '1':
        print(f'Your choice?: {prompt}')
        # balance function goes here
        print()
        print(f'Your current balance is ${round(balance(filename), 2)}.')
        print()
        prompt

    # 2: debit
    elif prompt == '2':
        print(f'Your choice?: {prompt}')
        print()
        debit_prompt = input('How much is the debit? ')
        # debit function goes here
        debit(debit_prompt)
        if balance(filename) > float(debit_prompt):
            print(f'Withdrew ${round(float(debit_prompt), 2)}, new balance is ${round(balance(filename), 2)}.')
        print()
        prompt     

    # 3: credit
    elif prompt == '3':
        print(f'Your choice?: {prompt}')
        print()
        credit_prompt = input('How much is the credit? ')
        # credit function goes here
        credit(credit_prompt)
        print(f'Deposited ${round(float(credit_prompt), 2)}, new balance is ${round(balance(filename), 2)}.')
        print()
        prompt
        
    else:
        print('Something went wrong!')
        break

    prompt = userchoice()

# 4: exit
print(f'Your choice?: {prompt}')
print()
print('Thanks, have a great day!')


