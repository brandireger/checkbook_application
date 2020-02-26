
filename = 'my_checkbook_plus.txt'

#Check if file exists
import os.path
from os import path

if not path.exists(filename):
    with open(filename, 'w') as f:
        f.write('0')

# Timestamp function
from datetime import datetime

def transaction_time():
    dateTimeObj = datetime.now()
    timeStr = dateTimeObj.strftime('%Y-%m-%d')
    print(f' , {timeStr}')

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
    with open(filename, 'a') as f:
        if float(debit_prompt) > balance():
            return print('balance is too low for this debit')
        
        else:
            category_choice = input('Please select a category for this withdrawal: \n\
a = work expense \n\
b = school expense \n\
c = household expense \n\
d = other ')
            
            while category_choice not in ['a', 'b', 'c', 'd']:
                print('Invalid selection. Please try again.')
                category_choice = input('Please select a category for this withdrawal: \n\
a = work expense \n\
b = school expense \n\
c = household expense \n\
d = other ')
            
            if category_choice == 'a':
                f.write('\n' + f'-{float(debit_prompt)} , {transaction_time()} , work expense')
                return print(f'Withdrew ${float(debit_prompt)}, new balance is ${round(balance(), 2)}.')
            elif category_choice == 'b':
                f.write('\n' + f'-{float(debit_prompt)} , {transaction_time()} , school expense')
                return print(f'Withdrew ${float(debit_prompt)}, new balance is ${round(balance(), 2)}.')
            elif category_choice == 'c':
                f.write('\n' + f'-{float(debit_prompt)} , {transaction_time()} , household expense')
                return print(f'Withdrew ${float(debit_prompt)}, new balance is ${round(balance(), 2)}.')
            elif category_choice == 'd':
                f.write('\n' + f'-{float(debit_prompt)} , {transaction_time()} , other expense')
                return print(f'Withdrew ${float(debit_prompt)}, new balance is ${round(balance(), 2)}.')

            else:
                return print('Something went wrong!')

# credit function
def credit(credit_prompt):
    with open(filename, 'a') as f:
        credit_category_choice = input('Please select a category for this deposit: \n\
a = paycheck \n\
b = gift \n\
c = tax returns \n\
d = other')
        while credit_category_choice not in ['a', 'b', 'c', 'd']:
            print('Invalid selection. Please try again.')
            credit_category_choice = input('Please select a category for this deposit: \n\
a = paycheck \n\
b = gift \n\
c = tax returns \n\
d = other')
        if credit_category_choice == 'a':
            f.write('\n' + f'{float(credit_prompt)} , {transaction_time()} , paycheck')
            return print(f'Deposited ${float(credit_prompt)}, new balance is ${round(balance(), 2)}.')
        elif credit_category_choice == 'b':
            f.write('\n' + f'{float(credit_prompt)} , {transaction_time()} , gift')
            return print(f'Deposited ${float(credit_prompt)}, new balance is ${round(balance(), 2)}.')
        elif credit_category_choice == 'c':
            f.write('\n' + f'{float(credit_prompt)} , {transaction_time()} , tax returns')
            return print(f'Deposited ${float(credit_prompt)}, new balance is ${round(balance(), 2)}.')
        elif credit_category_choice == 'd':
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

# checkbook app
print()
print('~~~ Welcome to your terminal checkbook! ~~~')
print()



print()
userchoice = input('What would you like to do?\n\n\
    1) view current balance\n\
    2) record a debit (withdraw)\n\
    3) record a credit (deposit)\n\
    4) view all historical transactions\n\
    5) view all transactions for a single day\n\
    6) view all transactions in a category\n\
    7) exit\n')

while userchoice not in ['1', '2', '3', '4', '5', '6']:
    print(f'Invalid choice: {userchoice}')
    userchoice = input('What would you like to do?\n\n\
        1) view current balance\n\
        2) record a debit (withdraw)\n\
        3) record a credit (deposit)\n\
        4) view all historical transactions\n\
        5) view all transactions for a single day\n\
        6) view all transactions in a category\n\
        7) exit\n')

while userchoice != '7':
    # 1: view current balance
    if userchoice == '1':
        print(f'Your choice?: {userchoice}')
        print()
        print(f'Your current balance is ${round(balance(), 2)}.')
        print()
        userchoice = input('What would you like to do?\n\n\
            1) view current balance\n\
            2) record a debit (withdraw)\n\
            3) record a credit (deposit)\n\
            4) view all historical transactions\n\
            5) view all transactions for a single day\n\
            6) view all transactions in a category\n\
            7) exit\n')

    # 2: debit
    elif userchoice == '2':
        print(f'Your choice?: {userchoice}')
        print()
        debit_prompt = input('How much is the debit? ')
        debit(debit_prompt)
        print()
        userchoice = input('What would you like to do?\n\n\
            1) view current balance\n\
            2) record a debit (withdraw)\n\
            3) record a credit (deposit)\n\
            4) view all historical transactions\n\
            5) view all transactions for a single day\n\
            6) view all transactions in a category\n\
            7) exit\n')   

    # 3: credit
    elif userchoice == '3':
        print(f'Your choice?: {userchoice}')
        print()
        credit_prompt = input('How much is the credit? ')
        credit(credit_prompt)
        print()
        userchoice = input('What would you like to do?\n\n\
            1) view current balance\n\
            2) record a debit (withdraw)\n\
            3) record a credit (deposit)\n\
            4) view all historical transactions\n\
            5) view all transactions for a single day\n\
            6) view all transactions in a category\n\
            7) exit\n')
    
    # 4: All transactions in file
    elif userchoice == '4':
        print(f'Your choice?: {userchoice}')
        print()
        print('All transactions to date: ', '\n',  all_transactions())
        userchoice = input('What would you like to do?\n\n\
            1) view current balance\n\
            2) record a debit (withdraw)\n\
            3) record a credit (deposit)\n\
            4) view all historical transactions\n\
            5) view all transactions for a single day\n\
            6) view all transactions in a category\n\
            7) exit\n')

    # 5: transactions on a given day
    elif userchoice == '5':
        print(f'Your choice?: {userchoice}')
        print()
        day_prompt = input('Please enter a day in this format: yyyy-mm-dd')
        print(f'All transaction on {day_prompt}' + trans_by_day(day_prompt))
        userchoice = input('What would you like to do?\n\n\
            1) view current balance\n\
            2) record a debit (withdraw)\n\
            3) record a credit (deposit)\n\
            4) view all historical transactions\n\
            5) view all transactions for a single day\n\
            6) view all transactions in a category\n\
            7) exit\n')

    # 6: view all transactions in a category
    elif userchoice == '6':
        print(f'Your choice?: {userchoice}')
        print()
        print(f'Showing all transactions in category {userchoice}: ')
        userchoice = input('What would you like to do?\n\n\
            1) view current balance\n\
            2) record a debit (withdraw)\n\
            3) record a credit (deposit)\n\
            4) view all historical transactions\n\
            5) view all transactions for a single day\n\
            6) view all transactions in a category\n\
            7) exit\n')
        
    else:
        print('Something went wrong!')
        break


# 7: exit
print(f'Your choice?: {userchoice}')
print()
print('Thanks, have a great day!')


