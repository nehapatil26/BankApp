class Account():

    def __init__(self, name, address, email, phone, balance, account_type):

        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__balance = balance
        self.__account_type = account_type
        self.__account_no = 0

        self.__transactions = []

    def set_account_no(self, no):
        self.__account_no = no

    def get_account_no(self):
        return self.__account_no

    def deposit(self, transaction):
        self.__transactions.append(transaction)

        self.__balance += transaction.get_amount()

    def withdraw(self, transaction):
        if self.__balance - transaction.get_amount() <= 0:
            print("Insufficient balance")
        else:
            self.__transactions.append(transaction)

            self.__balance -= transaction.get_amount()


    def list_transactions(self):
        print("-" * 60)
        print("{:^60}".format("List of transactions"))
        print("-" * 60)
        print("{:<20}{:>10}{:>20}".format("DATE", "BALANCE", "TX TYPE"))
        print("-" * 60)
        for transaction in self.__transactions:
            transaction.print_info()
        print("-" * 60)

    def print_info(self):
        str_type = ''
        if self.__account_type == 1:
            str_type = 'SAVING'
        elif self.__account_type == 2:
            str_type = 'CURRENT'

        print("{:<5}{:<15}{:<15}{:<35}{:<20}{:<15}{:<15}".format(self.__account_no, self.__name, self.__address, self.__email, self.__phone, str_type, self.__balance))