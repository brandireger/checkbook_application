
filename = 'my_checkbook_plus.txt'

#Check if file exists
import os.path
from os import path

if not path.exists(filename):
    with open(filename, 'w') as f:
        f.write(f'0 , {transaction_time} , starting balance')

# Timestamp function
from datetime import datetime

def transaction_time():
    dateTimeObj = datetime.now()
    timeStr = dateTimeObj.strftime('%Y-%m-%d')
    return print(f' , {timeStr}')

# Menu functions
def menu_choice():
    choice = input('What would you like to do?\n\n\
1) view current balance\n\
2) record a debit (withdraw)\n\
3) record a credit (deposit)\n\
4) view all historical transactions\n\
5) view all transactions for a single day\n\
6) view all transactions in a category\n\
7) exit\n')

    while choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print(f'Invalid choice: {choice}')
        choice = input('What would you like to do?\n\n\
1) view current balance\n\
2) record a debit (withdraw)\n\
3) record a credit (deposit)\n\
4) view all historical transactions\n\
5) view all transactions for a single day\n\
6) view all transactions in a category\n\
7) exit\n')

    else:
        return choice

def debit_category_choice():
    choice = input('Please select a category for this withdrawal: \n\
a = work expense \n\
b = school expense \n\
c = household expense \n\
d = other\n')
    
    while choice not in ['a', 'b', 'c', 'd']:
        print('Invalid selection. Please try again.')
        choice = input('Please select a category for this withdrawal: \n\
a = work expense \n\
b = school expense \n\
c = household expense \n\
d = other expense\n')
    
    else:
        return choice

def credit_category_choice():
    choice = input('Please select a category for this deposit: \n\
a = paycheck \n\
b = gift \n\
c = tax returns \n\
d = other income\n')
 
    while choice not in ['a', 'b', 'c', 'd']:
        print('Invalid selection. Please try again.')
        choice = input('Please select a category for this deposit: \n\
a = paycheck \n\
b = gift \n\
c = tax returns \n\
d = other\n')

    else:
        return choice


# clean list of transactions
def get_cleaned_transactions():
    with open(filename) as f:
        lines = f.read().split('\n')
        all_list = []
        for line in lines:
            all_list.append(line.split(' , '))
        return all_list

# balance function
def balance():
    all_list = get_cleaned_transactions()
    total = 0
    balance = []
    for sublist in all_list:
        balance.append(sublist[0])
    for b in balance:
        total += float(b)
    return round(total, 2)

# debit function
def debit(debit_prompt):
    debit_prompt = float(debit_prompt)
    with open(filename, 'a') as f:
        if debit_prompt > balance():
            return print('balance is too low for this debit')
        
        else:
            debit_category = debit_category_choice()
            
            while debit_category not in ['a', 'b', 'c', 'd']:
                print('Invalid selection. Please try again.')
                debit_category_choice()
            
            if debit_category == 'a':
                f.write('\n' + f'-{debit_prompt} , {transaction_time()} , work expense')
                return print(f'Withdrew ${debit_prompt}, new balance is ${round(balance(), 2)}.')
            elif debit_category == 'b':
                f.write('\n' + f'-{debit_prompt} , {transaction_time()} , school expense')
                return print(f'Withdrew ${debit_prompt}, new balance is ${round(balance(), 2)}.')
            elif debit_category == 'c':
                f.write('\n' + f'-{debit_prompt} , {transaction_time()} , household expense')
                return print(f'Withdrew ${debit_prompt}, new balance is ${round(balance(), 2)}.')
            elif debit_category == 'd':
                f.write('\n' + f'-{debit_prompt} , {transaction_time()} , other expense')
                return print(f'Withdrew ${debit_prompt}, new balance is ${round(balance(), 2)}.')

            else:
                return print('Something went wrong!')

# credit function
def credit(credit_prompt):
    with open(filename, 'a') as f:
        credit_category = credit_category_choice()

        while credit_category not in ['a', 'b', 'c', 'd']:
            print('Invalid selection. Please try again.')
            credit_category_choice()

        if credit_category == 'a':
            f.write('\n' + f'{float(credit_prompt)} , {transaction_time()} , paycheck')
            return print(f'Deposited ${float(credit_prompt)}, new balance is ${round(balance(), 2)}.')
        elif credit_category == 'b':
            f.write('\n' + f'{float(credit_prompt)} , {transaction_time()} , gift')
            return print(f'Deposited ${float(credit_prompt)}, new balance is ${round(balance(), 2)}.')
        elif credit_category == 'c':
            f.write('\n' + f'{float(credit_prompt)} , {transaction_time()} , tax returns')
            return print(f'Deposited ${float(credit_prompt)}, new balance is ${round(balance(), 2)}.')
        elif credit_category == 'd':
            f.write('\n' + f'{float(credit_prompt)} , {transaction_time()} , other')
            return print(f'Deposited ${float(credit_prompt)}, new balance is ${round(balance(), 2)}.')
        else:
            return print('Something went wrong!')

# All transactions to date function
def all_transactions():
    with open(filename) as f:
        transactions = f.readlines()
        for i, line in enumerate(transactions, 1):
            print(f'{i}. ', line)

# allow viewer to see all transactions from a given day
def trans_by_day(day_prompt):
    all_list = get_cleaned_transactions()
    date_list = []
    for line in all_list:
        if line[1] == day_prompt:
            date_list.append(line)
    for x, y in enumerate(date_list, 1):
        print(x, y)

# show all transactions in a category
def get_categories():
    cat_choice = input('What category would you like to select?\n\
a = work expense \n\
b = school expense \n\
c = household expense \n\
d = other expense\n\
e = paycheck \n\
f = gift \n\
g = tax returns \n\
h = other income\n')
    
    while cat_choice not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        print('Invalid selection. Please try again.')
        cat_choice = input('What category would you like to select?\n\
a = work expense \n\
b = school expense \n\
c = household expense \n\
d = other expense\n\
e = paycheck \n\
f = gift \n\
g = tax returns \n\
h = other income\n')
        
    if cat_choice == 'a':
        category = 'work expense'
    elif cat_choice == 'b':
        category = 'school expense'
    elif cat_choice == 'c':
        category = 'household expense'
    elif cat_choice == 'd':
        category = 'other expense'
    elif cat_choice == 'e':
        category = 'paycheck'
    elif cat_choice == 'f':
        category = 'gift'
    elif cat_choice == 'g':
        category = 'tax returns'
    elif cat_choice == 'b':
        category = 'other income'
    else: 
        print('Something went wrong!')
        
    all_list = get_cleaned_transactions()
    cat_list = []
    for line in all_list:
        if line[2] == category:
            cat_list.append(line)
    for x, y in enumerate(cat_list, 1):
        print(x, y)
    return print(f'Showing all transactions in category: {category}')

# checkbook app
print()
print('~~~ Welcome to your terminal checkbook! ~~~')
print()

menu_variable = True

while menu_variable == True:
    userchoice = menu_choice()
    print()

    while userchoice not in ['1', '2', '3', '4', '5', '6', '7']:
        print(f'Invalid choice: {userchoice}')
        userchoice = menu_choice()

    # 1: view current balance
    if userchoice == '1':
        print(f'Your choice?: {userchoice}')
        print()
        print(f'Your current balance is ${round(balance(), 2)}.')
        print()
        userchoice = menu_choice()

    # 2: debit
    elif userchoice == '2':
        print(f'Your choice?: {userchoice}')
        print()
        debit_prompt = input('How much is the debit? ')
        debit(debit_prompt)
        print()
        userchoice = menu_choice() 

    # 3: credit
    elif userchoice == '3':
        print(f'Your choice?: {userchoice}')
        print()
        credit_prompt = input('How much is the credit? ')
        credit(credit_prompt)
        print()
        userchoice = menu_choice()
    
    # 4: All transactions in file
    elif userchoice == '4':
        print(f'Your choice?: {userchoice}')
        print()
        print(all_transactions())
        userchoice = menu_choice()

    # 5: transactions on a given day
    elif userchoice == '5':
        print(f'Your choice?: {userchoice}')
        print()
        day_prompt = input('Please enter a day in this format: yyyy-mm-dd\n')
        print(trans_by_day(day_prompt))
        userchoice = menu_choice()

    # 6: view all transactions in a category
    elif userchoice == '6':
        print(f'Your choice?: {userchoice}')
        print()
        get_categories()
        userchoice = menu_choice()
        
    elif userchoice == '7':
        menu_variable = False

    else:
        print('Something went wrong!')
        break

# 7: exit
print(f'Your choice?: {userchoice}')
print()
print('Thanks, have a great day!')


