from bank import Bank
from account import Account
from transaction import Transaction
import datetime

bank = Bank("QORBITAL", "Pune", "+919876543219", "customer_support@qovarian.com")

def dummy_accounts():
    dummy_accounts = [
        {"name":"krishnat", "address":"kolhapur","email":"krishna.shinde@qovarian.com", "phone": "+918237631519", "balance": 0, "account_type": 1},
        {"name": "abhishek", "address": "aurangabad", "email": "abhishek.choudhary@qovarian.com", "phone": "+918378000531", "balance": 500, "account_type": 1},
        {"name": "neha", "address": "aurangabad", "email": "neha.patil@qovarian.com", "phone": "+919689247083", "balance": 3000, "account_type": 1},
        {"name": "hrushikesh", "address": "pune", "email": "hrushikesh.sangale@qovarian.com", "phone": "+918888389588", "balance": 1500, "account_type": 1},
        {"name": "mahesh", "address": "nanded", "email": "mahesh.gudmalwar@qovarian.com", "phone": "+918983997677", "balance": 5000, "account_type": 1},
        {"name": "sakshi", "address": "solapur", "email": "sakshi.mangrule@qovarian.com", "phone": "+919921527469", "balance": 10000, "account_type": 1}
    ]

    for dummy_account in dummy_accounts:
        account = Account(dummy_account['name'], dummy_account['address'], dummy_account['email'], dummy_account['phone'], dummy_account['balance'], dummy_account['account_type'])
        bank.open_account(account)

def show_menu():
    print("Welcome user...")
    print("0. List all the accounts")
    print("1. Open an account")
    print("2. Closed an account")
    print("3. Deposite amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6. List all transactions")
    print("7. Exit")
    print("Please select your option : ")

    try:
        choice = int(input())
    except Exception:
        print("invalid option")
        choice = -1
    return choice

def open_account():
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone = input("Enter your phone : ")
    email = input("Enter your email : ")
    balance = float(input("Enter your initial balance : "))
    account_type = int(input("Enter your account type (1: SAVING, 2:CURRENT, 3:DEMAT)"))

    account = Account(name, address, phone, email, balance, account_type)

    bank.open_account(account)

    print("Congrats...Your account is now active...")



def list_accounts():
    print("list of accounts")
    bank.list_account()

def open_account():
    # using dummy accounts :
    dummy_accounts()
    # get the data from input :
    # open_account()

def close_account():
    account_no = int(input("To close your account, Enter your account no : "))
    bank.close_account(account_no)

def deposit():
    account_no = int(input("To deposite amount, Enter your account no : "))
    amount = float(input("Enter amount to be deposited : "))
    transaction = Transaction(1, amount, datetime.date.today().isoformat(), account_no, 0)
    bank.create_transaction(transaction)


def withdraw():
    account_no = int(input("To withdraw amount, Enter your account no : "))
    amount = float(input("Enter amount to be withdrawl : "))
    transaction = Transaction(2, amount, datetime.date.today().isoformat(), account_no, 0)
    bank.create_transaction(transaction)

def transfer():
    account_no = int(input("To transfer amount, Enter your account no : "))
    amount = float(input("Enter amount to be transfer : "))
    receiver_account_no = int(input("To transfer amount, Enter Receiver account no : "))
    transaction = Transaction(3, amount, datetime.date.today().isoformat(), account_no, receiver_account_no)
    bank.create_transaction(transaction)


def list_transactions():
    account_no = int(input("To list transaction, Enter your account no : "))
    bank.list_transaction(account_no)


while True:
    choice = show_menu()

    if choice == 0:
        list_accounts()
    elif choice == 1:
        open_account()
    elif choice == 2:
        close_account()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        transfer()
    elif choice == 6:
        list_transactions()
    elif choice == 7:
        print("exiting...")
        break
    else:
        print("You have entered a wrong option")

    print()
    print("Enter key to continue...")
    ch = input()
