# -----LIBRARIES-----

import random

users = {}
# users = {user_id: {forename: 'John', surname: 'Smith', password: 'abc123',
#                    accounts: {acc_num: {acc_type: "Current Account", balance: 1000}}}}


# -----CLASSES-----

# Parent class
class Bank:
    def __init__(self, user_id, password, forename, surname, acc_num):
        self.user_id = user_id
        self.password = password
        self.forename = forename
        self.surname = surname
        self.balance = 0
        self.acc_num = acc_num

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance

    @staticmethod
    def acc_num_generator():
        return random.randint(100000, 999999)

    @staticmethod
    def validate_password(password):
        # Ensure password is >= 8 chars and contains a number
        return len(password) >= 8 and any(char.isdigit() for char in password)


# Child class
class CurrentAccount(Bank):
    def __init__(self, user_id, password, forename, surname, acc_num):
        super().__init__(user_id, password, forename, surname, acc_num)
        self.acc_type = "Current Account"
        self.overdraft_limit = 1000

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return "Insufficient funds. Overdraft limit reached"
        else:
            self.balance -= amount
            return self.balance


class SavingsAccount(Bank):
    def __init__(self, user_id, password, forename, surname, acc_num):
        super().__init__(user_id, password, forename, surname, acc_num)
        self.acc_type = "Savings Account"
        self.interest_rate = 0.05

    def apply_interest(self):
        self.balance += (self.balance * self.interest_rate)
        return self.balance


# -----FUNCTIONS-----

# Account number generator
# def acc_num_generator():
#     return random.randint(100000, 999999)


# Create new password
def validate_new_password():
    password = input("Create a password: ")
    while not Bank.validate_password(password):
        print("""Passwords must be alphanumerical and at least 8 characters with upper and lowercase letters
              Please try again""")
        password = input("Create a password: ")
    return password


# Register new user
def registration():
    forename = input("Enter your forename: ")
    surname = input("Enter your surname: ")
    user_id = input("Create a user id: ")

    password = input("Create a password: ")
    while not Bank.validate_password(password):
        print("""Passwords must be alphanumerical and at least 8 characters with upper and lowercase letters
              Please try again""")
        password = input("Create a password: ")

    password2 = input("Re-enter your password: ")
    while not password2 == password:
        print("The passwords do not match, please try again")
        password = input("Create a password: ")
        while not Bank.validate_password(password):
            print("""Passwords must be alphanumerical and at least 8 characters with upper and lowercase letters
                  Please try again""")
            password = input("Create a password: ")

        password2 = input("Re-enter your password: ")

    acc_num = Bank.acc_num_generator()

    print("Account created successfully")
    print(f"""Account details:
          Forename:\t{forename}
          Surname:\t{surname}
          User ID:\t{user_id}
          Acc No:\t{acc_num}
          Acc Type:\tPLACEHOLDER""")

# registration()


# Login

def login():
    user_id = input("Enter user_id: ")
    password = input("Enter password: ")

# login()


# -----MAIN PROGRAM-----

user_id = Bank('val1_user_id', 'val2_password',
               'val3_forename', 'val4_surname', 'val5_acc_num')
# print(user_id.user_id)
# print(user_id.user_id)

acc_num = SavingsAccount('val1_user_id', 'val2_password',
                         'val3_forename', 'val4_surname', 'val5_acc_num')

# print(acc_num.password)


# Input

# user_id = input("Enter user_id: ")
# password = input("Enter password: ")
# forename = input("Enter forename: ")
# surname = input("Enter surname: ")
# acc_num = int(input("Enter account number: "))

# print(user_id, password, forename, surname, acc_num)

# test_new_acc = SavingsAccount(user_id, password, forename, surname, acc_num)
# print(type(test_new_acc))