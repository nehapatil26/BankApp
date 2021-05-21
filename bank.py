class Bank:

    def __init__(self, name, address, phone, email):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email

        self.__accounts = []

    def open_account(self, account):
        account.set_account_no(len(self.__accounts) + 1)

        self.__accounts.append(account)

    def close_account(self, account_no):
        index = 0
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                self.__accounts.pop(index)
                print("Successfully closed your account.")
                break
            index += 1
        else:
            print("Account no does not exists")

    def new_deposit(self, transaction):
        receiver_account_no = transaction.get_receiver_account_no()

        for account in self.__accounts:
            if account.get_account_no() == receiver_account_no:
                account.deposit(transaction)
                break
            else:
                print("Account doest not exist")


    def create_transaction(self, transaction):
        account_no = transaction.get_account_no()

        for account in self.__accounts:
            if account.get_account_no() == account_no:
                if transaction.get_transaction_type() == 1:
                    account.deposit(transaction)
                elif transaction.get_transaction_type() == 2:
                    account.withdraw(transaction)
                elif transaction.get_transaction_type() == 3:
                    account.withdraw(transaction)
                    self.new_deposit(transaction)
                break
        else:
            print("Account doest not exist")

    def list_account(self):
        print("-" * 115)
        print("{:^115}".format(f"{self.__name} ACCOUNTS"))
        print("-" * 115)
        print("{:<5}{:<15}{:<15}{:^35}{:<20}{:<15}{:<15}".format("ID", "NAME", "ADDRESS", "EMAIL", "CONTACT", "A/C TYPE", "BALANCE"))
        print("-" * 115)

        for account in self.__accounts:
              account.print_info()

        print("-" * 115)

    def list_transaction(self, account_no):
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                account.list_transactions()
                break
            else:
                print("Account does not exist")


