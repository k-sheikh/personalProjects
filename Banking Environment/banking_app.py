# BANKING ENVIRONMENT

# -----PSEUDOCODE-----

"""
# Program Structure Overview

Main Menu
	Welcome, Login, Register, Exit
		Login
			Enter user id, Enter password
				You have no accounts, Create account
					Account type: Savings, Current
					Save Classes to txt
				Select account
					Check balance, Withdraw, Deposit
						Deposit with cash, transfer from another account
				Create new account
					Account type: Savings, Current
					Save Classes to txt
		Register
			Create user id, password
			Verify user id, password
			Check for match, save to txt
"""

"""
# Dictionary Structure

users = {user_id : {
                    'forename' : 'John',
                    'surname' : 'Smith',
                    'password' : 'password123'
                    'accounts' : {
                                'account_num' : 12345678
                                'account_type' : 'Current Account'
                                'balance' : 5000
                    }}}
"""


# -----LIBRARIES-----

import re
import random
import stdiomask

users = {}


# -----CLASSES-----

class User:
    def __init__(self, forename, surname, user_id, password):
        self.forename = forename
        self.surname = surname
        self.user_id = user_id
        self.password = password
        self.account = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account


class Account:
    def __init__(self, account_number, account_type, balance = 0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient funds")
        

class Bank:
    def __init__(self):
        self.users = {}

    def register_user(self, forename, surname, password):
        user_id = generate_user_id(forename, surname)
        new_user = User(forename, surname, user_id, password)
        self.users[user_id] = new_user
        return new_user
    
    def create_account(self, user_id, account_type):
        account_number = generate_account_number()
        account = Account(account_number, account_type)
        self.users[user_id].add_account(account)
        return account


# -----UTILITY FUNCTIONS-----

def generate_user_id(forename, surname):
    return f"{forename[0].lower()}{surname[:5].lower()}{random.randint(1000, 9999)}"
    


# -----FUNCTIONS-----

# Welcome message
def welcome():
    print("\nWelcome to FatWest Bank")


# Main menu
def main_menu():
    user_input = input("""Please select from one of the following options:
1 - Login
2 - Register
3 - Exit
: """)
    while user_input not in ['1', '2', '3']:
        print("\nInput is not valid.")
        user_input = input("""Please select from one of the following options:
1 - Login
2 - Register
3 - Exit
: """)
    if user_input == '1':
        pass
    elif user_input == '2':
        register_new_user()
    elif user_input == '3':
        print("\nThankyou for banking with FatWest. Goodbye!")
        exit()


# Register new user
def register_new_user():
    forename = input("\nPlease enter your forename: ")
    surname = input("Please enter your surname: ")
    name_validation = input(
        f"Your name is {forename} {surname}, is this correct? Yes/No: ")
    while name_validation.lower() != 'yes':
        print("Please try again")
        forename = input("Please enter your forename: ")
        surname = input("Please enter your surname: ")
        name_validation = input(
            f"Your name is {forename} {surname}, is this correct? Yes/No: ")
    
    # User id generator
    id_num = id_num_generator()
    user_id = f"{forename[0].lower()}{surname[:5].lower()}{id_num}"
    print(f"\nYour user id is {user_id}\n")
    
    # Password and validation
    print("Please create a password.")
    while True:
        password = stdiomask.getpass("""Passwords must be alphanumerical,
must contain at least one uppercase letter,
must contain at least one lowercase letter,
must contain at least 8 characters.
Create a password now:  """, mask="*")
        
        # Check password criteria
        if (len(password) >= 8 and
            re.search("[a-z]", password) and
            re.search("[A-Z]", password) and
            re.search("[0-9]", password)):
            
            # Re-enter the password
            password2 = stdiomask.getpass("Please re-enter your password: ")
            
            # Check if passwords match
            if password == password2:
                break
            else:
                print("\nPasswords do not match. Please start again.")
        else:
            print("\nInvalid password, please try again.")

    
    # Add user data to dictionary
    user_data = {
        'forename' : forename,
        'surname' : surname,
        'password' : password
        }
    users[user_id] = user_data

    print(f"\nCongratulations {forename}, your account has been created successfully.")


# -----MAIN PROGRAM-----

while True:
    welcome()
    main_menu()
    # register_new_user()
    # print("Thanks!")
    # exit()